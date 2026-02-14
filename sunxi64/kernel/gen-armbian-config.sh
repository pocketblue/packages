#!/usr/bin/env bash
set -euo pipefail

ARMBIAN_KERNEL_URL="https://raw.githubusercontent.com/armbian/build/refs/heads/main/lib/functions/compilation/armbian-kernel.sh"
OUTPUT="${1:-armbian.config}"
NO_BTF="${2:-}"

ARMBIAN_KERNEL_CONTENT="$(curl -fsSL "${ARMBIAN_KERNEL_URL}")"
exec 3<<<"${ARMBIAN_KERNEL_CONTENT}"
exec 4<<<"${ARMBIAN_KERNEL_CONTENT}"

# Minimal stubs expected by armbian-kernel.sh
function display_alert() { :; }
function run_host_command_logged() { "$@"; }
function exit_with_error() { echo "$*" >&2; exit 1; }

function version_cmp() {
  local v1="$1" v2="$2"
  local IFS=.
  local -a a b
  read -r -a a <<< "$v1"
  read -r -a b <<< "$v2"
  local len=${#a[@]}
  if (( ${#b[@]} > len )); then
    len=${#b[@]}
  fi
  local i ai bi
  for ((i=0; i<len; i++)); do
    ai=${a[i]:-0}
    bi=${b[i]:-0}
    if ((10#$ai > 10#$bi)); then
      echo 1
      return 0
    fi
    if ((10#$ai < 10#$bi)); then
      echo -1
      return 0
    fi
  done
  echo 0
}

function linux-version() {
  local cmd="$1" v1="$2" op="$3" v2="$4"
  if [[ "$cmd" != "compare" ]]; then
    echo "unsupported linux-version subcommand: $cmd" >&2
    return 2
  fi
  local cmp
  cmp=$(version_cmp "$v1" "$v2")
  case "$op" in
    ge) [[ $cmp -ge 0 ]] ;;
    gt) [[ $cmp -gt 0 ]] ;;
    le) [[ $cmp -le 0 ]] ;;
    lt) [[ $cmp -lt 0 ]] ;;
    eq) [[ $cmp -eq 0 ]] ;;
    ne) [[ $cmp -ne 0 ]] ;;
    *) echo "unsupported operator: $op" >&2; return 2 ;;
  esac
}

# Target context for Orange Pi 3 LTS
export ARCH="arm64"
export BRANCH="current"
export KERNEL_MAJOR_MINOR="6.18"
if [[ "${NO_BTF}" == "--no-btf" || "${NO_BTF}" == "no-btf" ]]; then
  export KERNEL_BTF="no"
else
  export KERNEL_BTF="${KERNEL_BTF:-}"
fi

# Arrays/dict used by armbian-kernel.sh
declare -a opts_y=() opts_n=() opts_m=()
declare -A opts_val=()

# Load Armbian kernel config hooks
# shellcheck disable=SC1090
source /dev/fd/3

# Call hooks in file order
mapfile -t hook_fns < <(awk '/^function armbian_kernel_config__/ {sub("function ", ""); sub(/\(\).*/, ""); print}' /dev/fd/4)

for fn in "${hook_fns[@]}"; do
  "$fn"
done

# Resolve final values in the same precedence as armbian_kernel_config_apply_opts_from_arrays
# opts_n -> opts_y -> opts_m -> opts_val

declare -A config_map=()

for opt in "${opts_n[@]}"; do
  config_map["$opt"]="n"
done
for opt in "${opts_y[@]}"; do
  config_map["$opt"]="y"
done
for opt in "${opts_m[@]}"; do
  config_map["$opt"]="m"
done
for opt in "${!opts_val[@]}"; do
  config_map["$opt"]="${opts_val[$opt]}"
done

# Write sorted config fragment
{
  printf '# Generated from %s\n' "${ARMBIAN_KERNEL_URL}"
  printf '# ARCH=%s BRANCH=%s KERNEL_MAJOR_MINOR=%s\n' "$ARCH" "$BRANCH" "$KERNEL_MAJOR_MINOR"
  printf '\n'
  for key in "${!config_map[@]}"; do
    printf '%s\n' "$key"
  done | sort | while IFS= read -r key; do
    printf 'CONFIG_%s=%s\n' "$key" "${config_map[$key]}"
  done
} > "${OUTPUT}"

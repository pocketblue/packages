### regreet rpm

building regreet rpm requires vendored cargo dependencies tarball

### get vendor tarball

```shell
git clone https://github.com/rharish101/ReGreet --branch=0.2.0 /tmp/regreet
cd /tmp/regreet
rust2rpm --path . --vendor=auto
install -D regreet-0.1.3-vendor.tar.xz ~/rpmbuild/SOURCES/regreet-0.2.0-vendor.tar.xz
```

we cloned 0.2.0 tag, but vendor tarball has 0.1.3 in it's name, and we are changing it to 0.2.0

### generate srpm

```shell
git clone https://github.com/pocketblue/extra-rpms /tmp/extra-rpms
cd /tmp/extra-rpms/regreet
spectool -g -R regreet.spec
rpmbuild -bs regreet.spec
```

### local build

```shell
mock ~/rpmbuild/SRPMS/regreet-0.2.0-1.fc43.src.rpm
```

### copr build

```shell
copr-cli build pocketblue/extra ~/rpmbuild/SRPMS/regreet-0.2.0-1.fc43.src.rpm
```

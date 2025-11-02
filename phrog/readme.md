### phrog rpm

building phrog rpm requires vendored cargo dependencies tarball

### get vendor tarball

```shell
git clone https://github.com/samcday/phrog /tmp/phrog
cd /tmp/phrog
rust2rpm --path . --vendor=auto
install -D phrog-0.46.0-vendor.tar.xz ~/rpmbuild/SOURCES/phrog-0.46.0-vendor.tar.xz
```

### generate srpm

```shell
git clone https://github.com/pocketblue/common-rpms /tmp/common-rpms
cd /tmp/common-rpms/phrog
spectool -g -R phrog.spec
rpmbuild -bs phrog.spec
```

### local build

```shell
mock ~/rpmbuild/SRPMS/phrog-0.46.0-1.fc43.src.rpm
```

### copr build

```shell
copr-cli build pocketblue/extra ~/rpmbuild/SRPMS/phrog-0.46.0-1.fc43.src.rpm
```

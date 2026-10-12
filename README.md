# homecontainer-selinux

SELinux container domain (`homecontainer.process`) that inherits the standard
container rules and adds read/write access to ordinary home files
(`user_home_t`). Sensitive home types such as `ssh_home_t`, `gpg_secret_t` and
`home_cert_t` stay inaccessible.

## Install

Download the RPM from the latest release and install it:

```
sudo dnf install https://github.com/zombiepigdragon/homecontainer-selinux/releases/download/v1.0/homecontainer-selinux-1.0-1.noarch.rpm
```

## Use in a quadlet

```ini
[Container]
SecurityLabelType=homecontainer.process
Volume=%h/myfiles:/data
```

Don't add `:z`/`:Z` to the volume; relabeling to `container_file_t` defeats the
purpose.

Verify with `ps -eZ | grep homecontainer`. Check denials with
`sudo ausearch -m avc -ts recent`.

## Releasing

1. Edit `homecontainer.cil`.
2. Bump `Version` (or `Release`) in `homecontainer-selinux.spec` and add a
   `%changelog` entry.
3. Commit, then tag and push: `git tag v1.1 && git push --tags`.

The workflow builds the RPM on Fedora and attaches it to the GitHub release.
It can also be run manually (workflow_dispatch); the RPM is then available as
a workflow artifact.

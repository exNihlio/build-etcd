Name:       etcd
Version:    v3.4.13
Release:    1
Summary:    etcd - a distributed, reliable key/value store
License:    Apache License - Version 2

%description
etcd is a distributed reliable key-value store for the most critical data of a distributed system, with a focus on being:
Simple: well-defined, user-facing API (gRPC)
Secure: automatic TLS with optional client cert authentication
Fast: benchmarked 10,000 writes/sec
Reliable: properly distributed using Raft

%pre 
if [ $(grep -c ^etcd /etc/passwd) == 0 ]; then
    /sbin/useradd --shell /sbin/nologin --no-create-home etcd
fi
%prep
if [ $(grep -c ^etcd /etc/passwd) == 0 ]; then
    /sbin/useradd --shell /sbin/nologin --no-create-home etcd
fi
%build

%install
if [ $(grep -c ^etcd /etc/passwd) == 0 ]; then
    /sbin/useradd --shell /sbin/nologin --no-create-home etcd
fi
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/etc/etcd.d
mkdir -p %{buildroot}/var/lib/etcd
mkdir -p %{buildroot}/usr/lib/systemd/system

install -m 755 etcdctl %{buildroot}/usr/local/bin/etcdctl
install -m 755 etcd %{buildroot}/usr/local/bin/etcd
install -m 0600 -o etcd -g root etcd.conf %{buildroot}/etc/etcd.d/etcd.conf
install -m 0644 etcd.service %{buildroot}/usr/lib/systemd/system
install -d -m 0750 -o etcd -g root %{buildroot}/var/lib/etcd

%files
%attr(0755, root, root) /usr/local/bin/etcdctl
%attr(0755, root, root) /usr/local/bin/etcd
%attr(0644, root, root) /etc/etcd.d/etcd.conf
/usr/lib/systemd/system/etcd.service
%attr(0750, etcd, root) /var/lib/etcd

%changelog

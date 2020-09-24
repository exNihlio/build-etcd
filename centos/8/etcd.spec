Name:       etcd
Version:    v3.4.13
Release:    1
Summary:    etcd - a distributed, reliable key/value store
License:    Apache License Version 2

%description
etcd

%prep
# we have no source, so nothing here

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 etcdctl %{buildroot}/usr/local/bin/etcdctl
install -m 755 etcd %{buildroot}/usr/local/bin/etcd

%files
/usr/local/bin/etcdctl
/usr/local/bin/etcd
%changelog

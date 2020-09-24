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

%prep

%build

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 etcdctl %{buildroot}/usr/local/bin/etcdctl
install -m 755 etcd %{buildroot}/usr/local/bin/etcd

%files
/usr/local/bin/etcdctl
/usr/local/bin/etcd
%changelog

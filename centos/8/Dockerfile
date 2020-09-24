FROM centos:8

ENV ETCD_URL="https://github.com/etcd-io/etcd/releases/download"
ENV ETCD_VER="v3.4.13"
ENV ETCD_ARCH="amd64"
ENV ETCD_URL="${ETCD_URL}/${ETCD_VER}/etcd-${ETCD_VER}-linux-${ETCD_ARCH}.tar.gz"
# The path inside the container where the rpm is copied to
ENV CONTAINER_PATH="/built_rpms"

WORKDIR /root

# Install the rpmbuild tools, set up our environment and download
# our code
RUN yum -y install rpm-build rpm-devel rpmlint rpmdevtools \
    && rpmdev-setuptree \
    && curl -L ${ETCD_URL} -o /root/rpmbuild/SOURCES/etcd-${ETCD_VER}-linux-${ETCD_ARCH}.tar.gz \
    && tar -C /root/rpmbuild/BUILD -xzvf /root/rpmbuild/SOURCES/etcd-${ETCD_VER}-linux-${ETCD_ARCH}.tar.gz \
    && ls /root/rpmbuild/SOURCES/ \
    && cp /root/rpmbuild/BUILD/etcd-${ETCD_VER}-linux-${ETCD_ARCH}/etcd /root/rpmbuild/BUILD/ \
    && cp /root/rpmbuild/BUILD/etcd-${ETCD_VER}-linux-${ETCD_ARCH}/etcdctl /root/rpmbuild/BUILD/

COPY etcd.spec /root/rpmbuild/SPECS/
COPY docker-entrypoint.sh /usr/local/bin/

RUN cd rpmbuild \
    # Buld the etcd RPM
    && rpmbuild -ba SPECS/etcd.spec

CMD /bin/bash /usr/local/bin/docker-entrypoint.sh

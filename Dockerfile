FROM haproxy:1.7
COPY ./certs /usr/local/etc/haproxy/certs
COPY ./haproxy/haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg

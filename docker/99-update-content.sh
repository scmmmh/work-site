#!/bin/bash
cd /var/www && \
./build.sh && \
chown -R nginx:nginx /var/www

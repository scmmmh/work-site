FROM nginx:stable

USER root

RUN apt-get update -y && \
    apt-get install -y git python3 python3-venv python3-pip

COPY docker/99-update-content.sh /docker-entrypoint.d
RUN chmod a+x /docker-entrypoint.d/99-update-content.sh
COPY docker/default.conf /etc/nginx/conf.d/default.conf

COPY ./ /var/www
RUN rm -rf /var/www/.venv /var/www/node_modules

#RUN git clone https://github.com/scmmmh/work-site.git /var/www && \

RUN    cd /var/www && \
    ./build.sh && \
    chown -R nginx:nginx /var/www

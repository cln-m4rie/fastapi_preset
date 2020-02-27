FROM nginx:latest

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get dist-upgrade -y

RUN mkdir -p /var/www/html
CMD ["/bin/bash", "-c", "nginx -g 'daemon off;'"]

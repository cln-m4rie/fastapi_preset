FROM nginx:latest

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt-get install -y tzdata
RUN echo "Asia/Tokyo" >  /etc/timezone
RUN cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

RUN mkdir -p /var/www/html
CMD ["/bin/bash", "-c", "nginx -g 'daemon off;'"]

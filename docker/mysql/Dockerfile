FROM mysql:5.7

RUN apt-get update -y
RUN apt-get install -y tzdata
RUN echo "Asia/Tokyo" >  /etc/timezone

RUN rm -rf /tmp/* /var/tmp/*
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /var/lib/apt/lists/*

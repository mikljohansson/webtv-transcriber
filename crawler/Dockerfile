FROM alpine:latest

# Runtime requirements
RUN apk -U add git python py-pip py-crypto rtmpdump ffmpeg

# To be able to build some Scrapy dependencies
RUN apk add gcc libc-dev python-dev libffi-dev openssl-dev libxml2-dev libxslt-dev
RUN pip install scrapy

# Install svtplay-dl
RUN git clone git://github.com/spaam/svtplay-dl
RUN pip install requests
ENV PATH ${PATH}:/svtplay-dl

VOLUME /data
WORKDIR /webtv

ADD scrapy.cfg /
ADD webtv /webtv/
ADD crawler.sh /

ENTRYPOINT ["/crawler.sh"]

FROM kaixhin/lasagne:latest

RUN apt-get -y install libav-tools python-scipy

VOLUME /data

ADD . /transcriber/
WORKDIR /transcriber

ENTRYPOINT ["python"]
CMD ["/transcriber/train.py"]

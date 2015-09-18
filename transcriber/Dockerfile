FROM kaixhin/lasagne:latest

VOLUME /data

ADD . /transcriber/
WORKDIR /transcriber

ENTRYPOINT ["python"]
CMD ["/transcriber/train.py"]

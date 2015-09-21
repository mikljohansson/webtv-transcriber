FROM kaixhin/lasagne:latest

RUN apt-get -y install libav-tools

RUN apt-get -y install gcc gfortran libopenblas-dev liblapack-dev
RUN pip install --upgrade scipy

VOLUME /data

ADD . /transcriber/
WORKDIR /

ENTRYPOINT ["python"]
CMD ["/transcriber/train.py"]

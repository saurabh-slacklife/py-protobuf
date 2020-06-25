from ubuntu-proto

ENV DEBIAN_FRONTEND=noninteractive

RUN apt install python3 python3-pip -y
RUN pip3 install protobuf

WORKDIR /app
COPY addressbook.proto .
COPY addressbook_pb2.py .
COPY test.py .

CMD ["python3","test.py"]

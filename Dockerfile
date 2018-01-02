FROM atilaromero/libyal:builder-debian-sid-1.3.2

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
  python-pip python-setuptools \
  liblzma-dev python-mock python-lzma

RUN pip install --upgrade pip
RUN pip install wheel
COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV LANG C.UTF-8
WORKDIR /usr/local/src/dfvfs
COPY ./ ./
RUN python run_tests.py

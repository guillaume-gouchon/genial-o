FROM resin/rpi-raspbian

# switch on systemd init system in container
ENV INITSYSTEM on
ENV READTHEDOCS True

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python \
        python-dev \
        python-numpy \
        python-scipy \
        python-smbus \
        espeak \
        rsync \
        rpi-update \
        wget \
        unzip

RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
        rm get-pip.py

# install Tensorflow
RUN wget https://github.com/samjabrahams/tensorflow-on-raspberry-pi/releases/download/v1.1.0/tensorflow-1.1.0-cp27-none-linux_armv7l.whl
ADD tensorflow-1.1.0-cp27-none-linux_armv7l.whl .
RUN pip install tensorflow-1.1.0-cp27-none-linux_armv7l.whl
RUN pip uninstall mock
RUN pip install mock
RUN cd libs/ && wget http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz

# pip install python deps from requirements.txt
# for caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# update Raspberry firmwares
RUN rpi-update

# copy sources
COPY . /app
WORKDIR /app



# run robot
CMD ["bash", "start.sh"]

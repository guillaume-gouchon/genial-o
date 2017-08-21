FROM resin/rpi-raspbian

# switch on systemd init system in container
ENV INITSYSTEM on
ENV READTHEDOCS True
ENV VERSION=0.0.1

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libdbus-1-dev \
		    libdbus-glib-1-dev \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python2.7 \
        python-dev \
        python-scipy \
        python-smbus \
        espeak \
        rsync \
        rpi-update \
        wget \
        unzip

# clean up dependencies
RUN  apt-get clean && \
        rm -rf /var/lib/apt/lists/*

# install pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
        rm get-pip.py

# copy sources
COPY . /app
WORKDIR /app

# install Tensorflow
RUN pip2 install libs/tensorflow-1.1.0-cp27-none-any.whl
RUN pip uninstall -y mock && pip install mock
RUN cd /app/libs/ && wget http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz

# pip install python deps from requirements.txt
# for caching until requirements.txt changes
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# update Raspberry firmwares
RUN rpi-update

# video libraries (https://raspberrypi.stackexchange.com/questions/34107/libmmal-core-so-missing)
RUN echo /opt/vc/lib > pi_vc_core.conf && chown root.root pi_vc_core.conf && mv pi_vc_core.conf /etc/ld.so.conf && ldconfig

# run robot
CMD ["bash", "start.sh"]

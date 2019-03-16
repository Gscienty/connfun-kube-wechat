FROM centos

MAINTAINER gaoxiaochuan@hotmail.com
LABEL com=connfun

RUN yum install -y \
        zlib-devel \
        openssl-devel \
        necurses-devel \
        bzip2-devel \
        libffi-devel \
        gcc \
        make

RUN curl -o Python-3.7.2.tgz https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
RUN tar zxvf Python-3.7.2.tgz
RUN cd Python-3.7.2 && ./configure && make && make install

ADD ./ /connfunc-kube-wechat

WORKDIR /connfunc-kube-wechat
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000/tcp
CMD python3 src/main.py

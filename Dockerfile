FROM python:3

MAINTAINER gaoxiaochuan@hotmail.com
LABEL com=connfun

ADD ./ /connfunc-kube-wechat

WORKDIR /connfunc-kube-wechat
RUN pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 5000/tcp
CMD python3 src/main.py

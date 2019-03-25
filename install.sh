#!/bin/sh
docker build . -t connfun.com/wechat-pay:latest
kubectl apply -f deployment.yaml

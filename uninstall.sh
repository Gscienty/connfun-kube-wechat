#!/bin/sh
kubectl delete service connfun-wechat-pay-service
kubectl delete deploy connfun-wechat-pay-deploy
docker rmi connfun.com/wechat-pay:latest

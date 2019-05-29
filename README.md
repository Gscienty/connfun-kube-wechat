# wechat 支付Kubernetes微服务

所需用到的环境变量如下：

* APP\_ID 服务商号 (必填)
* MCH\_ID 服务商商户号 (必填)
* SUB\_APP\_ID 子商户公众账号ID (选填，可在http request header 中添加 Sub-Appid，该优先级高于环境变量)
* SUB\_MCH\_ID 子商户号 (选填，可在 http request header 中添加 Sub-Mch-Id, 该优先级高于环境变量)
* WX\_MCH\_KEY 商户秘钥 (选填，可在 http request header 中添加 Wx-Mch-Key，该优先级高于环境变量)
* APP\_SECRET APP密钥
* SUB\_APP\_SECRET SubApp密钥
* API\_CERT 证书
* API\_KEY 证书密钥
* RUN\_ENV 运行状态 分为三个: release/develop/mock
* OAUTH\_REDIRECT\_URI oauth的调用地址, (可在 http request header 中添加 OAuth-Redirect-URI，该优先级高于环境变量)


hostPath 中需要装填 apiclient\_cert.pem 和 apiclient\_key.pem

## 适用环境
本模块主要应用在Kubernetes微服务集群中。

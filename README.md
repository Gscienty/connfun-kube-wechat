# wechat 支付Kubernetes微服务

所需用到的环境变量如下：

* APP_ID 服务商号 (必填)
* MCH_ID 服务商商户号 (必填)
* SUB_APP_ID 子商户公众账号ID (选填，可在http request header 中添加 Sub-Appid，该优先级高于环境变量)
* SUB_MCH_ID 子商户号 (选填，可在 http request header 中添加 Sub-Mch-Id, 该优先级高于环境变量)
* SUB_KEY 商户秘钥 (选填，可在 http request header 中添加 Sub-Key，该优先级高于环境变量)
* API_CERT 证书
* API_KEY 证书密钥
* RUN_ENV 运行状态 分为三个: release/develop/mock
* OAUTH_REDIRECT_URI oauth的调用地址, (可在 http request header 中添加 OAuth-Redirect-URI，该优先级高于环境变量)

## 适用环境
本模块主要应用在Kubernetes微服务集群中。

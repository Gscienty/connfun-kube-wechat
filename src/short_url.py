import app, app_inspect

@app.app.route('/native/short-url')
@app_inspect.fields({ 'long_url' })
def native_short_url():
    return app.process('https://api.mch.weixin.qq.com/tools/shorturl')


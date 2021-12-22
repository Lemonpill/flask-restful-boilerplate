from core import create_app

conf = "config.DevelopmentConfig"
app = create_app(conf)

if __name__=="__main__":
    app.run(host="127.0.0.1")

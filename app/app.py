from flask import Flask
import socket,os

app = Flask(__name__)

@app.route("/")
def index_page():
    hostname = socket.gethostname()

    env = os.environ
    env_str =  str([ "{}: {} </br>".format(i,env[i]) for i in env ])

    re = "主机名: {}</br> \
应用版本：v2 <br>\
环境变量: <br>{}".format(hostname,env_str)

    return re

if __name__ == '__main__':

    app.debug = False
    app.run(host='0.0.0.0',port=80)

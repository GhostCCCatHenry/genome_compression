from flask import Flask, render_template, request, redirect, sessions, session, make_response

from util.user import USER_INFO

app = Flask(__name__)  # 实例化对象


@app.route('/cluster')
def cl():
    return render_template('cluster.html')


@app.route('/docker')
def do():
    return render_template('docker.html')


@app.route('/standalone')
def sa():
    return render_template('standalone.html')


@app.route('/action')
def dashboard():
    return render_template('action.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/hdfs')
def hdfs():
    headers = {
        'location': 'http://10.166.38.112:50070'
    }
    response = make_response('hdfs', 301)
    response.headers = headers
    return response


@app.route('/hdfslist')
def hl():
    headers = {
        'location': 'http://10.166.38.112:50070/explorer.html#/'
    }
    response = make_response('hdfs', 301)
    response.headers = headers
    return response


@app.route('/yarn')
def yarn():
    headers = {
        'location': 'http://10.166.38.112:8088'
    }
    response = make_response('yarn', 301)
    response.headers = headers
    return response


@app.route('/fastq')
def jump_q():
    headers = {
        'location': 'https://www.internationalgenome.org/category/fastq/'
    }
    response = make_response('fastq', 301)
    response.headers = headers
    return response


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        render_template('login.html')
    usr = request.form.get("user")
    password = request.form.get("pwd")
    # print(USER_INFO.values())
    if {'id': usr, 'pwd': password} in USER_INFO.values():
        return redirect('/index')
    else:
        return render_template('login.html', msg='用户名或密码错误！')


if __name__ == '__main__':
    # app.config.from_object('config/config.py')
    # app.config('DEBUG')
    app.run(debug='True', host='10.20.66.90', port='4000')

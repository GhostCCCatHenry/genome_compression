# 首先，先向大家介绍一下什么是 werkzeug，Werkzeug是一个WSGI工具包，
# 他可以作为一个Web框架的底层库。这里稍微说一下， werkzeug 不是一个web服务器，也不是一个web框架，而是一个工具包，
# 官方的介绍说是一个 WSGI 工具包，它可以作为一个 Web 框架的底层库，因
# 为它封装好了很多 Web 框架的东西，例如 Request，Response 等等。
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple


@Request.application
def hello(request):
    return Response("hello world")


# __name__是系统变量
if __name__ == "__main__":
    run_simple('localhost', 4000, hello)  # flask app.run底层就调用的这个方法！

# -*- coding: utf-8 -*-

from application import app
from common.libs.Helper import ops_render

@app.errorhandler(404) #捕获应用的异常
def error_404(e):
    return ops_render( "error/error.html",{ "status":404,"msg":"很抱歉！,您访问的页面不存在 ~~" } )

@app.errorhandler(500) #捕获应用的异常
def error_500(e):
    return ops_render("error/error.html",{ "status":500,"msg":"服务器错误" })

@app.errorhandler(502) #捕获应用的异常
def error_502(e):
    return ops_render("error/error.html")



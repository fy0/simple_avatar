# coding:utf-8

import tornado.ioloop
import tornado.web
from simple_avatar import get_avatar_html


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("""
        <!doctype html>
        <html style="width: 960px;margin-left: auto;margin-right: auto;margin-top: 50px;">
        <head>
            <style>
                .sa-avatar {
                    color: white;
                    text-align: center;
                    display: inline-block;
                    -ms-user-select:none;
                    -moz-user-select:none;
                    -webkit-user-select: none;
                    font-family: "Helvetica Neue",Arial,"Hiragino Sans GB","Hiragino Sans GB W3","Microsoft YaHei","Wenquanyi Micro Hei",sans-serif;
                }
            </style>        
        </head>
        <body>
            <div sty>
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
                <br><br>
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
                <a href="javascript:void(0);">%s</a> 
            </div>
        </body>
        </html>
        """ % (get_avatar_html('s', 48),get_avatar_html('i', 32),get_avatar_html('m', 32),get_avatar_html('p', 32),get_avatar_html('l', 32), get_avatar_html('e', 32),
        get_avatar_html('中', 56), get_avatar_html('文', 56), get_avatar_html('测中文测试', 56), get_avatar_html('试中文测试', 56)
        ))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

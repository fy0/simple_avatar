# coding:utf-8

import sys
import tornado.ioloop
import tornado.web
from simple_avatar import get_avatar_html

py_ver = sys.version_info.major

if py_ver == 3:
    unichr = chr

tmpl = """
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
        
        .avatar-box {
            border-radius: 3px;
            margin: 5px;
        }
        
        body {
            font-family: "Helvetica Neue",Arial,"Hiragino Sans GB","Hiragino Sans GB W3","Microsoft YaHei","Wenquanyi Micro Hei",sans-serif;
        }

        a {
            color: #337ab7;
            text-decoration: none;
        }

        a:hover {
            color: #286090;
        }
    </style>        
</head>
<body>
    <p style="text-align:center;">
        <a href='/demo1'>Demo 1</a> |
        <a href='/demo2'>Demo 2</a>
    </p>
    <div>
        %s
    </div>
</body>
</html>
"""


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.redirect('/demo1')


class DemoHandler1(tornado.web.RequestHandler):
    def get(self):
        self.write(tmpl % """
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
        """ % (get_avatar_html('s', 48),get_avatar_html('i', 32),get_avatar_html('m', 32),get_avatar_html('p', 32),get_avatar_html('l', 32), get_avatar_html('e', 32),
        get_avatar_html('中', 56), get_avatar_html('文', 56), get_avatar_html('测中文测试', 56), get_avatar_html('试中文测试', 56)
        ))


class DemoHandler2(tornado.web.RequestHandler):
    def get(self):
        lst = []
        for i in range(1, 51):
            lst.append(get_avatar_html(str(i), 48, ecls=['avatar-box']))
        for i in range(ord(u'一'), ord(u'一') + 50):
            lst.append(get_avatar_html(unichr(i), 48, ecls=['avatar-box']))
        text = ' '.join(lst)

        self.write(tmpl % text)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/demo1", DemoHandler1),
        (r"/demo2", DemoHandler2),
    ], debug=True)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

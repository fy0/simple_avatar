# coding: utf-8

"""
CSS:
.sa-avatar {
    color: white;
    text-align: center;
    -ms-user-select:none;
    -moz-user-select:none;
    -webkit-user-select: none;
    font-family: "Helvetica Neue",Arial,"Hiragino Sans GB","Hiragino Sans GB W3","Microsoft YaHei","Wenquanyi Micro Hei",sans-serif;
}
"""

import sys
import hashlib

py_ver = sys.version_info.major


def get_background_color(txt):
    if py_ver == 3:
        return '#%s' % hashlib.md5(bytes(txt, 'utf-8')).hexdigest()[:6]
    else:
        return '#%s' % hashlib.md5(txt).hexdigest()[:6] # fix for py2


def avatar_generate(txt, color, size, css_class='sa-avatar'):
    params = {
        'min-width': '%spx' % size,
        'min-height': '%spx' % size,
        'line-height': '%spx' % size,
        'font-size': '%spx' % (size-10),
        'background-color': color,
    }
    
    if py_ver == 3:
        char = txt[0]
    else:
        if type(txt) == str:
            char = txt.decode('utf-8')[0]
        else:
            char = txt[0]

    return u"""<div class="%s" style="%s">%s</div>"""\
           % (css_class, ';'.join('%s:%s' % x for x in params.items()), char.upper())


def get_avatar_html(txt, size, css_class='sa-avatar'):
    return avatar_generate(txt, get_background_color(txt), size, css_class)

    
if __name__ == '__main__':
    print(get_avatar_html('Test', 16))
    print(get_avatar_html('测试', 32))

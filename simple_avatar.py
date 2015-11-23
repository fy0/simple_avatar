# coding: utf-8

"""
CSS:
.sa-avatar {
    color: white;
    text-align: center;
    display: inline-block;
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
        # fix for py2
        if type(txt) == unicode:
            return '#%s' % hashlib.md5(txt.encode('utf-8')).hexdigest()[:6]
        else:
            return '#%s' % hashlib.md5(txt).hexdigest()[:6]


def avatar_generate(txt, color, size, css_class='sa-avatar', ecls=None):
    """
    :param txt: text for generate
    :param color: css color, like #abc
    :param size: integer, box size
    :param css_class: str, default css_class
    :param ecls: list, extra css classes
    :return: html of avatar
    """

    params = {
        'width': '%spx' % size,
        'height': '%spx' % size,
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

    if ecls:
        css_classes = '%s %s' % (css_class, ' '.join(ecls))
    else:
        css_classes = css_class

    return u"""<div class="%s" style="%s">%s</div>"""\
           % (css_classes, ';'.join('%s:%s' % x for x in params.items()), char.upper())


def get_avatar_html(txt, size, css_class='sa-avatar', ecls=None, color_func=get_background_color):
    return avatar_generate(txt, color_func(txt), size, css_class, ecls)


if __name__ == '__main__':
    print(get_avatar_html('Test', 32))
    print(get_avatar_html('测试', 64))
    print(get_avatar_html('测试', 64, ecls=['test']))

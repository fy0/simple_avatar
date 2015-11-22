# Simple Avatar

Use first character to generate avatar.

Tested on py2.7/py3.4

```python
import simple_avatar

>>>> print(simple_avatar.get_background_color('Test'))
#0cbc66

>>>> print(simple_avatar.avatar_generate('Test', '#0cbc66', 32))
<div class="sa-avatar" style="font-size:22px;background-color:#0cbc66;min-height:32px;min-width:32px;line-height:32px">T</div>

>>>> print(simple_avatar.get_avatar_html('测试', 32))
<div class="sa-avatar" style="font-size:22px;background-color:#db06c7;min-height:32px;min-width:32px;line-height:32px">测</div>

```

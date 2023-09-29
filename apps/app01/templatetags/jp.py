"""
    这是自定义的模版函数
"""

from django import template

register = template.Library()


@register.filter
def myfunc(value):
    # 自定义的这个函数需要去使用它的HTML里引入  {% load jp %}
    return value.upper()


@register.filter
def con(value):
    # 把参数传进python函数里进行处理，会简单很多
    if int(value) >= 18:
        return True
    else:
        return False


@register.simple_tag()
def mytag1():
    # 这是参数无限制的，多返回文本
    return "HAHAHA"


@register.simple_tag()
def mytag2(a1, a2):
    return a1 + "HAHAHA" + a2


@register.inclusion_tag("app01/xxxx.html")
def xx():
    # 这个函数执行后是将字典里的值给上面指定的网页里
    # 注：返回字典形式
    return {"name": "jack", "age": 20}


@register.inclusion_tag("app01/menu.html")
def menu(role):
    if role == 'user':
        return {
            "data": [
                {"title": "管理权限", "url": "xxx/xxx/xx"},
                {"title": "添加权限", "url": "xxx/xxx/xx"}]
        }
    elif role == 'admin':
        return {
            "data": {"title": "增删", "url": "xx/x/x"},
        }

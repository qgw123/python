__author__ = '秋轩'

from django import template
from django import forms
from django.forms import widgets
from django.forms import fields

class FM(forms.Form):
    user  = fields.CharField(
        error_messages={'required': '用户名不能为空'},
        widget=widgets.Textarea(attrs={'class':'c1'}),
        label='用户名'
    )
    pwd = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'request':'密码不能为空。', 'min_length':'密码长度不能小于6',
                        "max_length": '密码长度不能大于12'}
    )
    email = fields.EmailField(error_messages={'required': '邮箱不能为空.','invalid':"邮箱格式错误"})

    f = fields.FileField()


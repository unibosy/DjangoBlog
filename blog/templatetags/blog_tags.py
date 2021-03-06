#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.org/
@software: PyCharm
@file: blog_tags.py
@time: 2016/11/2 下午11:10
"""

from django import template
from django.conf import settings
import markdown
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def timeformat(data):
    try:
        return data.strftime(settings.TIME_FORMAT)
        # print(data.strftime(settings.TIME_FORMAT))
        # return "ddd"
    except:
        return ""


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(content):
    return mark_safe(markdown.markdown(content,
                                       extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
                                       safe_mode=True, enable_attributes=False))


@register.inclusion_tag('categorytree.html')
def parseCategoryName(article):
    names = article.getCategoryNameTree()

    names.append((settings.SITE_NAME, 'http://127.0.0.1:8000'))
    names = names[::-1]
    print(names)
    return {'names': names}


"""
@register.tag
def parseCategoryName(parser,token):
    tag_name, category = token.split_contents()
    print(category)
    print(tag_name)
    return CategoryNametag(category)

class CategoryNametag(template.Node):
    def __init__(self,category):
        self.category=category
        self.names=[]


    def parseCategory(self,category):
        self.names.append(category.name)
        if category.parent_category:
            self.parseCategory(category.parent_category)


    def render(self, context):
        self.parseCategory(self.category)
        print(self.names)
        return " > ".join(self.names)

        #if self.category.parent_category:
"""

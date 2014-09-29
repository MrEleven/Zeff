setuptools是一个方便的python文件包管理工具(安装工具)。
我平时就用到一个函数，一半要安装东西就这么写。
<pre>
#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    pass

setup(
    name = 'trans',
    version = '0.1',
    keywords = ('leo, trans'),
    description = 'The trans system of Leo',
    author = 'master yumi',
    packages = [ '.', 'trans'], 
    )
</pre>

name就是要按装的软件的名字
version表示版本
keywords目前我还不知道是干嘛用的
description这个我不用解释，大家都知道的
author 看字面意思也知道就是作者的意思
packages表示包可以加'.'表示当前包。

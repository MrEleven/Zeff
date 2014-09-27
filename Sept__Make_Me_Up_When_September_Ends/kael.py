# /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Date  : 2014-03-13
# Author: Eleven
# Email : <iGod_eleven@163.com>

import inspect

# kael是dota中召唤师(血魔法师)的名字。
# 这个修饰器用来进行参数检查和参数转换。
def kael(func):
    arg_info = inspect.getargspec(func)
    func_args = arg_info.args
    atypes = [info.get("atype") for info in arg_info.defaults]
    adefs = [info.get("adef") for info in arg_info.defaults]
    def __pauline(*args, **kwargs):
        eurika_map = { func_args[i]: arg for i, arg in enumerate(args) }
        kwargs.update(eurika_map)
        eurika_map = { arg: atypes[i](kwargs[arg]) if kwargs.get(arg) != None else adefs[i] for i, arg in enumerate(func_args) }
        return func(**eurika_map)
    return __pauline

@kael
def say(a={"adef": 1, "atype": int}, b={"adef": 'x', 'atype': str}, c={'adef': 'ok', 'atype': str}):
    print 'a =', repr(a), 'b =', repr(b), 'c =', repr(c)
        
if __name__ == '__main__':
    say("1", c=1)
    say(a="110", b="w", c={"name": "eleven"})
    say("1", 123, ["ok", "fuck"])



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

def caesar(func):
    arg_info = inspect.getargspec(func)
    func_args = list(arg_info.args)
    has_self = "self" in func_args
    if has_self:
        func_args.pop(0)
    defaults = arg_info.defaults
    default_args = { func_args[i-len(defaults)]: v for i, v in enumerate(defaults) }
    def __monkey(*args, **kwargs):
        args = list(args)
        if has_self:
            self = args.pop(0)
        monkey_map = { func_args[i]: arg for i, arg in enumerate(args) }
        kwargs.update(monkey_map)
        monkey_map = {}
        monkey_map.update(default_args)
        monkey_map.update(kwargs)
        print "*[*caesar args*]*  ", monkey_map, "  *[*/caesar args*]*"
        if has_self:
            result = func(self, **monkey_map)
        else:
            result = func(**monkey_map)
        print "*[*caesar return*]*  ", result, "  *[*/caesar return*]*"
        return result
    return __monkey


        
if __name__ == '__main__':
    say("1", c=1)
    say(a="110", b="w", c={"name": "eleven"})
    say("1", 123, ["ok", "fuck"])

# add this comment for test github email config setting



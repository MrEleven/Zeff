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


WRAP_FUNCTION = """
def %s(%s):
    return monkey(%s)
wrap_function = %s
"""


def caesar(func):
    """
        记录参数和返回值的家伙
    """
    arg_info = inspect.getargspec(func)
    func_args = list(arg_info.args) if arg_info.args else []
    has_self = "self" in func_args
    if has_self:
        func_args.pop(0)
    defaults = arg_info.defaults or []
    keywords = arg_info.keywords
    default_args_values = { func_args[i-len(defaults)]: v for i, v in enumerate(defaults) } if defaults else {}
    def _monkey(*args, **kwargs):
        args = list(args) if args else []
        if has_self:
            self = args.pop(0)
        monkey_map = { func_args[i]: arg for i, arg in enumerate(args) }
        kwargs.update(monkey_map)
        monkey_map = {}
        monkey_map.update(default_args_values)
        monkey_map.update(kwargs)
        logging.info(''.join(["\033[1;32m*[*caesar args*]*\033[0m  ", str(monkey_map), "  \033[1;32m*[*/caesar args*]*\033[0m"]))
        if has_self:
            result = func(self, **monkey_map)
        else:
            result = func(**monkey_map)
        logging.info(''.join(["\033[1;32m*[*caesar return*]*\033[0m  ", str(result), "  \033[1;32m*[*/caesar return*]*\033[0m"]))
        return result

    default_args = []
    normal_args = []
    for k in func_args:
        if k in default_args_values:
            default_args.append(k)
        else:
            normal_args.append(k)
    
    default_args_str = ['='.join([k,"'", str(default_args_values[k]), "'"]) if isinstance(default_args_values[k], basestring) else '='.join([k, str(default_args_values[k])]) for k in default_args]
    call_args_str = ['%s=%s' % (k, k) for k in func_args ]
    arg_items = []
    arg_items.extend(normal_args)
    arg_items.extend(default_args_str)
    if keywords:
        arg_items.append("**" + keywords)
        call_args_str.append("**" + keywords)
    if has_self:
        arg_items.insert(0, 'self')
        call_args_str.insert(0, 'self')
        
    params_str = ', '.join(arg_items)
    call_args_str = ', '.join(call_args_str)

    local_vars = {"wrap_function": None}
    global_vars = {"functools": functools, "monkey": _monkey}

    code = WRAP_FUNCTION % (func.__name__, params_str, call_args_str, func.__name__)
    print code
    exec code in global_vars, local_vars
    return local_vars["wrap_function"]



if __name__ == '__main__':
    say("1", c=1)
    say(a="110", b="w", c={"name": "eleven"})
    say("1", 123, ["ok", "fuck"])

# add this comment for test github email config setting



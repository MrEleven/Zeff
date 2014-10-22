今天本来打算早点回家看Python的。结果因为一个修饰器的问题搞到九点多才回来，到家已经十点多了。

def kael(func):
    arg_info = inspect.getargspec(func)
    func_args = arg_info.args
    has_self = "self" in func_args
    if has_self:
        func_args.pop(0)
    if arg_info.defaults:
        atypes = [info.get("atype") for info in arg_info.defaults]
        adefs = [info.get("adef") for info in arg_info.defaults]
        aneeds = [func_args[i] for i, info in enumerate(arg_info.defaults) if info.get("aneed", False)]
    else:
        atypes, adefs, aneeds = [], [], []
    def __pauline(*args, **kwargs):
        args = list(args) if args else []
        if has_self:
            self = args.pop(0)
        eurika_map = { func_args[i]: arg for i, arg in enumerate(args) }
        kwargs.update(eurika_map)
        if set(aneeds) - set(kwargs.keys()):
            raise Exception("Missing args.")
        eurika_map = { arg: atypes[i](kwargs[arg]) if kwargs.get(arg) != None else adefs[i] for i, arg in enumerate(func_args) }
        kwargs.update(eurika_map)
        if has_self:
            return func(self, **kwargs)
        else:
            return func(**kwargs)
    return __pauline

这个修饰器是没有任何问题的，唯一有缺陷的地方就是呗修饰的函数的__doc__和参数信息不见了。这也难怪，毕竟修饰器新创建了一个函数。

__doc__信息比较好处理，直接能从函数属性中获取，但是参数就不一样了，参数和函数执行的代码是紧密相连的，要分开没这么容易。

我找到一个functool中的一个好像叫wrapper的一个修饰器，这个家伙也是挂羊头卖狗肉，直视吧__doc__和__funcname__换了一下。

不过看Python的实现，这个问题没这么好解决，但愿pypy能解决这个遗留的问题，期待。


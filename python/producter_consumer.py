"""
    对coroutine这一块还不是很清楚。今天回家以后好好看看这个。据说Go和Erlang都是靠这个实现并发的。等学会了这个再去看看nodejs的callback模型
    The only difference is that a generator function cannot control where should the execution continue after it yields; the control is always transferred to the generator’s caller. 
    无法决定挂起之后的生成器的执行控制权限应该分配给谁是python生成器方式coroutine的硬伤啊。不过生成器跟coroutine本身就是两个概念
"""

queue = []

def produce():
    while True:
        while len(queue) <= 10:
            queue.append(0)
            print queue
        consumer = consume()
        consumer.next()
        yield queue

def consume():
    while True:
        while len(queue) > 0:
            queue.pop(0)
            print queue
        yield queue


if __name__ == '__main__':
    produce_gener =  produce()
    for i in xrange(0, 10):
        produce_gener.next()

        
        

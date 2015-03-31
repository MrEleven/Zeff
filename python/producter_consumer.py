"""
    对coroutine这一块还不是很清楚。今天回家以后好好看看这个。据说Go和Erlang都是靠这个实现并发的。等学会了这个再去看看nodejs的callback模型
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

        
        

def read(text, next_coroutine):
    for line in text.split():
        next_coroutine.send(line)
    next_coroutine.close()

def match_filter(pattern, next_coroutine):
    print "Looking for " + pattern
    try:
        while True:
            s = (yield)
            if pattern in s:
                next_coroutine.send(s)
    except GeneratorExit:
        next_coroutine.close()

def print_consumer():
    print "Preparing to print"
    try:
        while True:
            line = (yield)
            print line
    except GeneratorExit:
        print "=== Done ==="

if __name__ == "__main__":
    printer = print_consumer()
    printer.next()
    text = "Commending spending is offending to people pending lending!"
    matcher = match_filter("pend", printer)
    matcher.next()
    read(text, matcher)
    

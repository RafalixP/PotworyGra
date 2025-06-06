

def gen_range(stop, start=1, step=1):
    stop = 5
    num = start
    while num <= stop:
        yield num
        print(num)
        num += step    
ord
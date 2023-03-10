import queue_exsampl

def hotPotato(namelist, num):
    simqueue = queue.Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == '__main__':
    print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
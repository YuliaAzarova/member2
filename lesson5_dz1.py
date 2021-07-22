a = int(input()) # первая остановка первого автобуса
b = int(input()) # последняя остановка первогоавтобуса
c = int(input()) # первая остановка второго автобуса
d = int(input()) # последняя остановка второго автобуса

if a > b:
    bus1start = b
    bus1stop = a
else:
    bus1start = a
    bus1stop = b

if c > d:
    bus2start = d
    bus2stop = c
else:
    bus2start = c
    bus2stop = d

if bus1stop < bus2start:
    print(0)
elif bus2stop < bus1start:
    print(0)
else:
    if bus2start > bus1start and bus1stop > bus2stop:
        print(bus2stop - bus2start + 1)
    elif bus1start > bus2start and bus2stop > bus1stop:
        print(bus1stop - bus1start + 1)
    else:
        if bus2start < bus1stop and bus2stop > bus1stop:
            print(bus1stop - bus2start + 1)
        elif bus2stop > bus1start and bus2stop < bus1stop:
            print(bus2stop - bus1start + 1)
        else:
            if bus1start == bus2start and bus1stop < bus2stop:
                print(bus1stop - bus1start + 1)
            elif bus1start == bus2start and bus2stop < bus1stop:
                print(bus2stop - bus2start + 1)
            elif bus1stop == bus2stop and bus2start < bus1start:
                print(bus1stop - bus1start + 1)
            elif bus1stop == bus2stop and bus1start < bus2start:
                print(bus2stop - bus2start + 1)
            else:
                if bus1stop == bus2start:
                    print(1)
                elif bus2stop == bus1start:
                    print(1)
                else:
                    print(bus2stop - bus1start + 1)
def arr():
    #x,y,z,n = [input() for i in range(4)]
    l = []
    m = []
    for a in range(x+1):
        for b in range(y+1):
            for c in range(z+1):
                if a+b+c != n:
                    l = [a,b,c]
                    m.append(l)
    print(m)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr()

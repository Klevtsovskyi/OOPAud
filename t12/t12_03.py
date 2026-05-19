def P(a):
    P0=1
    P1=1
    P2=1
    n=0
    while P1<a:
        P3=P1+P0
        P0=P1
        P1=P2
        P2=P3
        n+=1
    return n


if __name__ == '__main__':
    print(P(1000))

#! /usr/bin/env python3

def integrar(f,a,b,n):
    h = (b-a) / n
    m = [a + i * h for i in range(n+1)]
    acum = 0
    for i in m:
        acum += h * f(i)    


    return acum





if __name__ == "__main__":
    func = lambda x : x**2

    print(integrar(func,0,1,1000))
    
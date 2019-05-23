def balancebracket(oepnB,closeB,n,s=[]):

    #base case
    if closeB==n:
        print(''.join(s))
        return

    else:

        if oepnB>closeB:
            s.append(')')
            balancebracket(oepnB,closeB+1,n,s)
            s.pop()

        if oepnB<n:
            s.append('(')
            balancebracket(oepnB+1,closeB,n,s)
            s.pop()

n=3
balancebracket(0,0,n)


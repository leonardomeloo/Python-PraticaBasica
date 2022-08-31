def fat(n, show= False ):
    f = 1
    for i in range(n,0,-1):
        if show == True:
            if i > 1:
                print(f'{i} x ', end='')
            else:
                print(f'{i} = ', end='')
        f *= i

    return f
print(fat(10,True))
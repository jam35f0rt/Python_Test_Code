def friendlyNumber(a,b):
    c,d=0,0
    for number in range(1,a+1):
        if a%number==0:
            c+= number

    for number in range(1,b+1):
        if b%number==0:
            d+= number

    return 'They are friendly' if c/a == d/b else 'They are not friendly'
    

friendlyNumber(30,2480)

#2480, 6200 et 40640

def tower(n,start,end,middle):
    if n == 1:
        print('move disk %i from tower %s to tower %s' %(n,start,end))
    else:
        tower(n-1,start,middle,end)
        print('move disk %i from tower %s to tower %s' %(n,start,end))
        tower(n-1,middle,end,start)
        
print(tower(4,'A','C','B'))

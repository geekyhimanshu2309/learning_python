def even_generator(limit):
    li=[]
    for i in range(2,limit+1,2):
        li.append(i)
        print(i)
    return li

print(even_generator(10))
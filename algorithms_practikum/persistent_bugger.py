def persistence(num):
    counter=0
    while num>9:
        counter+=1
        num_str=str(num)
        total=1
        for i in num_str:
            total=total* int(i)
        num=total
    return(counter)

print(persistence(999))
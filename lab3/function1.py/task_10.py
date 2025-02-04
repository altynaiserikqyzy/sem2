def uniqus(list_of_nums):
    uniqs=[]
    for i in range(len(list_of_nums)):
        isuniq=True
        for j in range(len(list_of_nums)):
            if i!=j and list_of_nums[i]==list_of_nums[j]:
                isuniq=False
                break
        if isuniq:
            uniqs.append(list_of_nums[i])
            return uniqs
print(uniqus(b))

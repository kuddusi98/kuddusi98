# 1 1 2 3 5 8 13 21 34
limit = int(input("how many finbonacci number do you want?"))
list1=[0,1]
def fibonacci(arglimit):
    for i in range(2,arglimit):
        number1=list1[i-1] + list1[i-2]
        list1.append(number1)
    return list1
print(fibonacci(limit))

a = [1,3,5,7]
b = [2,4,6,8]
res = a + b
for i in range(len(res)-2):
    for j in range(len(res)-1):
        if res[j] > res[j+1]:
            res[j], res[j+1] = res[j+1], res[j]
print(res)
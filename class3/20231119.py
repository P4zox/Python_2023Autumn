weight=[]
sum=0
for i in range(3):
    weight.append(int(input("The {} student is ".format(i+1))))
    sum+=weight[i]
print(sum)

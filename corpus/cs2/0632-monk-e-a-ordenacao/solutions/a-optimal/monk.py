import time

vetor = []
n = input()
n = int(n)
chaves = input()
chaves = chaves.split()
for i in range(n):
    vetor.append(int(chaves[i]))

hd = [[] for _ in range(200000)]
i = 1
count = 0    
while True:
    for j in range(len(vetor)):
        
        if vetor[j] < 0: 
            x = vetor[j]*-1
            x = x%10**(5*i)
            x = x*-1
        else:
            x = vetor[j]
            x = x%10**(5*i)
        if int(x/10**(5*(i-1))) == 0 : count+=1
        hd[int(x/10**(5*(i-1))+100000)].append(vetor[j])

    if count == len(vetor) : break

    vetor = []

    for k in range(len(hd)):
        if len(hd[k])>=1:
            for l in hd[k]:
                vetor.append(l)
        hd[k] = []
    print(vetor.__str__().replace("[", "").replace("]", "").replace(",", ""))
    i+=1
    count = 0

start = int(input())
num = start
tens = 1
numA = 0
while num != 0:
    if num%10 == 4:
        numA += 3*tens
    tens*=10
    num = num // 10
B = start-numA
result = "Case #x: " + str(numA) + " " + str(B)
print(result)
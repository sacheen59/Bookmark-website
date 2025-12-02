# data = [1,2,3,[4,5],[6,7,8],10]

# output = []

# for i in data:
#     if isinstance(i,list):
#         for j in i:
#             output.append(j)
#     else:
#         output.append(i)

# print(output)

numbers = [1,2,3,4,5,6,20,40]

for i in range(0, len(numbers)):
    if numbers[i] > numbers[i+ 1]:
        temp = numbers[i]

print(temp)
a = [1, 2, 1, 3, 2, 4, 5]
result = []
for i in a:
    if i not in result:
        result.append(i)

print(result)

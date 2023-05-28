i = 1

while i <= 10:
    if i == 5:
        print("Stopping loop execution.")
        break
    print(i)
    i += 1
print("-------------------")
i = 1
while i <= 10:
    if i > 5 and i < 8:
        i += 1
        continue
    print(i)
    i += 1

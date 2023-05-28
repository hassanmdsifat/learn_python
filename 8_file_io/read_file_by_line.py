file = open('test_file.txt', 'r')

# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)

all_lines = file.readlines()

print(all_lines)
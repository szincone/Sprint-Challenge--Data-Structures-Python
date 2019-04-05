import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


# # og sprint code
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates1.append(name_1)

duplicates = []
names_1_no_dups = list(set(names_1))
names_2_no_dups = list(set(names_2))
names = names_1_no_dups + names_2_no_dups
names.sort()

for x in range(len(names) - 1):
    if names[x] == names[x + 1]:
        duplicates.append(names[x])

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

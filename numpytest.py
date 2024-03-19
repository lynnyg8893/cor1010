import numpy as np

print ('my numpy version: ', np.__version__)

n = np.random.randint(1,20)
randomList = []
for i in range(1_000_000):
    n = np.random.randint(1,20)
    randomList.append(n)
#
randomArray = np.random.randint(1, 6, size=10000000)
print("randomArray: ", randomArray.shape, randomArray.size)

count = 0
for number in randomArray:
    if number == 5:
        count += 1

print("the list contains ", count, "5s.")
print(f"the list contains {count} 5s.")

print("Finished")
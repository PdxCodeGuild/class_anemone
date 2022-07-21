import matplotlib.pyplot as plt

names = []
numbers = []

f = open('test_data.txt', 'r')
for row in f:
    row = row.split(' ')
    names.append(row[0])
    numbers.append(int(row[1]))


plt.bar(names, numbers, color='r', label='data to show')

plt.xlabel('Names', fontsize=10)
plt.ylabel('Numbers', fontsize=10)

plt.title("Test Chart", fontsize=20)
plt.legend()
plt.show()
import matplotlib.pyplot as plt

names = []
marks = []

for i in range(5):
    name = input("What's your name?")
    names.append(name)
    mark = int(input("What's your mark?"))
    marks.append(mark)

plt.bar(names,marks,color="red")
plt.title("MarksOfStudents")
plt.xlabel("Name")
plt.ylabel("Mark")
plt.grid()
plt.show()


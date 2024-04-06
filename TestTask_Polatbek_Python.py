# Task 1
number = int(input())

if number == 7:
    print("Hello")

name = str(input())

if name == "John":
    print("Hello John")

# custom array length
array_length = int(input())

n_array = []

for i in range(array_length):
    num = float(input())
    n_array.append(num)

divisor = 3  # Change this to the desired divisor
for num in n_array:
    if num % divisor == 0:
        print(num)

# Task 2
# Given bracket sequence: [((())()(())]]

# Can this sequence be considered correct? - No, it is not correct If the answer to the previous question is “no”,
# then what needs to be changed in it to make it correct?
# - Either remove single ] at the end and single ( at the
# beginning or add [ to the beginning and ) to the end, but before ]

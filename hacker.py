import os
import random

min = 1
max = pow(2, 30)
t = int(1e3)

input_file = open('main/input.txt', 'w')

input_file.write(str(t) + '\n')
for i in range(t):
    input_file.write(str(random.Random().randint(min, max)) + '\n')

os.system('main/main.py')
os.system('code.py')

input_file = open('main/output.txt', 'r')
output1 = input_file.read()
input_file = open('output1.txt', 'r')
output2 = input_file.read()

if output1 == output2:
    print('Success')
else:
    print('Fail')

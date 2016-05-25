import sys

with open(sys.argv[1], 'r') as file:
    code = file.readlines()

acc = 0

variables = {}
labels = {}
current_line = 0

def load(a):
    global acc, labels
    acc = variables[a]

def store(variable):
    global acc, labels
    variables[variable] = acc

def add(variable):
    global acc, labels
    if variable[0] == '=':
        acc += int(variable[1:])
    else:
        acc += variables[variable]

def sub(variable):
    global acc, labels
    if variable[0] == '=':
        acc -= int(variable[1:])
    else:
        acc -= variables[variable]

def mult(variable):
    global acc, labels
    if variable[0] == '=':
        acc *= int(variable[1:])
    else:
        acc *= variables[variable]

def div(variable):
    global acc, labels
    if variable[0] == '=':
        acc //= int(variable[1:])
    else:
        acc //= variables[variable]

def be(label):
    global acc, labels
    if acc == 0:
        current_line = labels[label] - 1

def bg(label):
    global acc, labels
    if acc > 0:
        current_line = labels[label] - 1

def bl(label):
    global acc, labels
    if acc < 0:
        current_line = labels[label] - 1

def bu(label):
    global acc, labels
    current_line = labels[label] - 1

def end():
    global acc, labels
    current_line = -2

def read(variable):
    global acc, labels
    variables[variable] = int(input())

def assembly_print(variable):
    global acc, labels
    print(variables[variable])

def dc(variable, value):
    global acc, labels
    variables[variable] = int(value)


code = [i.lower() for i in code]

for i, line in enumerate(code):
    parameters = line.split()
    if len(parameters) == 3 and parameters[1] != 'dc':
        labels[parameters[0]] = i

print(labels)

while current_line > -1 and current_line < len(code):
    parameters = code[current_line].split()

    index_add = 0

    if len(parameters) == 3 and parameters[1] == 'dc':
        dc(parameters[0], parameters[2])
        current_line += 1
        continue

    if len(parameters) == 3:
        index_add = 1

    parameters[index_add] = parameters[index_add].replace('print', 'assembly_print')

    eval_string = parameters[index_add] + '("' + parameters[1+index_add] + '")'
    eval(eval_string)

    current_line += 1

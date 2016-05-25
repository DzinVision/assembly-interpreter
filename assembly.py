import sys

with open(sys.argv[1], 'r') as file:
    code = file.readlines()

acc = 0

variables = {}
labels = {}
current_line = 0

def load(a):
    global acc, labels, current_line, variables
    acc = variables[a]

def store(variable):
    global acc, labels, current_line, variables
    variables[variable] = acc

def add(variable):
    global acc, labels, current_line, variables
    if variable[0] == '=':
        acc += int(variable[1:])
    else:
        acc += variables[variable]

def sub(variable):
    global acc, labels, current_line, variables
    if variable[0] == '=':
        acc -= int(variable[1:])
    else:
        acc -= variables[variable]

def mult(variable):
    global acc, labels, current_line, variables
    if variable[0] == '=':
        acc *= int(variable[1:])
    else:
        acc *= variables[variable]

def div(variable):
    global acc, labels, current_line, variables
    if variable[0] == '=':
        acc //= int(variable[1:])
    else:
        acc //= variables[variable]

def be(label):
    global acc, labels, current_line, variables
    if acc == 0:
        current_line = labels[label] - 1

def bg(label):
    global acc, labels, current_line, variables
    if acc > 0:
        current_line = labels[label] - 1

def bl(label):
    global acc, labels, current_line, variables
    if acc < 0:
        current_line = labels[label] - 1

def bu(label):
    global acc, labels, current_line, variables
    current_line = labels[label] - 1

def end(a):
    global acc, labels, current_line, variables
    current_line = -2

def read(variable):
    global acc, labels, current_line, variables
    value = int(input())
    variables[variable] = value
    acc = value

def assembly_print(variable):
    global acc, labels, current_line, variables
    print(variables[variable])

def dc(variable, value):
    global acc, labels, current_line, variables
    variables[variable] = int(value)


code = [i.lower().replace('\n', '') for i in code]

for i, line in enumerate(code):
    parameters = line.split('\t')
    if parameters[0] != '':
        labels[parameters[0]] = i

while current_line > -1 and current_line < len(code):
    parameters = code[current_line].split('\t')

    if parameters[1] == 'dc':
        dc(parameters[0], parameters[2])
        current_line += 1
        continue

    if parameters[1] == 'print':
        assembly_print(parameters[2])
        current_line += 1
        continue

    eval_string = parameters[1] + '("' + parameters[2] + '")'
    eval(eval_string)

    current_line += 1

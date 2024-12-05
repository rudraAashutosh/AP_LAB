
with open("LAB_01\\4\\add1.c", 'r') as file:
    c_program = file.read()


c_program = c_program.replace('+', '*')
with open("add2.c", 'w') as file:
    file.write(c_program)
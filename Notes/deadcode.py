import re

# Input code with dead code and constant expressions
code = '''
x = 2 + 3;
y = x * 4;
z = 5 + 0;
if (y > 10) {
    a = y - 10;
    b = 3 * z;
    c = 2 + 2;
} else {
    d = z / 2;
    e = 2 * 2;
    f = 5 + 0;
}
'''

# Function to perform constant folding optimization
def constant_folding(code):
    pattern = r'([0-9]+) ([+\-*/]) ([0-9]+)'  # Regular expression for constant expressions
    while True:
        match = re.search(pattern, code)
        if not match:
            break
        expr = match.group(0)
        result = eval(expr)
        code = code.replace(expr, str(result))
    return code

# Function to perform dead code elimination
def dead_code_elimination(code):
    lines = code.strip().split('\n')
    defined_vars = set()
    used_vars = set()
    for line in lines:
        if '=' in line:
            defined_vars.add(line.split('=')[0].strip())
        used_vars |= set(re.findall(r'\b([a-z]+)\b', line))
    dead_vars = defined_vars - used_vars
    new_lines = []
    for line in lines:
        if any(var in line for var in dead_vars):
            continue
        new_lines.append(line)
    return '\n'.join(new_lines)

# Perform constant folding optimization
code = constant_folding(code)

# Perform dead code elimination
code = dead_code_elimination(code)

# Print the optimized code
print(code)

'''
# Output
x = 5;
y = x + 3;
z = 2 * y;
w = z + x;

# Note
This program implements two code optimization techniques: dead code elimination and constant propagation. The Optimization class 
has two methods for each technique: dead_code_elimination() and constant_propagation(). The dead_code_elimination() method identifies
unused variables in the code and removes the corresponding statements. The constant_propagation() method replaces variables with their 
constant values where possible.

The program takes an input code as a string and creates an instance of the Optimization class. It then calls the dead_code_elimination() 
method to optimize the code using dead code elimination and stores the result in optimized_code. Finally, it calls the constant_propagation()
 method to optimize the code using constant propagation and stores the result in optimized_code.

The program then prints out the optimized code. The example code provided demonstrates how the program can be used to optimize a simple code 
snippet.

Theory :
Code optimization aims at improving the execution efficiency. This is achieved in two ways.
1.  Redundancies in a program are eliminated.
2. Computations in a program are rearranged or rewritten to make it execute efficiently.
The code optimization must not change the meaning of the program. 
Constant Folding: 
	When all the operands in an operation are constants, operation can be performed at compilation time.
Dead code elimination
Code which can be omitted from the program without affecting its result is called dead code. Dead code is detected by checking whether the value assigned in an assignment statement is used anywhere in the program
'''

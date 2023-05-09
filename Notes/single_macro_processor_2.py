# Code
# Define the macro processor
class MacroProcessor:
    def __init__(self):
        self.MNT = {}
        self.MDT = []
        self.ALA = []
        self.expanded_code = []

    def expand_macros(self, code):
        for line in code:
            tokens = line.split()
            if len(tokens) > 0 and tokens[0].endswith(':'):
                self.expanded_code.append(line)
            elif len(tokens) > 0 and tokens[0] in self.MNT:
                macro_id = self.MNT[tokens[0]]
                macro_definition = self.MDT[macro_id]['definition']
                macro_args = self.MDT[macro_id]['args']
                arg_values = tokens[1:]
                for i, arg in enumerate(arg_values):
                    macro_definition = macro_definition.replace(macro_args[i], arg)
                self.ALA.append(arg_values)
                self.expanded_code.extend(macro_definition.split('\n'))
            else:
                self.expanded_code.append(line)

    def add_macro(self, name, definition, args=[]):
        self.MNT[name] = len(self.MDT)
        self.MDT.append({'name': name, 'definition': definition, 'args': args})

    def display_tables(self):
        print('Macro Name Table (MNT):', self.MNT)
        print('Macro Definition Table (MDT):', self.MDT)

# Example usage
processor = MacroProcessor()

# Define a macro
processor.add_macro('ADD', 'MOV AX, {0}\nADD AX, {1}\nMOV {2}, AX', ['src1', 'src2', 'dest'])

# Define some code with macro calls
code = [
    'START: ADD 5, 10, RESULT',
    'MOV AH, 4CH',
    'INT 21H'
]

# Expand the macros in the code
processor.expand_macros(code)

# Display the expanded code and the MDT/MNT tables
print('Expanded code:')
for line in processor.expanded_code:
    print(line)
processor.display_tables()


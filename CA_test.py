#
# 6/3/19
#
# --------------------------------------------------------------------------------------
"""
Trying a console based ECA implementation.
"""
# --------------------------------------------------------------------------------------

# Imports
import time
from numpy import binary_repr

# Rule selection
rule = 27

# Seeding (puts binary ON at specified indecies)
seed_indicies = 11, 19, 37, 92, 250

# Evolution parameters
generations = 300
delay = 0.05

# Static variables
boundaries = False
width = 250
fill = u"\u25A0"
empty = ' '

# Converting seed to binary width
if isinstance(seed_indicies, int):
    seed_indicies = [seed_indicies - 1]
def seed_convert(indicies, width):
    empty = '0' * width
    seed = list(empty)
    for index in indicies:
        seed[index - 1] = '1'
    return ''.join(seed)
seed = seed_convert(seed_indicies, width)

# Converting rule to binary
rule = binary_repr(rule, 8)
print('Rule: ', rule)
rule_set = {
    '111' : rule[0],
    '110' : rule[1],
    '101' : rule[2],
    '100' : rule[3],
    '011' : rule[4],
    '010' : rule[5],
    '001' : rule[6],
    '000' : rule[7]

}

# Checking boundaries
if boundaries == True:
    bounds = '1'
else:
    bounds = '0'

# Cellular evolution
def evolve(line, rule_set, width, bounds):
    new_line = []
    for i in range(len(line)):
        if i == 0:
            state = bounds + line[i] + line[i + 1]
        elif i == width - 1:
            state =  line[i - 1] + line[i] + bounds
        else:
            state = line[i - 1] + line[i] + line[i +1]
        new_line.append(rule_set[state])
    return ''.join(new_line)

# Parsing
def parse(line, fill, empty):
    output = []
    for character in line:
        if character == '1':
            output.append(fill)
        else:
            output.append(empty)
    return ''.join(output)

# Rendering
line = seed
output = parse(line, fill, empty)
print(output)
time.sleep(delay)
for generation in range(generations):
    line = evolve(line, rule_set, width, bounds)
    output = parse(line, fill, empty)
    print(output)
    time.sleep(delay)


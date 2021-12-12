import os, os.path
import fnmatch
#Number of .py file in folder quant_interview
list = fnmatch.filter(os.listdir('.'), '*.py')
print(list, len(list))

#Total umber of code lines
count_code_line = 0
for file_name in list:
    file = open(file_name, 'r')
    for line in file:
        if line != '\n':
            line_ = line.strip()
            if not line_.startswith('#'):
                count_code_line += 1

print(count_code_line)

#Total number of comment lines
count_cmt_line = 0
for file_name in list:
    file = open(file_name, 'r')
    for line in file:
            line_ = line.strip()
            if line_.startswith('#'):
                count_cmt_line += 1

print(count_cmt_line)

#Number of definition
count_definition = 0
for file_name in list:
    file = open(file_name, 'r')
    for line in file:
            line_ = line.strip()
            if line_.startswith('def'):
                count_definition += 1

print(count_definition)
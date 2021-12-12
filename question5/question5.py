import os
import subprocess
from os.path import dirname


def count_python_files(dir):
    result = 0
    for _, _, files in os.walk(dir):
        result += len([f for f in files if f[-3:] == '.py'])
    return result


def count_line_in_python_file(py_txt_format):
    count_total = 0
    count_comment = 0
    count_code = 0
    count_function = 0
    for line in py_txt_format:
        if line == '':
            continue
        count_total += 1
        if line.startswith('#'):
            count_comment += 1
        else:
            count_code += 1
        if line.startswith('def'):
            count_function += 1
    return count_total, count_comment, count_code, count_function


def count_lines(dir):
    n_total = 0
    n_codes = 0
    n_comments = 0
    n_functions = 0
    for roots, dirs, files in os.walk(dir):
        for f in files:
            if f.endswith('.py'):
                print(os.path.join(roots, f))
                with open(os.path.join(roots, f), 'r') as f_count:
                    py_lines = f_count.read().split('\n')
                    count_total, count_comment, count_code, count_function = count_line_in_python_file(py_lines)
                    n_total += count_total
                    n_codes += count_code
                    n_comments += count_comment
                    n_functions += count_function
                    print("total: {}\tcodes: {}\t comments: {}\t functions:{}".format(n_total, n_codes, n_comments,
                                                                                      n_functions))
    return n_total, n_codes, n_comments, n_functions





if __name__ == '__main__':
    print(get_size('/home/dungdv/source/Quantitative_Interview'))

import re
f = open('sample-text-file.txt', 'r')
txt = f.read()
text = 'Nguyen Tien Phuc was on 05 Oct 1996, 2'

a = re.findall("(\d\d\d\d)(/)(0\d|1[0-2])(/)(0\d|1\d|2\d|3[0-1])|(0\d|1[0-2])(/)(0\d|1\d|2\d|3[0-1])(/)(\d\d\d\d)|(0\d|1\d|2\d|3[0-1])(/)(0\d|1[0-2])(/)(\d\d\d\d)|(0\d|1\d|2\d|3[0-1])(\s)(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(\s)(\d\d\d\d)", txt)

if len(a) == 0:
    print("There is no appearance of 'date' in this text." )
if len(a) == 1:
    print("There is an appearance of 'date' in this text.")
if len(a)>1:
    print(f"There are {a} appearances of 'date' in this text.")


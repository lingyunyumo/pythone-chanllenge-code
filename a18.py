import Image, difflib, time
from cStringIO import StringIO
from pprint import pprint
l1 = []
l2 = []
with open('delta.txt') as f:
    for line in f:
        l1.append(line[:53])
        l2.append(line[56:-1])
result = list(difflib.ndiff(l1, l2))
def solve(condition):
    s = [chr(int(group, 16))
         for line in result if line.startswith(condition)
         for group in line[len(condition):].split()]
    Image.open(StringIO("".join(s))).show()

for condition in " +-":
    solve(condition)
    time.sleep(1)  # give time to view

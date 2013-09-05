import re
def describe(s):
    return "".join([str(len(m.group(0))) + m.group(1)
                    for m in re.finditer(r"(\d)\1*", s)])
s = "1"
for dummy in range(30):
    s = describe(s)
print len(s)  # prints 5808

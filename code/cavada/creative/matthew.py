import pprint

with open('matthew.txt','rt',encoding='utf8') as f:
    text = f.read()
    lines = (text.split('\n'))
# print(lines)

# for i, line in enumerate(lines):
#     print(lines[i])
    
    
m=lines.pop(0)
matthew = []
for i, line in enumerate(lines):
    dict = {lines[i]:line}
    matthew.append(dict)

print(f"book: {matthew}")
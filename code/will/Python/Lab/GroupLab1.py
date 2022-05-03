jl = [0,0]

years = 0

while len(jl) <1000:
    for j in jl:
        if 4 <= j <=8:
            jl.append(0)
    
    for x in range(len(jl)-1,-1):
        if jl[x] == 10:
          jl.pop(x)
    
    for x in range(len(jl)):
        jl[x] += 1 

    years += 1
    
print(f'It would take {years} years to get {len(jl)} jackalopes')


# This lab is Myers, Wood, and Cicero
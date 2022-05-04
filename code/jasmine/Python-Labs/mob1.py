

# population list

jack = [0,0]

# filter the years of jacks with loop 

years = 0

#produce at 4-8 and die at 10 
#remove from list at age 10 

while len(jack) < 1000:
    # baby making loop
    for x in jack:
        if 4 <= x <= 8:
            jack.append(0)

    # loop to off the jack
    for i in range(len(jack)-1,-1):
        if jack[i] == 10:
            jack.pop(i)
    

    # loop to age the jack
    for i in range(len(jack)):
        jack[i] += 1
    print(len(jack), years)  




    years += 1

print(f'Our population is {len(jack)} after {years} years')


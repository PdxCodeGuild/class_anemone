let distance = parseFloat(prompt('What is the distance?  '))
let unit = prompt('What is the starting unit?  ')
let unit2 = prompt('What unit do you want to convert to?  ')

if (unit == 'ft'){
    result = distance * 0.3048}
else if (unit == 'mi'){
    result = distance * 1609.34}
else if (unit == 'm'){
    result = distance}
else if (unit == 'km'){
    result = distance * 1000}
else if (unit == 'yard'){
    result = distance * 0.9144}
else if (unit == 'inch'){
    result = distance * 0.0254}
    
 
alert(result)

if (unit2 == 'ft'){
    alert(result/0.3048)}
else if (unit2 == 'mi'){
    alert(result/1609.34)}
else if (unit2 == 'm'){
    alert(result)}
else if (unit2 == 'km'){
    alert(result/1000)}
else if (unit2 == 'yard'){
    alert(result/0.9144)}
else if (unit2 == 'inch'){
    alert(result/0.0254)}


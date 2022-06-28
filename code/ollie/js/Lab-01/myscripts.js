let distance = parseInt(prompt("What is the distance (no units): "))
let input = prompt("What are the input units? (ft, m , mi, km, in, yd): ")
let output = prompt("What are the output units? (ft, m , mi, km, in, yd): ")
let result

if (input === 'ft') {
    result = distance * 0.3048
} else if (input === 'm') {
    result = distance * 1
} else if (input === 'mi') {
    result = distance * 1609.34
} else if (input === 'km') {
    result = distance * 1000
} else if (input === 'in') {
    result = distance * 0.0254
} else if (input === 'yd') {
    result = distance * 0.9144
} else {
    alert('This unit converter does not support that unit of measurement.')
}

if (output === 'ft') {
    alert(`${distance} ${input} is ${(result / 0.3048).toFixed(2)} ${output}.`)
} else if (output === 'm') {
    alert(`${distance} ${input} is ${(result / 1).toFixed(2)} ${output}.`)
} else if (output === 'mi') {
    alert(`${distance} ${input} is ${(result / 1609.34).toFixed(2)} ${output}.`)
} else if (output === 'km') {
    alert(`${distance} ${input} is ${(result / 1000).toFixed(2)} ${output}.`)
} else if (output === 'in') {
    alert(`${distance} ${input} is ${(result / 0.0254).toFixed(2)} ${output}.`)
} else if (output === 'yd') {
    alert(`${distance} ${input} is ${(result / 0.9144).toFixed(2)} ${output}.`)
} else {
    alert('This unit converter does not support that unit of measurement.')
}
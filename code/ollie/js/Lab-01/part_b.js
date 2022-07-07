let distance = document.getElementById('distance')
let input = document.getElementById('in_unit')
let output = document.getElementById('out_unit')
let convert = document.getElementById('convert')
let display = document.getElementById('display')
let result
let newDist

convert.addEventListener('click', function() {
    if (input.value === 'ft') {
        result = distance.value * 0.3048
    } else if (input.value === 'm') {
        result = distance.value * 1
    } else if (input.value === 'mi') {
        result = distance.value * 1609.34
    } else if (input.value === 'km') {
        result = distance.value * 1000
    } else if (input.value === 'in') {
        result = distance.value * 0.0254
    } else if (input.value === 'yd') {
        result = distance.value * 0.9144
    } else {
        alert('This unit converter does not support that unit of measurement.')
    }
    
    if (output.value === 'ft') {
        newDist = result / 0.3048
    } else if (output.value === 'm') {
        newDist = result / 1
    } else if (output.value === 'mi') {
        newDist = result / 1609.34
    } else if (output.value === 'km') {
        newDist = result / 1000
    } else if (output.value === 'in') {
        newDist = result / 0.0254
    } else if (output.value === 'yd') {
        newDist = result / 0.9144
    }

    let print = document.createElement('p')
    print.innerText = `${distance.value} ${input.value} is ${newDist.toFixed(1)} ${output.value}.`
    display.prepend(print)
})
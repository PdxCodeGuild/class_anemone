// let distance = parseFloat(prompt('What is the distance?  '))
// let unit = prompt('What is the starting unit?  ')
// let unit2 = prompt('What unit do you want to convert to?  ')




    
    


function convert(distance,unit,unit2){
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
        
    
    // return(result)

    if (unit2 == 'ft'){
        return(result/0.3048)}
    else if (unit2 == 'mi'){
        return(result/1609.34)}
    else if (unit2 == 'm'){
        return(result)}
    else if (unit2 == 'km'){
        return(result/1000)}
    else if (unit2 == 'yard'){
        return(result/0.9144)}
    else if (unit2 == 'inch'){
        return(result/0.0254)}
}

// let number = convert

let btn=document.getElementById('Submit')
btn.addEventListener('click', function(){
    let distance = document.getElementById('input')
    let input = distance.value
    let unit = document.getElementById('unit')
    let unit2 = document.getElementById('unit2')
    let number = convert(parseInt(input),unit.value,unit2.value)
   let conversion = document.getElementById('conversion')
   conversion.innerHTML= number
})

// console.log('hi')


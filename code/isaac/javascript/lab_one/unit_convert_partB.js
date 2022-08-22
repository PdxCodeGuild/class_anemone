// Python lab 1: Unit Converter -- VERSION 1
// Write the Python lab in JavaScript

// Create variables with the given measurements; feet(ft), miles(mi), kilometers(km), meters(m)
// convert to meters

// each unit is based on a 1:1 conversion between meters and the given unit
// of measurement.

let ft = 0.3048
let mi = 1609.34
let km = 1000
let m = 1
let yd = 0.9144
let inc = 0.0254 // inc = inches as in would convert to an (in) statement


// let ask_distance = document.querySelector("What is the distance in feet? ")
// let meter_distance = parseInt(ask_distance) * ft
// alert(`${ask_distance} feet is ${Math.round(meter_distance, 5)} meters`)


let calcBtn = document.getElementById("calculate")

calcBtn.addEventListener('click', function(){
    let user_distance = document.getElementById("distance")  // Version 2
    console.log(user_distance)
    let distance_unit = document.getElementById("units")
    // let numberDistance = user_distance
    
    let distanceValue = distance_unit.value
    let userValue = parseInt(user_distance.value)
    
    let showResult = document.getElementById("output-one")
    console.log(userValue)

    if (distanceValue === 'feet') {
        let total_ft = userValue * ft
        console.log(total_ft)
        showResult.innerText = `${userValue} feet is ${total_ft} meters.`
    } else if (distanceValue === 'miles') {
        let total_mi = userValue * mi
        showResult.innerText = `${userValue} miles is ${total_mi} meters.`
    } else if (distanceValue === 'kilometers') {
        let total_km = userValue * km 
        showResult.innerText = `${userValue} kilometers is ${total_km} meters.`
    } else if (distanceValue === 'meters') {
        let total_m = userValue * m 
        showResult.innerText = `${userValue} meters is ${total_m} meters.`
    } else if (distanceValue === 'inches') {      // -- VERSION 3 - Incorporate inches and yards
        let total_in = userValue * inc 
        showResult.innerText = `${userValue} inches is ${total_in} meters.`
    } else if (distanceValue === 'yards') {
        let total_yd = userValue * yd
        showResult.innerText = `${userValue} yards is ${total_yd} meters.`
    }

})
console.log(calcBtn)


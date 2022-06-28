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

// create the input variables

let ask_distance = prompt("What is the distance in feet? ")
let meter_distance = parseInt(ask_distance) * ft
alert(`${ask_distance} feet is ${Math.round(meter_distance, 5)} meters`)


// --------------------------------------------------------------------------------- //

// -- VERSION 2

// Ask for the distance and set the distance 
// to the corresponding unit of measurement (UOM)

let user_distance = parseInt(prompt("What is the distance? "))
let distance_unit = prompt("What is the Unit Of Measurement? ")

// create conditional if and else if statements
// for each input

if (distance_unit === 'feet') {
    let total_ft = user_distance * ft
    alert(`${user_distance} feet is ${total_ft} meters.`)
}

else if (distance_unit === 'miles') {
    let total_mi = user_distance * mi
    alert(`${user_distance} miles is ${total_mi} meters.`)
}

else if (distance_unit === 'kilometers') {
    let total_km = user_distance * km 
    alert(`${user_distance} kilometers is ${total_km} meters.`)
}

else if (distance_unit === 'meters') {
    let total_m = user_distance * m 
    alert(`${user_distance} meters is ${total_m} meters.`)
}


// --------------------------------------------------------------------- //

// -- VERSION 3

// Incorporate inches and yards

else if (distance_unit === 'inches') {
    let total_in = user_distance * inc 
    alert(`${user_distance} inches is ${total_in} meters.`)
}

else if (distance_unit === 'yards') {
    let total_yd = user_distance * yd
    alert(`${user_distance} yards is ${total_yd} meters.`)
}

// -------------------------------------------------------------------- //

// -- VERSION 4

// conver UOM to meters 

let user_given_distance = parseInt(prompt("Please give a number for the distance: "))
let first_unit = prompt("What is the first unit? ")

let outcome_ft = user_given_distance * ft
let outcome_mi = user_given_distance * mi 
let outcome_km = user_given_distance * km 
let outcome_m = user_given_distance * m 

if (first_unit === 'feet') {
    let outcome_ft = user_given_distance * ft
    alert(`Old distance is ${outcome_ft}`)
}
else if (first_unit === 'miles') {
    let outcome_mi = user_given_distance * mi
    alert(`Old distance is ${outcome_mi}`)
}
else if (first_unit === 'kilometers') {
    let outcome_km = user_given_distance * km
    alert(`Old distance is ${outcome_km}`)
}
else if (first_unit === 'meters') {
    let outcome_m = user_distance * m
    alert(`Old distance is ${outcome_m}`)
}

let second_unit = prompt("Enter second unit? ")
if (second_unit === 'feet') {
    let new_dist_ft = outcome_ft / ft
    alert(`New is distance is ${new_dist_ft}`)
}
else if (second_unit === 'miles') {
    let new_dist_mi = outcome_mi / mi
    alert(`New is distance is ${new_dist_mi}`)
}
else if (second_unit === 'kilometers') {
    let new_dist_km = outcome_km / km
    alert(`New is distance is ${new_dist_km}`) 
}
else if (second_unit === 'meters') {
    let new_dist_m = outcome_m / m
    alert(`New is distance is ${new_dist_m}`) 
}


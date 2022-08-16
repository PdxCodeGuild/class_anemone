let output
let final_output
let ft = 0.3048
let mi = 1609.34
let m = 1
let km = 1000
let yd = 0.9144
let inch = 0.0254




let convertUnit = document.getElementById("convert")
let resultsDiv = document.getElementById('results')



convertUnit.addEventListener("click", function(){


    distance = document.getElementById("distance").value
    input_unit = document.getElementById("input").value
    output_unit = document.getElementById("output").value
    
    distance = Number(distance)

    console.log(distance)
    console.log(input_unit)
    console.log(output_unit)

    if(input_unit === 'ft' || input_unit === 'feet'){
        output = distance * ft
        console.log(distance)
        console.log(output)
    }else if (input_unit === 'mi' || input_unit === 'miles'){
        output = distance * mi
    }else if (input_unit === 'km' || input_unit === 'kilometers'){
        output = distance * km
    }else if (input_unit === 'm' || input_unit === 'meter'){
        output = distance * m
    }else if (input_unit === 'yd' || input_unit === 'yard'){
        output = distance * yd
    }else if (input_unit === 'in' || input_unit === 'inch'){
        output = distance * inch
    }

    if (input_unit === output_unit){
        final_output = distance
    }else if(output_unit === 'ft' || output_unit === 'feet'){
        final_output = output * 3.28084
    }else if(output_unit === 'mi' || output_unit === 'miles'){
        final_output = output / mi
    }else if(output_unit === 'km' || output_unit === 'kilometers'){
        final_output = output / km
    }else if(output_unit === 'yd' || output_unit === 'yard'){
        final_output = output * 1.094
    }else if(output_unit === 'in' || output_unit === 'inch'){
        final_output = output * 39.37
    }
    console.log(output)
    console.log(final_output)

    let resultsP = document.createElement('h4')
    resultsP.innerText = `${distance} ${input_unit} is ${final_output} ${output_unit}`
    resultsDiv.replaceChildren(resultsP)



})


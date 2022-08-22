
let metrics = {
    'feet': .3048,
    'miles': 1609.34,
    'meters': 1,
    'kilometers': 1000,
}



const selctionbutton = document.querySelectorAll('[data-selection]')

function conversion(input, input_sel, output_sel) {
    let answer = (input * metrics[`${input_sel}`]).toFixed(3);
    let convert = (answer / metrics[`${output_sel}`]).toFixed(3);
return convert
}




submitBtn.addEventListener("click", function(){

    let input = document.getElementById('input').value;
    let input_sel = document.getElementById('input_sel').value;
    let output_sel = document.getElementById('output_sel').value;

    result = conversion(input, input_sel, output_sel);
    document.getElementById('output').innerHTML = "Your conversion is: " + `${result} ${output_sel}.`


})








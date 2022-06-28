// Assignment Code
var generateEl = document.querySelector("#generate");




//* Slider control for password length label
document.getElementById("length-slider").oninput = function(){

    let sliderValue = document.getElementById("length-slider").value;

    if(sliderValue > 0){
        document.getElementById("length").innerHTML = "Password Length: " + sliderValue;
    } 
    else{
        document.getElementById("length").innerHTML = "Password Length: 8"
    }
}

//* Write password to the #password input
generateEl.addEventListener("click", function() {

    // set password length/complexity
    let lengthEl = document.getElementById("length-slider").value;
    let upperEl = document.getElementById("upper-check").check;
    let numberEl = document.getElementById("number-check").check;
    let symbolEl = document.getElementById("symbol-check").check;
    let values = "";
    
    //* possible password character values
    
    var check = $('input:checked:checkbox[name=cc]');
    var id = '';
    $(check).each( function(index) {
        id += $(this).attr('id');
    })
    if ($(check).is(':checked')) {
        console.log("in switch")
        console.log(id)
        // switch case for possible characters
        switch (id) {
            case 'upper-check':
                values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz";
                console.log(id);
                break;
            case 'number-check':
                values = "abcdefghijklmnopqrstuvwxyz1234567890";
                console.log(id);
                break;
            case 'symbol-check':
                values = "abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+";
                console.log(id);
                break;
            case 'upper-checknumber-check':
                values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz1234567890";
                console.log(id);
                break;
            case 'upper-checksymbol-check':
                values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+";
                console.log(id);
                break;
            case 'number-checksymbol-check':
                values = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+";
                console.log(id);
                break;
            case 'upper-checknumber-checksymbol-check':
                values = "ABCDEFGHIJKLMNOPQRSTUVWZYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+";
                console.log(id);
                break;
        }
    } else {
        values = "abcdefghijklmnopqrstuvwxyz";
        console.log("nothing checked");
    }

    console.log(values)

    let password = "";

    for (var i = 0; i < lengthEl; i++) {
        password = password + values.charAt(Math.floor(Math.random() * Math.floor(values.length - 1)));
    }
    // Display Password
    document.getElementById("password").value = password;
});
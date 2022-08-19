var input = document.getElementById('input');
var result = document.getElementById('result');
var inputText = document.getElementById('inputText');
var resultText = document.getElementById('resultText');
var inputTextValue,resultTextValue;

input.addEventListener("keyup",myResult);
inputText.addEventListener("change", myResult);
resultText.addEventListener("change", myResult);

inputTextValue = inputText.value;
resultTextValue = resultText.value;





function myResult(){

    inputTextValue = inputText.value;
    resultTextValue = resultText.value; 

    // logic table for meter conversion
    if(inputTextValue === "meter" && resultTextValue === "kilometer"){
        result.value = Number(input.value) * 0.001;
    }else if(inputTextValue === "meter"  && resultTextValue === "yard"){
        result.value = Number(input.value) * 1.09361;
    }else if (inputTextValue === "meter" && resultTextValue === "inch"){
        result.value = Number(input.value) * 39.3701;
    }else if(inputTextValue === "meter"  && resultTextValue === "mile"){
         result.value = Number(input.value) * 0.000621371;
    }else if (inputTextValue === "meter" && resultTextValue === "feet"){
         result.value = Number(input.value) * 3.28084;
    }

    // logic table for kilometer conversion
    if(inputTextValue === "kilometer" && resultTextValue === "kilometer"){
        result.value = Number(input.value) * 1;
    }else if(inputTextValue === "kilometer"  && resultTextValue === "yard"){
        result.value = Number(input.value) * 109.361;
    }else if (inputTextValue === "kilometer" && resultTextValue === "inch"){
        result.value = Number(input.value) * 3937.01;
    }else if(inputTextValue === "kilometer"  && resultTextValue === "mile"){
         result.value = Number(input.value) * 0.0621371;
    }else if (inputTextValue === "kilometer" && resultTextValue === "feet"){
         result.value = Number(input.value) * 328.084;

    }


    // logic table for yard conversion
    if(inputTextValue === "yard" && resultTextValue === "kilometer"){
        result.value = Number(input.value) * 0.0009144;
    }else if(inputTextValue === "yard"  && resultTextValue === "yard"){
        result.value = Number(input.value) * 1;
    }else if (inputTextValue === "yard" && resultTextValue === "inch"){
        result.value = Number(input.value) * 36;
    }else if(inputTextValue === "yard"  && resultTextValue === "mile"){
         result.value = Number(input.value) * 0.00568182;
    }else if (inputTextValue === "yard" && resultTextValue === "feet"){
         result.value = Number(input.value) * 3;

    }
    // logic table for inches
    if(inputTextValue === "inch" && resultTextValue === "kilometer"){
        result.value = Number(input.value) * (1/39370);
    }else if(inputTextValue === "inch"  && resultTextValue === "yard"){
        result.value = Number(input.value) * 0.027778;
    }else if (inputTextValue === "inch" && resultTextValue === "inch"){
        result.value = Number(input.value) * 1;
    }else if(inputTextValue === "inch"  && resultTextValue === "mile"){
         result.value = Number(input.value) * (1/63360);
    }else if (inputTextValue === "inch" && resultTextValue === "feet"){
         result.value = Number(input.value) * 0.0833333;

    }
    // logic table for miles
    if(inputTextValue === "miles" && resultTextValue === "kilometer"){
        result.value = Number(input.value) * 1.60934;
    }else if(inputTextValue === "miles"  && resultTextValue === "yard"){
        result.value = Number(input.value) * 1760;
    }else if (inputTextValue === "miles" && resultTextValue === "inch"){
        result.value = Number(input.value) * 63360;
    }else if(inputTextValue === "miles"  && resultTextValue === "mile"){
         result.value = Number(input.value) * 1;
    }else if (inputTextValue === "miles" && resultTextValue === "feet"){
         result.value = Number(input.value) * 5280;

    }
    // logic table for feet
    if(inputTextValue === "ft" && resultTextValue === "kilometer"){
        result.value = Number(input.value) * 0.0003048;
    }else if(inputTextValue === "ft"  && resultTextValue === "yard"){
        result.value = Number(input.value) * 0.333333;
    }else if (inputTextValue === "ft" && resultTextValue === "inch"){
        result.value = Number(input.value) * 12;
    }else if(inputTextValue === "ft"  && resultTextValue === "mile"){
         result.value = Number(input.value) * 0.000189394;
    }else if (inputTextValue === "ft" && resultTextValue === "feet"){
         result.value = Number(input.value) * 1;
    }

    if(inputTextValue === "yard" && resultTextValue === "kilometer"){
        result.value = Number(input.value) * 1;
    }else if(inputTextValue === "yard"  && resultTextValue === "yard"){
        result.value = Number(input.value) * 109.361;
    }else if (inputTextValue === "yard" && resultTextValue === "inch"){
        result.value = Number(input.value) * 3937.01;
    }else if(inputTextValue === "yard"  && resultTextValue === "mile"){
         result.value = Number(input.value) * 0.0621371;
    }else if (inputTextValue === "yard" && resultTextValue === "feet"){
         result.value = Number(input.value) * 328.084;

    }

} 
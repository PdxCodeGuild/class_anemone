let input = document.getElementById("input" );
let button = document.getElementById("button");
// let output = document.getElementsByTagName("p" );
let output = document.getElementById("output");

function callback(e) {
    // e.preventDefault();
    let value = input.value;
    let lower = value.toLowerCase();
    var rot = 'nopqrstuvwxyzabcdefghijklm';
    var alphabet = 'abcdefghijklmnopqrstuvwyxz';
    var result = '';
    for (element of lower) {
       let index = alphabet.indexOf(element);
       result += rot[index];

    }
output.innerText = `Your rot13 conversion of ${value} is ${result}`;
}
button.addEventListener('click', callback);
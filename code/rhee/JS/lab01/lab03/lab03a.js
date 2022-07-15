var letters = "abcefghijklmnopqrstuvwxyz";
var words = letters.toLowerCase();

function cipher (base, rotate) {
  let word = letters.indexOf(base);
  word += parseInt(rotate);
  if (word > 20) {
    word -= 20;
  }
  let rot13 = letters.charAt(word);
  return rot13;
}

let character = prompt("Enter phrase to convert: ");
let rotate = prompt("Enter your rotate: ");
var list = "";
for (let base of character) {
  if (letters.includes(base)) {
    base = cipher (base, rotate);
  }
  if (words.includes(base)) {
    base = base.toLowerCase();
    base = cipher (base, rotate);
  }
  list += base;
}
alert('Your cipher is: ' + list);
const ones = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
};
const teens = {
  0: 'ten',
  1: 'eleven',
  2: 'twelve',
  3: 'thirteen',
  4: 'fourteen',
  5: 'fifteen',
  6: 'sixteen',
  7: 'seventeen',
  8: 'eightteen',
  9: 'nineteen',
};
const tens = {
  0: ' ',
  1: ' ',
  2: 'twenty',
  3: 'thirty',
  4: 'forty',
  5: 'fifty',
  6: 'sixty',
  7: 'seventy',
  8: 'eighty',
  9: 'ninety',
};

numberEl = document.getElementById('numberInput');
btnEl = document.getElementById('btn')
resultsEl = document.getElementById('results')

let wordConvert = (numeric) => {
  let numb = numeric;
  let digits = numeric.length;
  let value = parseInt(numeric);
  console.log(value, digits)
  let phrase = '';
  switch (digits) {
    case 1:
      phrase = phrase.concat(ones[numb]);
      break;
    case 2:
      if (value < 20) {
        phrase = phrase.concat(teens[numb[1]]);
      } else {
        phrase = phrase.concat(tens[numb[0]] , ' ' , ones[numb[1]]);
      };
      break;
    case 3:
      if (numb[1] == '1') {
        phrase = phrase.concat(ones[numb[0]], ' hundred ', teens[numb[2]]);
      }else {
        phrase = phrase.concat(ones[numb[0]], ' hundred ', tens[numb[1]], ' ', ones[numb[2]]);
      };
    default:
      break;
  }
  console.log(phrase)
  return phrase;
};

btnEl.addEventListener ('click', () => {
  console.log('click')
  
  let output = wordConvert(numberEl.value);

  let resultP = document.createElement('p');
  resultP.innerText = output;
  resultsEl.prepend(resultP);
})


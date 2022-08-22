console.log('...intializing...');

let unitInEl = document.getElementById('unitInput');
let unitOutEl = document.getElementById('unitOutput');
let distanceEl = document.getElementById('distanceInput');
let btnEl = document.getElementById('btn');
let resultsEl = document.getElementById('results');

let toMeters = (unit) => {
  let cn = 0;
  switch (unit) {
    case 'in':
      cn = 0.0254;
      break;

    case 'ft':
      cn = 0.3048;
      break;
    case 'yd':
      cn = 0.9144;
      break;

    case 'mi':
      cn = 1609.34;
      break;

    case 'm':
      cn = 1.0;
      break;

    case 'km':
      cn = 1000.0;
      break;

    default:
  }
  return cn;
};

btn.onclick = (event) => {
  let unitInput = toMeters(unitInEl.value);
  let unitOutput = toMeters(unitOutEl.value);
  let distance = distanceEl.value;

  convertDistance = (distance * unitInput) / unitOutput;

  let resultP = document.createElement('p');
  resultP.innerText = convertDistance;
  resultsEl.prepend(resultP);
};

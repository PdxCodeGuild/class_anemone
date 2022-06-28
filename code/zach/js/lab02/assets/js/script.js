
console.log('...intializing...');
let distance = prompt('Enter integer value of distance: ');
let oUnit = prompt('Enter unit of input distance[in,ft,yd,mi,m,km]: ');
let cUnit = prompt('Enter unit distance is being converted to[in,ft,yd,mi,m,km]: ');




let toMeters = (unit) => {
  let cn=0
  switch(unit) {
    case 'in': cn = 0.0254;
    break;

    case 'ft': cn =0.3048;
    break;
    case 'yd': cn = 0.9144;
    break;

    case 'mi': cn = 1609.34;
    break;

    case 'm':   cn = 1.0;
    break;

    case 'km': cn =1000.0;
    break;

    default:
  }
  return cn;
}

let distanceConverter = (dis,x,y) => {
  convertDistance = (dis * x)/ y;
  return convertDistance;
}

let oVal = toMeters(oUnit)
let cVal = toMeters(cUnit)
let final = distanceConverter(distance,oVal,cVal);
console.log(`${distance} ${oUnit} converts to ${final} ${cUnit}`)

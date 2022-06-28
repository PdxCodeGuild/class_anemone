const numbers = [5, 0, 8, 3, 4, 1, 6];

function getAvg(numbers) {
  const total = numbers.reduce((acc, c) => acc + c, 0);
  return total / numbers.length;
}

const average = getAvg(numbers);
console.log(average);
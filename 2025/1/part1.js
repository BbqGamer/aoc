const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


let state = 50;
let count_zero = 0;
rl.on('line', (line) => {
    letter = line[0];
    val = Number(line.slice(1));
    if (letter === 'L') {
        state -= val;
    } else {
        state += val;
    }
    state = ((state % 100) + 100) % 100
    if (state === 0) {
        count_zero += 1;
    }
    console.log(state);
});

rl.on('close', () => {
  console.log("Result: ", count_zero);
});

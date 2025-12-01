const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


let state = 50;
let count_part1 = 0;
let count_part2 = 0
rl.on('line', (line) => {
    letter = line[0];
    val = Number(line.slice(1));
    if (letter === 'L') {
        let inv_state = 100 - state;
        if (state === 0) {
          inv_state = 0;
        }
        count_part2 += Math.floor((inv_state+val)/100)
        state -= val;

    } else { // R
        state += val;
        count_part2 += Math.floor(state/100);
    }
    state = ((state % 100) + 100) % 100
    if (state === 0) {
        count_part1 += 1;
    }
});

rl.on('close', () => {
  console.log("Part 1: ", count_part1);
  console.log("Part 2: ", count_part2)
});

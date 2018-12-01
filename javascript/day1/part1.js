const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
});

let frequencyCount = 0;

rl.on("line", (input) => {
  frequencyCount += Number.parseInt(input.trim())
}).on("close", () => {
  console.log(`Frequency is ${frequencyCount}`);
})

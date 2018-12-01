const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
});

let frequencyList = [];

rl.on("line", (input) => {
  frequencyList.push((Number.parseInt(input.trim())));
}).on("close", () => {
  let currentFrequency = 0;
  let frequenciesSeen = new Set();
  frequenciesSeen.add(currentFrequency);

  let currentIndex = 0;
  while (true) {
    currentFrequency += frequencyList[currentIndex];
    if (frequenciesSeen.has(currentFrequency)) {
      console.log(`Saw frequency ${currentFrequency} twice`);
      break;
    } else {
      currentIndex = (currentIndex + 1) % frequencyList.length;
      frequenciesSeen.add(currentFrequency);
    }
  }
})

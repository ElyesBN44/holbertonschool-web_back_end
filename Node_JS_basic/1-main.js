const { spawn } = require('child_process');

// Simulate input for the child process
const child = spawn('node', ['1-stdin.js']);

child.stdout.on('data', (data) => {
  process.stdout.write(data);
});

child.stderr.on('data', (data) => {
  process.stderr.write(`Error: ${data}`);
});

// Send input after receiving the initial prompt
child.stdin.write('Alice\n');

// Close the input stream to trigger 'end'
child.stdin.end();

child.on('close', (code) => {
  console.log(`Child process exited with code ${code}`);
});

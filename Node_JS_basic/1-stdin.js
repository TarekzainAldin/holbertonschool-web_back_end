// Display the initial message
console.log('Welcome to Holberton School, what is your name?');

// Enable stdin to read user input
process.stdin.setEncoding('utf8');

// Listen for user input
process.stdin.on('readable', () => {
    const input = process.stdin.read();
    if (input !== null) {
        const name = input.trim(); // Trim any extra spaces or newlines
        console.log(`Your name is: ${name}`);

        // Once the name is displayed, close the input stream
        process.stdin.end();
    }
});

// When stdin ends, display the exit message
process.stdin.on('end', () => {
    console.log('This important software is now closing');
});

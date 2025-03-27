import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

// Handle connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new school (unchanged)
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// Async function to display school value
async function displaySchoolValue(schoolName) {
  try {
    const reply = await getAsync(schoolName);
    console.log(reply);
  } catch (err) {
    console.error(err);
  }
}

// Call the functions as required
(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();

// Close the connection when done (optional)
// client.quit();

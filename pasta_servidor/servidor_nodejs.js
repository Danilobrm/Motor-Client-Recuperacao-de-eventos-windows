const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

// Object to store connected users along with their names and IP addresses
const connectedUsers = {};

wss.on('connection', function connection(ws, req) {
  console.log('Client connected');
  let userData

  ws.once('message', function firstMessage(message) {
    userData = JSON.parse(message);
    const ip = req.socket.remoteAddress;
    console.log(ip)
    connectedUsers[ip] = { userData: userData, updates: {} }; // Initialize updates object
    console.log('User connected:', userData.username);
  });

  ws.on('message', function incoming(message) {
    const updates = JSON.parse(message);

    const test = {
      user: {
        ...userData
      },
      ...updates,
      status: setStatus(updates.idle_time)
    }

    console.log(test)

  });

  ws.on('error', function error(err) {
    console.error('Connection error:', err);
  });

  ws.on('close', function close() {
    console.log('Client disconnected');
    const ip = req.socket.remoteAddress;
    delete connectedUsers[ip];
  });
});

wss.on('error', function error(err) {
  console.error('WebSocket server error:', err);
});

console.log('WebSocket server is listening on port 8080');

function setStatus(idle_time) {
  if(idle_time > 0)
    return "idle"

  return "online"
}
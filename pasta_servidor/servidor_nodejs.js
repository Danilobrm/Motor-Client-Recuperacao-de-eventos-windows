const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8080 });
const connected = new Set();

wss.on("connection", function connection(ws, req) {
  console.log("Client connected");
  connected.add(ws);
  let userData;
  
  ws.once("message", function firstMessage(message) {
    message = JSON.parse(message);
  });
  
  ws.on("message", function incoming(message) {
    const info = JSON.parse(message);
    console.log(info)

    const data = {
      ...userData,
      ...info,
      status: getStatus(info.idle_time)
    }

    connected.forEach((admin) => {
      ws.send(JSON.stringify(data))
    })
    ws.send(JSON.stringify(data))
  });

  ws.on("error", function error(err) {
    console.error("Connection error:", err);
  });

  ws.on("close", function close() {
    console.log("Client disconnected");
    // const ip = userData.user.ipv4_address;
    // const userIndex = connectedUsers.findIndex(user => user.ip === ip);
    // if (userIndex !== -1) {
    //   connectedUsers.splice(userIndex, 1); // Remove user from the connectedUsers array
    // }
  });
});

wss.on("error", function error(err) {
  console.error("WebSocket server error:", err);
});

console.log("WebSocket server is listening on port 8080");

function sendUserUpdates(user) {
  user.ws.send(JSON.stringify(user.userData)); // Send updates to the specific user
}

function getStatus(idle_time) {
  return idle_time > 0 ? "idle" : "online";
}

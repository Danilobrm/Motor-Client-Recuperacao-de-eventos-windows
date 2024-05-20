const WebSocket = require("ws");

const wss = new WebSocket.Server({ port: 8080 });
const connectedUsers = new Map(); // Store connections with their identifiers

wss.on("connection", function connection(ws, req) {
  console.log("Client connected");
  let userData;
  
  ws.once("message", function firstMessage(message) {
    message = JSON.parse(message);

    message.role &&
      connectedUsers.set(message.role, ws) && console.log("Admin connected");
  });

  ws.on("message", function incoming(message) {
    const info = JSON.parse(message);

    !info.role && console.log(info)

    const data = {
      ...userData,
      ...info,
      status: getStatus(info.idle_time),
    };
    // if(data.user.role) {
    //   console.log(data.user)
    // }
    
    // data.user.role = "desenvolvedor"
    

    const adminConnection = connectedUsers.get('admin');
    if (adminConnection) {
      !info.role && adminConnection.send(JSON.stringify({ type: 'update', data }));
    }
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

function getStatus(idle_time) {
  return idle_time > 0 ? "idle" : "online";
}

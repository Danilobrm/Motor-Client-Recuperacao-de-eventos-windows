const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function connection(ws) {
  console.log('Cliente conectado');

  ws.on('message', function incoming(message) {
    // console.log('Mensagem recebida: %s', message);
    console.log('%s', message);
    // Aqui você pode processar a mensagem recebida, por exemplo, gravar em um banco de dados.
  });

  ws.on('error', function error(err) {
    console.error('Erro na conexão:', err);
  });

  ws.on('close', function close() {
    console.log('Cliente desconectado');
  });
});

wss.on('error', function error(err) {
  console.error('Erro no servidor WebSocket:', err);
});


console.log('Servidor WebSocket está escutando na porta 8080');
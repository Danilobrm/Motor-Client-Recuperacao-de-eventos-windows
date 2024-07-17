export default (colaboradores) => {
  const server_ip = 'localhost'
  const port = 8080
  const ws = new WebSocket(`ws://${server_ip}:${port}`)

  ws.onopen = () => {
    ws.send(JSON.stringify({ role: 'admin' }))

    console.log('Connected to WebSocket server')
  }

  ws.onmessage = async (message) => {
    const newColaborador = await JSON.parse(message.data)

    const index = colaboradores.findIndex((colaborador) => colaborador !== newColaborador)

    if (index === -1) colaboradores.push(newColaborador.data)
    else {
      if (colaboradores[index].status != newColaborador.data.status)
        colaboradores[index].status = newColaborador.data.status
      else if (colaboradores[index].programs != newColaborador.data.programs)
        colaboradores[index].programs = newColaborador.data.programs
    }

  }
}

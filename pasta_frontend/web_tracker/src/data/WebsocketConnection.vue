<script>
// export default {
//   data() {
//     return {
//       colaboradores: []
//     }
//   },
//   created() {
//     const server_ip = 'localhost'
//     const port = 8080
//     const ws = new WebSocket(`ws://${server_ip}:${port}`)

//     ws.onopen = () => {
//       console.log('Connected to WebSocket server')
//       ws.send(JSON.stringify({ role: 'admin' }))
//     }

//     ws.onmessage = async (message) => {
//       const newColaborador = await JSON.parse(message.data)
//       if(newColaborador.data.role)
//         return

      
//       if(this.colaboradores.findIndex(colaborador => colaborador !== newColaborador) === -1)
//         this.colaboradores.push(newColaborador.data)
//     }
//   }
// }
</script>
<script>
import MonitorHeading from '../components/MonitorHeading.vue'
import MonitorSubheading from '../components/MonitorSubheading.vue'
import ColaboratorsTable from '../components/ColaboratorsTable.vue'

export default {
  components: {
    MonitorHeading,
    MonitorSubheading,
    ColaboratorsTable
  },
  data() {
    return {
      colaboradores: [],
      amount: 0
    }
  },
  created() {
    const server_ip = 'localhost'
    const port = 8080
    const ws = new WebSocket(`ws://${server_ip}:${port}`)

    ws.onopen = () => {
      ws.send(JSON.stringify({ role: 'admin' }))
      message(this.colaboradores)

      console.log('Connected to WebSocket server')
    }

    function message(colaboradores) {
      ws.onmessage = async (message) => {
        const newColaborador = await JSON.parse(message.data)
        console.log(newColaborador)

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
  }
}
</script>

<template>
  <div class="monitor">
    <MonitorHeading heading="Colaboradores" />
    <MonitorSubheading :amount="colaboradores.length" />
    <ColaboratorsTable :colaboradores="colaboradores" />
  </div>
</template>

<style>
.monitor {
  margin: 52px 26px 52px calc(132px + 26px);
  display: flex;
  flex-direction: column;
  width: 100%;
}
</style>

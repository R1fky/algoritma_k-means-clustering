import express from 'express'
import clusterRouter from './router/clusterRouter.js'

const app = express()
const port = 3000

app.get('/', (req, res) => {
    res.send('First API')
})

app.use('/predict', clusterRouter)



app.listen(port, () => {
    console.log(`server running in http://localhost:${port}`)
})
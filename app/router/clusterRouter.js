import express from 'express'
import { predictCluster } from '../controller/clusterController.js'

const router = express.Router()

// router.get('/', predictCluster)

router.post('/predict-cluster', predictCluster) // satu user


export default router
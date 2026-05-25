import express from 'express'
import { predictCluster } from '../controller/clusterController.js'

const router = express.Router()

router.get('/', predictCluster)

export default router
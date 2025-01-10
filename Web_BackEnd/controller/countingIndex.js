import express from 'express'
import ctrl from './countingCtrl.js'

let currentCount = 0;

const router = express.Router();

router.post('/update_count', (req, res) => {
    const { count } = req.body;
    // console.log('count:', count);
    if (typeof count === 'number') {
        currentCount = count;
        // console.log(`Updated  count: ${currentCount}`);
        res.status(200).send('Count updated');
    } else {
        res.status(400).send('Invalid data');
    }
});

router.get('/', ctrl.startCounting = (req, res) => {
    res.json({ count: currentCount });
});

export default router;
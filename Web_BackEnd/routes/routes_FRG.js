import login from './login/loginIndex.js'
import details from './details/detailsIndex.js'
import cctvRouter from './cctv/cctvIndex.js';
import counting from './counting/countingIndex.js';

const mountRouters = (app, server) => {
    app.use('/login', login);
    app.use('/details', details);
    app.use('/counting', counting);
    app.use('/cctv', cctvRouter);
}

export default mountRouters;
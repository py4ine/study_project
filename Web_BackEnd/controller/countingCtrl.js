import { spawn } from 'child_process';

let pythonProcess = null;
let currentCount = 0;
const condaPath = 'c:/miniconda3/envs/p2/python.exe';

const startCounting = () => {

    if (pythonProcess) {
        console.log('Python script is already running.');
        return;
    }
    
    console.log('Starting Python script...');
    pythonProcess = spawn(condaPath, ['./src/api/counting/countingProcess.py']);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python Output: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python Error: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`Python script exited with code ${code}`);
        pythonProcess = null; // 종료되면 프로세스 변수 초기화
    });

}
startCounting();

export default {
    startCounting,
}
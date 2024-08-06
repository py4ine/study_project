import { Line } from "react-chartjs-2";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
  } from "chart.js";

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
);  

const labels = ["2017", "2018", "2019", "2020", "2021", "2022", "2023", "2024"];

const options = {
    responsive: true,  // 반응형으로 차트를 만들고 싶을 경우 true
    interaction: {  // 차트위 hover했을 때, 데이터 값이 보이는 것
        intersect: false  //  true = 정확한 데이터 위치에 hover해야 데이터 값이 보임 = defalut
    },
    scales: {  // 축의 그리드(선) 설정
        x: { grid: { display: false } },
        y: { grid: { display: true } }
    },
    plugins: {
        legend: { position: "bottom" } }  // 레전드 위치설정 default = "top"
};


export const data = {
    labels,
    datasets: [
        {
            label: "React",
            data: [32, 42, 51, 60, 51, 95, 97, 88],
            backgroundColor: "#0CD3FF",
            borderColor: "#0C3FF"
        },
        {
            label: "Angular",
            data: [38, 45, 54, 61, 50, 99, 93, 81],
            backgroundColor: "#a6120d",
            borderColor: "#a6120d"
        },
        {
            label: "Vue",
            data: [60, 30, 10, 20, 10, 50, 90, 80],
            backgroundColor: "#FFCA29",
            borderColor: "#FFCA29"
        },
    ],
};


const ChartjsExample = () => {
    return (
        <div>
            <h1>Chart js</h1>
            <div style={{ width: 600, height: 300 }}>
                <Line options={options} data={data} />
            </div>
        </div>
    )
}

export default ChartjsExample;
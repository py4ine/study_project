import React, { useState, useEffect } from 'react';

function  Counting() {
    const [count, setCount] = useState(0);
    const [imageBlob, setImageBlob] = useState(null);

    // 서버에서 데이터를 가져오는 함수
    const fetchCount = async () => {
        try {
            const response = await fetch('http://localhost:8080/counting');
            const data = await response.json();
            // console.log("받은데이터:", data);
            setCount(data.count);
        } catch (error) {
            console.error('Error fetching person count:', error);
        }
    };

    // 컴포넌트가 마운트되면 매초 데이터를 가져옴
    useEffect(() => {
        const interval = setInterval(fetchCount, 1 * 500);  // 0.5초마다 데이터 가져오기
        return () => clearInterval(interval); // 컴포넌트 언마운트 시 정리
    }, []);

    useEffect(() => {
        let ws;
    
        const connectWebSocket = () => {
            ws = new WebSocket('ws://localhost:9988');
            ws.binaryType = "blob"; // WebSocket 데이터를 바이너리 Blob으로 수신
    
            ws.onopen = () => {
                console.log("WebSocket connected!");
                ws.send("Hello from client!");
            };
            ws.onmessage = (event) => {
                // console.log("Message from server:", event.data);
                if (event.data instanceof Blob) {
                    setImageBlob(URL.createObjectURL(event.data)); // Blob URL 생성
                }
            };
            ws.onclose = () => {
                console.log("WebSocket connection closed. Retrying in 5 seconds...");
                setTimeout(connectWebSocket, 1000); // 5초 후 재연결 시도
            };
            ws.onerror = (error) => {
                console.error("WebSocket error:", error);
                ws.close();
            };
        };
    
        connectWebSocket();
    
        // 컴포넌트 언마운트 시 WebSocket 정리
        return () => {
            if (ws && ws.readyState === WebSocket.OPEN) {
                ws.close();
            }
        };
    }, []); // 빈 배열은 WebSocket 설정을 한 번만 실행하도록 설정
    

    return (
        <div style={{ textAlign: 'center', marginTop: '50px' }}>
            <h1>Real-Time Count</h1>
            <p style={{ fontSize: '24px', fontWeight: 'bold' }}>Current Count: {count}</p>
            {imageBlob && (
                <div>
                    <h2>Live Feed</h2>
                    <img src={imageBlob} alt="Live feed" style={{ maxWidth: '100%', height: 'auto' }} />
                </div>
            )}
        </div>
    );
}

export default Counting;
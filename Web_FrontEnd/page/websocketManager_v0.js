
let ws = null;
let activePage = null; // 현재 활성 페이지

export const connectWebSocket = () => {

    if (ws && ws.readyState === WebSocket.OPEN) return;  // 이미 연결되어 있으면 중복 연결 방지

    ws = new WebSocket('ws://localhost:8000/stream');

    ws.onopen = () => {
        console.log("WebSocket connection opened!");
    }
    ws.onmessage = (event) => {
        if (!activePage) return;  // 활성화 페이지 없으면 데이터 무시
        // console.log("Message from server:", event.data); // 데이터를 로깅하거나 상태 업데이트
        if (typeof event.data === "string") {
            handleTextMessage(event.data);  // 텍스트 데이터 처리
        } else if (event.data instanceof Blob) {
            handleVideoMessage(event.data);  // 바이너리 데이터 처리
        }
    };
    ws.onclose = () =>  {
        console.log("WebSocket connection closed. Retrying...");
        ws = null;
        setTimeout(connectWebSocket, 3000);  // 연결이 끊기면 3초 뒤에 다시 연결 시도
    };
    ws.onerror = (error) => {
        console.error("WebSocket error:", error);
        ws.close();
    };
};

const handleTextMessage = (message) => {
    if (!message) return;  // 데이터가 비어있으면 처리하지 않음
    // console.log("Text Message:", message);

    // counting 페이지 업데이트
    const event = new CustomEvent("countingUpdate", { detail: { count: message }});
    window.dispatchEvent(event);  // counting 페이지로 이벤트 전달
};

const handleVideoMessage = async (blob) => {
    // console.log("Binary Message Received");
    try {
        if (!blob) return;  // 데이터가 비어있으면 처리하지 않음

        // Blob 데이터를 cctv 페이지로 전달
        const arrayBuffer = await blob.arrayBuffer();
        const event = new CustomEvent("cctvUpdate", { detail: { frame: arrayBuffer }});
        window.dispatchEvent(event);  // cctv 페이지로 이벤트 전달
    } catch (error) {
        console.error("Error processing Binary message", error);
    }    
};

// 활성 페이지 설정
export const setActivePage = (page) => {
    activePage = page;
    console.log(`Active page set to: ${page}`);
};

export const getWebSocket = () => ws;  // WebSocket 객체를 가져오는 함수
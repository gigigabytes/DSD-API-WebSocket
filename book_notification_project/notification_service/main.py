from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from websocket_manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    await manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

@app.post("/notify/{user_id}")
async def notify_user(user_id: str, message: str):
    await manager.broadcast(f"User {user_id}, {message}")
    return {"message": f"Notification sent to user {user_id}"}

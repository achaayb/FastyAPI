from fastapi import APIRouter, WebSocket, Depends, WebSocketDisconnect
from ..helpers.response import Response, Error
from ..models import users as users_models
from ..dependencies import auth as auth_dependencies

from bson import ObjectId

router = APIRouter(
    responses={404: {"description": "Not found"}},
    dependencies = [Depends(auth_dependencies.JWT_protect)]
)

class ConnectionManager:
    def __init__(self):
        #dumb to use it like this in prod.
        #use redis or something idk, wait for next push.
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, data: str):
        for connection in self.connections:
            await connection.send_text(data)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)
    
    async def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.broadcast(f"message : User Joined")
    await manager.connect(websocket)
    while True:
        try:
            data = await websocket.receive_text()
            await manager.broadcast(f"message : {data}")
        except (WebSocketDisconnect):
            await manager.disconnect(websocket)
            await manager.broadcast(f"message : User Disconnected")
            break
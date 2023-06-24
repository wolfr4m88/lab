import asyncio
import uvicorn
from fastapi import FastAPI

class MessageService:
    @staticmethod
    async def get_message():
        return {'msg': 'not implemented yet'}

app = FastAPI()

app.add_api_route("/message", MessageService.get_message, methods=["GET"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5002)

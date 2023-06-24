import asyncio
import uvicorn
from fastapi import FastAPI
import hazelcast

app = FastAPI()

client = hazelcast.HazelcastClient(cluster_members=["127.0.0.1:5701"])

distributed_queue = client.get_queue("distributed-queue")
messages = []

async def consume_messages():
    while True:
        message = await distributed_queue.take()
        messages.append(message)

@app.get("/message")
async def get_message():
    return {'msg': messages}

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(consume_messages())
    uvicorn.run(app, host="0.0.0.0", port=5002)  # Запустіть другий екземпляр на порті 5003

import uvicorn
import hazelcast
from fastapi import FastAPI
from pydantic import BaseModel

client = hazelcast.HazelcastClient(cluster_members=["127.0.0.1:5701"])
distributed_map = client.get_map("distributed-map")

class Log(BaseModel):
    uuid: str
    msg: str

class LoggingService:
    @staticmethod
    async def create_log(log: Log):
        await distributed_map.set(log.uuid, log.msg)
        return {'uuid': log.uuid, 'msg': log.msg}

    @staticmethod
    async def get_log():
        all_values = await distributed_map.values()
        return {'logs': all_values}

app = FastAPI()

app.add_api_route("/log", LoggingService.get_log, methods=["GET"])
app.add_api_route("/log", LoggingService.create_log, methods=["POST"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5005)

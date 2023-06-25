import requests
import os
from flask import Flask
from random import randint

app = Flask(__name__)


def register_service_to_consul(service_name, port):
    consul_host = os.getenv('CONSUL_HOST', 'localhost')
    consul_port = os.getenv('CONSUL_PORT', 8500)

    service_definition = {
        "ID": service_name,
        "Name": service_name,
        "Tags": ["microservice"],
        "Address": "127.0.0.1",
        "Port": port,
        "Check": {
            "DeregisterCriticalServiceAfter": "90m",
            "HTTP": f"http://localhost:{port}/health",
            "Interval": "10s"
        }
    }
    requests.put(f'http://{consul_host}:{consul_port}/v1/agent/service/register', json=service_definition)


@app.route('/health', methods=['GET'])
def health_check():
    return "Healthy", 200


if __name__ == "__main__":
    service_port = randint(3000, 5000)  # Random port for the microservice
    register_service_to_consul('facade-service', service_port)
    app.run(port=service_port)

from flask import Flask, request, jsonify
import requests, uuid, logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

class FacadeService:
    @staticmethod
    @app.route('/', methods=['POST'])
    def post_data():
        msg = request.get_json()["msg"]
        msg_id = uuid.uuid4()
        payload = {"id": str(msg_id), "msg": msg}
        requests.post('http://localhost:5001/', json=payload)
        logging.info(f"Message with id {msg_id} sent successfully\n")
        return f"Message with id {msg_id} sent successfully\n", 200

    @staticmethod
    @app.route('/', methods=['GET'])
    def get_data():
        response_logging = requests.get('http://localhost:5001/').text
        response_messages = requests.get('http://localhost:5002/').text
        logging.info(f"Received responses from logging and messages services\n")
        return response_logging + "\n" + response_messages, 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)

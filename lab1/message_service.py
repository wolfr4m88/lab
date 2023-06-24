from flask import Flask, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

class MessageService:
    @staticmethod
    @app.route('/', methods=['GET'])
    def get_data():
        logging.info("Returned static message\n")
        return 'not implemented yet\n', 200

if __name__ == '__main__':
    app.run(port=5002, debug=True)

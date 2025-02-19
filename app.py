from flask import Flask, request
import logging

app = Flask(__name__)

# Configurar logging en Amazon Linux 2
logging.basicConfig(filename="C:\Python\flask_app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.route('/test', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        data = request.args.to_dict()
        log_msg = f"Received GET request: {data}"
    elif request.method == 'POST':
        data = request.form.to_dict()
        log_msg = f"Received POST request: {data}"

    print(log_msg)  # Muestra en consola
    app.logger.info(log_msg)  # Guarda en log

    return {"status": "success", "data": data}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

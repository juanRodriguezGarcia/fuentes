from flask import Flask, request, jsonify
import logging
import requests

app = Flask(__name__)

# Configurar logging en Windows
logging.basicConfig(filename="flask_app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

# URL del servidor al que quieres hacer la solicitud (cambia si es necesario)
url = "http://localhost:5001/test2"

# Cabeceras HTTP
headers = {
    "Content-Type": "application/json"
}

@app.route('/test', methods=['POST','GET'])

def handle_request():
    if request.method == 'GET':
        data = request.args.to_dict()
        log_msg = f"Received GET request: {data}"
        print(log_msg)
        return {"status": "success", "data": data}, 200
#    elif request.method == 'POST':
        
#        data = request.form.to_dict()
#        log_msg = f"Received POST request: {data}"

#    print(log_msg)  # Muestra en consola
#    app.logger.info(log_msg)  # Guarda en log
    try:
        data = request.get_json()
        if not data:
            print("Error 400: No se recibió JSON")
            return jsonify({"error": "No se recibió JSON"}), 400

        print("Status success, data:", data)

        # Enviar request a otro servidor
        response = requests.post(url, json=data, headers=headers)

        # Imprimir la respuesta del servidor
        print("Código de estado:", response.status_code)
        print("Respuesta JSON:", response.json())

        return jsonify({
            "status": "success",
            "data_received": data,
            "server_response": response.json()
        }), 200

    except Exception as e:
        print("Error 500...", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

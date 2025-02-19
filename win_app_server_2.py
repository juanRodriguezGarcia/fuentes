from flask import Flask, request, jsonify
import logging



app = Flask(__name__)

# Configurar logging en Windows
logging.basicConfig(filename="flask_app.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

@app.route('/test2', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        data = request.args.to_dict()
        log_msg = f"Received GET request: {data}"
    try:
        data = request.get_json()
        if not data:
            print("error 400 No se recibió JSON")
            return jsonify({"error": "No se recibió JSON"}), 400
        print("status success data", data)
        return jsonify({"status": "success", "data": data}), 200
    except Exception as e:
        print("error 500...(*-*)", str(e))
        return jsonify({"error": str(e)}), 500

    return {"status": "success", "data": data}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

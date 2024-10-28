from flask import Flask, request, jsonify
from gpiozero import LED # type: ignore

app = Flask(__name__)

def process_data(data):
    # Add your data processing logic here
    print("Processing data:", data)
    # For example, you could control an LED based on the data
    led = LED(27)
    if data.get["buttons"]["button_2"] == 1:
        led.on()
    else:
        led.off()

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.is_json:
        data = request.get_json()
        # Process the JSON data here
        process_data(data)
        return jsonify({"message": "JSON received and processed"}), 200
    else:
        return jsonify({"message": "Request is not JSON"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
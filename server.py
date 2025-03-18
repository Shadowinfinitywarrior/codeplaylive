from flask import Flask, send_from_directory
import socket

app = Flask(__name__)

@app.route('/')
def serve_page():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Get local IP address dynamically
    host_ip = socket.gethostbyname(socket.gethostname())
    port = 5000  # Change this if needed

    print(f"Server running at: http://{host_ip}:{port}")
    print("Accessible from another device on the same network.")

    # Run the Flask app and make it accessible to other devices on the network
    app.run(host='0.0.0.0', port=port, debug=True)

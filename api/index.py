from flask import Flask, send_file, request
from datetime import datetime

app = Flask(__name__)

# accepts ANY path, ie test, test.png, bleh/test.png
@app.route('/<path:path>')

def track(path):
    # Capture the requester's IP and the current time
    requester_ip = request.remote_addr
    access_time = datetime.now()

    print(f"Path: {path} IP: {requester_ip} Time: {access_time}")
    # Log the IP and time TODO later send this to database. sqlite would be fine but i want practice w influxdb. this could be separate server or use influxdb http api for sep server. have failsafe if the server is down.

    return send_file("boo.png", mimetype="image/png")

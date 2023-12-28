from flask import Flask, send_file, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def track():  # put application's code here
    # Capture the requester's IP and the current time
    requester_ip = request.remote_addr
    access_time = datetime.now()

    # Log the IP and time TODO later send this to database. sqlite would be fine but i want practice w influxdb. this could be separate server or use influxdb http api for sep server. have failsafe if the server is down.
    print(f"Image requested by {requester_ip} at {access_time}") #TODO also include the url they requested with whatever other deets
    return send_file("boo.png", mimetype="image/png")
if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=5000)

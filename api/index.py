from flask import Flask, send_file, request
from datetime import datetime
import os, time
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
bucket = "pixl"
org = "pixl"
url = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)
write_api = client.write_api(write_options=SYNCHRONOUS)

app = Flask(__name__)

# accepts ANY path ending in .png, ie test.png, bleh/test.png
@app.route('/<path:path>.png')

def track(path):
    # Capture the requester's IP and the current time
    requester_ip = request.remote_addr
    access_time = time.time()

    print(f"Path: {path} IP: {requester_ip} Time: {access_time}")
    # Log the IP and time TODO later send this to database. sqlite would be fine but i want practice w influxdb. this could be separate server or use influxdb http api for sep server. have failsafe if the server is down.

    p = influxdb_client.Point("q").tag("IP", requester_ip).tag("epoch", access_time).field("path", path)
    write_api.write(bucket=bucket, org=org, record=p)

    return send_file("boo.png", mimetype="image/png")

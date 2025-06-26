from fastapi import FastAPI

app = FastAPI()

device_status = {"pump": "OFF"}

@app.get("/status")
def get_status():
    return device_status

@app.post("/toggle")
def toggle():
    device_status["pump"] = "ON" if device_status["pump"] == "OFF" else "OFF"
    return device_status

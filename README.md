# API for screen shots
a simple flask json api to take screen shots!
## Installing
Please install the requirements:
```
# Linux/macOS
python3 -m pip install -r requirements.txt
# Windows
py -3 -m pip install -r requirements.txt
```
[Install Chrome driver ](https://chromedriver.chromium.org/home)
And then you're ready to go
## Runing 
```
python app.py
```
## Usage
``http://127.0.0.1:5000/shot?url=<your_requested_url>``
## Response Example 
api returns base64 screenshot 
```json
{"screenshot":"iVBORw0KGgoAAAANSUhEUgAABAoAAALDCAYAAACck+JqAAAAAXNSR0IArs4c6QAAIABJREFUeJzs3Xl8VOW9x/HvObNmTwgQdhGUTdTivoJLlbphKy61vd1v69ZW26q9tda21m4WrVqpVbvZe+tCcUOrRcSCC4oiKKIIaJQ9EJKQZTL7OfcP4JRAkjmTzGQmyef9evmqTJ","success":true}
```
if request url not found or not responding
```json
{"error":"Bad request","success":false}
```
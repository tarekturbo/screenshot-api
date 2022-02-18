import selenium
import validators
from flask import Flask,request,jsonify
from selenium import webdriver
app = Flask(__name__)
@app.route("/shot")
def screenshot():
    if request.args.get("url") !=  None:
        if validators.url(request.args.get("url")):
            try:
                driver.get(request.args.get("url"))
                return jsonify({"success":True,"screenshot":driver.get_screenshot_as_base64()}) 
            except:
                return jsonify({"success":False,"error":"Bad request"})
        else:
            return jsonify({"success":False,"error":"Invaild url"})
    else:
        return jsonify({"success":False,"error":"Parameter url i required"})
if __name__ == "__main__":
    driver = webdriver.Chrome()
    app.run()
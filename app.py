import selenium
from flask import Flask,request
from selenium import webdriver
app = Flask(__name__)
@app.route("/shot")
def screenshot():
    url = request.args.get("url")
    driver.get(url)
    return driver.get_screenshot_as_png(),200,{"Content-Type":"image/png"}
if __name__ == "__main__":
    driver = webdriver.Chrome()
    app.run()
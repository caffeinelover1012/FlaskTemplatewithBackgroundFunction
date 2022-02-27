from flask import Flask, render_template, url_for, request, redirect
import atexit
app = Flask(__name__)
from apscheduler.schedulers.background import BackgroundScheduler


def functoberun():
    print("Hello")

scheduler = BackgroundScheduler()
scheduler.add_job(func=functoberun, trigger="interval", seconds=1)
scheduler.start()

@app.route("/")
def hello():
    return render_template("test.html")

atexit.register(lambda: scheduler.shutdown())

if __name__=="__main__":
    app.run(port=5000,debug=True,use_reloader=False)

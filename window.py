import flask
import threading
import Tkinter
import tkMessageBox
import Queue

root = Tkinter.Tk()
app = flask.Flask(__name__)
jobs = Queue.Queue()

@app.route('/')
def index():
    return 'Hi Oleg'

@app.route('/handler/<text>')
def handler(text):
    jobs.put(text)
    return "response"

def process_job():
    while True:
        try:
            job = jobs.get(timeout=1)
            tkMessageBox.showinfo("Title job", job)
        except:
            break
    root.after(100, process_job)

def flask_main():
    app.run(port=8080)


if __name__ == "__main__":
    flask_thread = threading.Thread(target=flask_main)
    flask_thread.daemon = True
    flask_thread.start()
    root.after(100, process_job)
    root.mainloop()
    flask_thread.join()
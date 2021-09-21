from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def input_number():
    return render_template('input.html')

@app.route("/process_number?number=<telp>")
def process_number(telp):
    return redirect(url_for('detail_number',telp=telp))

@app.route("/<telp>")
def detail_number(telp=6288888888888):
    return render_template('index.html', telp=telp)

    
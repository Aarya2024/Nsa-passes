from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

event_data = pd.read_csv('trial.csv')

@app.route("/")
def home():
    return render_template("login.html")
#def is_valid_id(reg_id):
    #print(f"Checking ID: {reg_id}")  # Debugging line
 #   return reg_id in event_data['id'].astype(str).values

@app.route("/validate")
def validate():
    reg_id = request.args.get('id')
    #print(f"Received ID: {reg_id}")
    #if is_valid_id(reg_id):
    if reg_id in event_data['id'].astype(str).values:
        return render_template("new.html")
    else:
        return render_template("access_denied.html")

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'secrets, secrets'
import random

@app.route ('/')
def index():
    if "myGold" not in session:
        session["myGold"] = 0
    
    
    return render_template('ninja_gold.html')

@app.route ('/process_money', methods=["POST"])
def process_money():
    print(request.form)
    if request.form["location"]=="farm":
        print("I'm at the farm")
        randNum = random.randint(10, 20)
        session["myGold"] += randNum
    if request.form["location"]=="cave":
        print("I'm at the cave")
        randNum = random.randint(5, 10)
        session["myGold"] += randNum
    if request.form["location"]=="house":
        print("I'm at the house")
        randNum = random.randint(2, 5)
        session["myGold"] += randNum
    elif request.form["location"]=="casino":
        print("I'm at the casino")
        randNum = random.randint(-50, 50)
        session["myGold"] += randNum

    return redirect('/')


if __name__=="__main__": 
    app.run(debug=True) 
from flask import Flask, render_template
from practice2 import BankAccount

app = Flask(__name__)

@app.route("/")
def home():
    acc = BankAccount("Shashank", 12345, 90000)
    acc.deposit(2000)
    acc.withdraw(1500)
    details = acc.display()
    return render_template("index.html", details=details)

if __name__ == "__main__":
    app.run(debug=True)

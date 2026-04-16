from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("cakeshop.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    conn = get_db()
    cakes = conn.execute("SELECT * FROM cakes").fetchall()
    conn.close()
    return render_template("index.html", cakes=cakes)

if __name__ == "__main__":
    app.run(debug=True)
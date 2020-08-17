import sqlite3
from flask import Flask, request, redirect, flash, render_template, url_for

app = Flask(__name__)
app.secret_key = "Secret Key"


@app.route('/')
def index():
    sqliteConnection = sqlite3.connect('mns_database.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT * FROM Agent")
    rows = cursor.fetchall()
    sqliteConnection.commit()
    cursor.close()
    return render_template("index.html", agent=rows)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        sno = request.form['sno']
        agent = request.form['agent']
        amount = request.form['amount']
        sqliteConnection = sqlite3.connect('mns_database.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("INSERT INTO Agent (sno, agent, amount) VALUES (?, ?, ?)", (sno, agent, amount))
        sqliteConnection.commit()
        cursor.close()
        flash("Agent Inserted Successfully")
    return redirect(url_for('/'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == "POST":
        sno = request.form["sno"]
        agent = request.form["agent"]
        amount = request.form["amount"]
        sqliteConnection = sqlite3.connect('mns_database.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("UPDATE Agent SET sno=?,amount=? WHERE agent=?", (sno, amount, agent))
        sqliteConnection.commit()
        cursor.close()
    flash("Agent Updated Successfully")
    return redirect(url_for('/'))


@app.route('/delete', methods=['POST'])
def delete():
    agent = request.form['agent']
    sqliteConnection = sqlite3.connect('mns_database.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("DELETE FROM Agent WHERE agent=?", (agent,))
    sqliteConnection.commit()
    cursor.close()
    flash("Agent Deleted Successfully")
    return redirect(url_for('/'))


if __name__ == '__main__':
    app.run()

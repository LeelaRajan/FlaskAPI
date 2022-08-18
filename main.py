import mysql.connector as connection
from flask import Flask, render_template, request, jsonify
import csv
app = Flask(__name__)
# creation of DB
@app.route('/DB_creation', methods=['POST'])
def db_create():
    if (request.method=='POST'):
        conn = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)
        cur = conn.cursor()  # create a cursor to execute queries
        cur.execute("create database db1")
        return jsonify(status="success", message="DB created successfully")
# creation of Table with two fields
@app.route('/Table_creation', methods=['POST'])
def table_create():
    conn = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)
    cur = conn.cursor()
    cur.execute("create table db1.user (id INT NOT NULL, name VARCHAR(10), PRIMARY KEY (`id`))")
    return jsonify(status="success")
# Passing values for the table
@app.route('/Insert', methods=['POST'])
def insert():
    try:
        # _id = int(request.form['id'])
        # _name = request.form['name']
        conn = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)
        cur = conn.cursor()
        cur.execute('''INSERT INTO db1.user (id, name) VALUES (3, 'Aravind')''')
        conn.commit()
        return jsonify(id=cur.lastrowid)
    except BaseException as err:
        print(err)
# downloading the file in CSV format in the specified location
@app.route('/get_details', methods=['GET'])
def download():
    conn = connection.connect(host="localhost", user="root", passwd="root", use_pure=True)
    cur = conn.cursor()
    cur.execute("select * from db1.user")
    f = open("C:/Users/aravi/download.csv","w+")
    rows = cur.fetchall()
    f = open("C:/Users/aravi/download.csv","a")
    for i in rows:
        f.write(str(i).replace('(', "").replace(')', "") + "\n")
    f.close()
    conn.commit()
    return jsonify(status="success")
if __name__ == '__main__':
    app.run()

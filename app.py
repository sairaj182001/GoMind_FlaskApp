from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import uuid

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'gomind_flaskapp'

mysql = MySQL(app)


@app.route('/personal-details/<uuid:id>', methods=['GET'])
def personal_details(id):
    query = f"SELECT * FROM users WHERE id = '{id}'"
    cur = mysql.connection.cursor()
    cur.execute(query)
    fetchdata = cur.fetchone()
    return render_template('personal-details.html',data = fetchdata)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = uuid.uuid4()
        name = request.form['name']
        college = request.form['college']
        email = request.form['email']

        query = f"INSERT INTO users(id,username,college,email) VALUES('{id}','{name}','{college}','{email}')"
        cur = mysql.connection.cursor()
        cur.execute(query)
        mysql.connection.commit()
        cur.close()

        return redirect(f'/personal-details/{id}')
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)

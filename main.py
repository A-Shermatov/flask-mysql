from flask import Flask, render_template, request
from flask_mysqldb import MySQL



app = Flask(__name__, template_folder='Templates')

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shermatov_123'
app.config['MYSQL_DB'] = 'test01'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return render_template('index.html', f=firstName, l=lastName)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
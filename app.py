from flask import Flask, json, render_template, request
from flask.ext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

#MySQL configs
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '+r1t0n$k1k1b0uDiN'
app.config['MYSQL_DATABASE_DB'] = 'lacetest1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

 

@app.route('/search')
def search():
  _term1 = request.form['searchTerm1']
  _term2 = request.form['searchTerm2']
  _term3 = request.form['searchTerm3'] 

  if _term1:
    return json.dumps({'html':'<span>Valid input!</span>'})
  else:
    return json.dumps({'html':'<span>Please enter a search term.!</span>'})

@app.route("/")
def main():
  return render_template('index.html')

if __name__ == "__main__":
  app.run() 

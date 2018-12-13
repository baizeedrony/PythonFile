import cx_Oracle
from flask import Flask
#connection with oracle
con = cx_Oracle.connect("cc/cc@127.0.0.1/orcl")
# make a query

app = Flask(__name__)


@app.route('/')
def roni():
    cur = con.cursor()
    cur.execute("select service_name from cc_serviceinfo")
    return "<h1>{}</h1>".format(cur.fetchone()[0])
#con.close()


#if __name__ == '__main__':
app.run(host='127.0.0.1', port=4996, debug=True)

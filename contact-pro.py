from flask import*
import sqlite3
app=Flask(__name__)
@app.route('/')
@app.route('/home')
def index():
    return render_template('welcomepage.html')
connect=sqlite3.connect('contact.db')
connect.execute('CREATE TABLE IF NOT EXISTS contactlist(name TEXT,contact TEXT)')
@app.route('/entry',methods=['GET','POST'])
def entry():
    if request.method=='POST':
        name=request.form['name']
        contact=request.form['contact']
        with sqlite3.connect('contact.db')as cn:
            curr=cn.cursor()
            curr.execute('INSERT INTO contactlist(name,contact)VALUES(?,?)',(name,contact))
            cn.commit()
        return render_template('welcomepage.html')
    else:
        return render_template('contact.html')
@app.route('/view')
def viewing():
    with sqlite3.connect('contact.db')as conn:
        cur=conn.cursor()
        cur.execute('SELECT * FROM contactlist')
        datas=cur.fetchall()
    return render_template('viewpage.html',values=datas)
if __name__=='__main__':
    app.run(debug=True)






    

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

""" DECLARACION DE LA app y servidor """
app = Flask (__name__)

#Conexion a MySql
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='flaskcontacts'
mysql = MySQL(app)

#Configuracion
app.secret_key = 'millavesecreta'

""" Decorador """
@app.route('/')
def Inicio():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos')
    data = cur.fetchall()
    return render_template('index.html',contactos = data)

@app.route( '/add_contacto',methods=['POST'])
def add_contacto():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        social = request.form['social']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contactos (fullname,phone,email,social) VALUES (%s,%s,%s,%s)',(fullname,phone,email,social))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect (url_for('Inicio'))         

@app.route('/edit_contacto/<string:id>')
def get_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contactos WHERE id = %s',(id))
    data = cur.fetchall()
    return render_template('edita_contacto.html',contacto = data[0])

@app.route('/update/<id>')
def update_contacto(id):
    cur = mysql.connection.cursor()
    cur.execute(""" 
     UPDATE contactos
     SET fullname = %s
         phone = %s
         email= %s
        social= %s
    WHERE id = %s
    """,(fullname,phone,email,social,id))
    flash('Contacto actualizado satisfactoriamente')
    return redirect(url_for('Inicio'))        


@app.route('/delete_contacto/<string:id>')
def delete_contacto(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM contactos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado satisfactoriamente')
    return redirect(url_for('Inicio'))
if __name__ == "__main__":
    app.run(port= 3000,debug=True)

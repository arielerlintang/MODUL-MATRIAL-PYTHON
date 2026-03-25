from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector
from werkzeug.utils import secure_filename

app = Flask(__name__)

# koneksi database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="crud"
)

cursor = db.cursor(dictionary=True)

# folder upload
UPLOAD_FOLDER = 'static/img'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# route tampil data
@app.route('/')
def index():
    cursor.execute("SELECT * FROM produk")
    data = cursor.fetchall()
    return render_template("index.html", data=data)

# route tambah data
@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nama = request.form['nama_produk']
        jenis = request.form['jenis_produk']
        deskripsi = request.form['deskripsi_produk']

        foto = request.files['foto_produk']
        filename = secure_filename(foto.filename)

        if filename != '':
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        query = f"""
            INSERT INTO produk (nama_produk, deskripsi_produk, jenis_produk, foto_produk)
            VALUES ('{nama}', '{deskripsi}', '{jenis}', '{filename}')
        """
        cursor.execute(query)
        db.commit()

        return redirect(url_for('index'))

    return render_template('tambah.html')

# route edit data
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    cursor.execute(f"SELECT * FROM produk WHERE id_produk={id}")
    produk = cursor.fetchone()

    if request.method == 'POST':
        nama = request.form['nama_produk']
        jenis = request.form['jenis_produk']
        deskripsi = request.form['deskripsi_produk']

        foto = request.files['foto_produk']

        if foto.filename != '':
            filename = secure_filename(foto.filename)
            foto.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            filename = produk['foto_produk']

        query = f"""
            UPDATE produk
            SET nama_produk='{nama}',
                deskripsi_produk='{deskripsi}',
                jenis_produk='{jenis}',
                foto_produk='{filename}'
            WHERE id_produk={id}
        """
        cursor.execute(query)
        db.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', data=produk)

# route hapus data
@app.route('/hapus/<int:id>')
def hapus(id):
    cursor.execute(f"SELECT * FROM produk WHERE id_produk={id}")
    produk = cursor.fetchone()

    if produk:
        if produk['foto_produk']:
            path_foto = os.path.join(app.config['UPLOAD_FOLDER'], produk['foto_produk'])
            if os.path.exists(path_foto):
                os.remove(path_foto)

        cursor.execute(f"DELETE FROM produk WHERE id_produk={id}")
        db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

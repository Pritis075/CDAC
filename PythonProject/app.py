from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)  # Corrected __name__

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_generated = False
    if request.method == 'POST':
        data = request.form['data']
        if data:
            img = qrcode.make(data)
            img_path = os.path.join('static', 'qr.png')
            img.save(img_path)
            qr_generated = True
    return render_template('index.html', qr_generated=qr_generated)

@app.route('/download')
def download():
    img_path = os.path.join('static', 'qr.png')
    if os.path.exists(img_path):
        return send_file(img_path, as_attachment=True)
    return "QR Code not found.", 404

if __name__ == '__main__':
    app.run(debug=True)
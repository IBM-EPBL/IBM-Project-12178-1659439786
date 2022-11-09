from flask import Flask,render_template,request
 
app = Flask(__name__)
 
@app.route('/home')
def form():
    return render_template('home.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template('data.html',form_data = form_data)

app.run(host='localhost', port=5000)
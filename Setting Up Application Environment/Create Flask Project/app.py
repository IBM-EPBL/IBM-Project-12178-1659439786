from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/kowshika')
def home():
    return"Helloo Kowshika!!"

if __name__=="__main__":
    app.run(debug=True)
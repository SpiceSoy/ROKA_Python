from flask import Flask, render_template
from craw import GetRuliWebPS4

 
app = Flask(__name__)      

 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/<int:page>')
def GetPages():
  return render_tamplate('home.html',page)
 

 
if __name__ == '__main__':
  app.run(debug=True)
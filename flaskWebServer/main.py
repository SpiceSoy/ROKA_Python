from flask import Flask, render_template
from craw import GetCommicList

 
app = Flask(__name__)      

 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/<int:uid>')
def GetPages(uid):
  temp = GetCommicList(uid)
  commictTitle = temp[0]
  postList = temp[1]
  return render_template('home.html',commictTitle=commictTitle,postList=postList)

 
if __name__ == '__main__':
  app.run(debug=True)
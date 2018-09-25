from flask import Flask, render_template
from craw import GetRuliNews

 
app = Flask(__name__)      

 
@app.route('/')
def home():
  return render_template('home.html')

@app.route('/<int:page>')
def GetPages(page):
  postList = GetRuliNews(page)
  return render_template('home.html',postList=postList)

 
if __name__ == '__main__':
  app.run(debug=True)
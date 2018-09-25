from flask import Flask, render_template
from craw import GetRuliNews,GetRuliPost

 
app = Flask(__name__)      

 
@app.route('/')
def home():
  return render_template('redirect.html')

@app.route('/<int:page>')
def GetList(page):
  postList = GetRuliNews(page)
  return render_template('list.html',postList=postList,currentPage=page)
@app.route('/read/<int:id>')
def GetPost(id):
  post = GetRuliPost(id)
  return render_template('post.html',post=post)

 
if __name__ == '__main__':
  app.run(debug=True)
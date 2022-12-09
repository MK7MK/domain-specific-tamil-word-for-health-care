import wikipedia
from translate import Translator

from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/',methods=['POST'])
def login():
    user=request.form['nm']
    query=user
    cause_query="cause of "+user
    symp_query="symptoms of "+user
    rel_dis=user+" can cause what other disease"
    translator= Translator(to_lang="ta")
    
    wikipedia.set_lang("en")
    result1 = query
    result2 = wikipedia.summary(cause_query,sentences=2)
    result3 = wikipedia.summary(symp_query,sentences=2)
    result4 = wikipedia.search(rel_dis,results=5)
    translation4=[]
    translation1 = translator.translate(result1)
    translation2 = translator.translate(result2)
    translation3 = translator.translate(result3)
    for i in result4:      
        t = translator.translate(i)
        translation4.append(t)
    return render_template('index.html',res=translation1,res2=translation2,res3=translation3,res4=translation4)

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'hello %s' % guest



# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))

#     else:
#         return redirect(url_for('hello_guest', guest=name))


# app.add_url_rule('/','hello',hello_world())

if __name__ == '__main__':
    app.run()

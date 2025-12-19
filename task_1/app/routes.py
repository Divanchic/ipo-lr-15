from flask import Flask
from flask import request
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return """На данном сайте есть 2 функции:
        POST /json — принимает JSON {name, age} и выводит фразу.
        GET /multiply/<-a->/<-b-> — возвращает произведение чисел.
        """

@app.route('/hello/<name>')
def hello(name):
    return f"Привет {name}"

@app.route('/square/<int:number>')
def sqr(number):
    return f"{number**2}"

@app.route('/multiply/<a>/<b>')
def show_user_profile(a, b):
  return f'Произведение {int(a)*int(b)}'

data = {}

@app.route('/json', methods=['GET', 'POST'])
def authorization():
   if request.method == 'POST':
       Name = request.form.get('Name')
       Age = request.form.get('Age')
       data["name"] = Name
       data["age"] = Age
       json_data = json.dumps(data)
       python_dict = json.loads(json_data)
       return f"Здравствуй {python_dict["name"]}, вижу тебе уже {python_dict["age"]}"
   return '''
   <form method="POST">
   <div><label>Name: <input type="text" name="Name"></label></div>
   <div><label>Age: <input type="text" name="Age"></label></div>
   <input type="submit" value="Enter">
   </form>'''

if __name__ == '__main__':
    app.run(debug=True)
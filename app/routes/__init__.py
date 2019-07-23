from app import app, db
from flask import render_template, request, jsonify, make_response, json
from app.schemas.user import User

@app.route('/')
def index():
   return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/lfrom flask import jsongup')
def logup():
    return render_template('logup.html')

@app.route('/register', methods=['POST'])
def register():
   #print(request.value)
   #return jsonify({"status":200, "data": request.form})
   user = User(
      email = request.form['email'],
      password = request.form['password'],
      confirmed=False
   )

   try:
      print(user)
      db.session.add(user)
      db.session.commit()
      # db.session.add(user)
      return jsonify({"status":201, "data": request.form})
   except Exception as e:
      print(e)
      db.session.rollback()

      return jsonify({"status":402, "data": request.form, "error": json.dumps(e)})

   #return jsonify({"status":200, "data": request.form})
   # read the posted values from the UI
   # _name = request.form['inputName']
   # _email = request.form['inputEmail']
   # _password = request.form['inputPassword']
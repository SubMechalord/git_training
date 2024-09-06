from flask import Flask, render_template, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///users.db"
db=SQLAlchemy(app)

class Motor(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    model=db.Column(db.String(20),nullable=False)

    def __repr__(self):
        return f"Name : {self.name}"

# def handle_sql_exception(error):
#     # Log the error or perform any other necessary actions
#     print(f"SQLAlchemyError: {error}")
    
#     # Return a JSON response with error details
#     response = {
#         "error": "USERNAME ALREADY EXISTS!",
#         "message": str(error)

#     }
#     return jsonify(response), 500

@app.route("/",methods=['GET','POST'])
def index():
    # try:
    #     name=None
    #     model=None
    #     if request.method=="POST":
    #         name=request.form[""]
    #         password=request.form["password"]
    #         new_user=User(username=username,password=password)
    #         db.session.add(new_user)
    #         db.session.commit()
    #     return render_template("index.html", username=username,password=password)
    # except SQLAlchemyError as e:
    #     return handle_sql_exception(e)

    if request.method=="POST":
        button_value=request.form.get('button')
        if(button_value=="update"):
            return redirect("/update")
        
        else:
            return redirect("/rent")
    return render_template("index.html")

@app.route("/rent",methods=['GET','POST'])
def rent():
    name=None
    model=None
    if request.method=="POST":
        name=request.form["name"]
        model=request.form["model"]
        home=request.form.get('home-button')
        if(home=="home"):
            return redirect("/")
        new_motor=Motor(name=name,model=model)
        db.session.add(new_motor)
        db.session.commit()
    motors=Motor.query.order_by(Motor.id).all()
    return render_template("rent.html",name=name,model=model,motors=motors)

# WORK ON THIS!
# @app.route("/update",methods=['GET','POST'])
# def update():


# @app.route("/view",methods=['GET','POST'])
# def view():
#     motors=Motor.query.order_by(Motor.id).all()
#     home=request.form.get('home-button')
#     if(home=="home"):
#         return redirect("/")
#     return render_template("view.html",motors=motors)

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True,port=8000)

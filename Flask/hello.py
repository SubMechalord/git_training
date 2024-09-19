from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from flask import render_template_string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://arunvenkat:password@localhost:3306/users"
db = SQLAlchemy(app)

class Motor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"Name: {self.name}"

class Booked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    model = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return f"Name: {self.name}"

def handle_sql_exception(error):
    print(f"SQLAlchemyError: {error}")
    response = render_template_string('''
    <script type="text/javascript">
        alert("BIKE ALREADY EXISTS!\\n{{ error_message }}");
        window.history.back();
    </script>
    ''', error_message=str(error))
    return response, 500

def handle_exception(error1):
    print(f"Error: {error1}")
    response = render_template_string('''
    <script type="text/javascript">
        alert("NO VALUE GIVEN!\\n{{ error_message }}");
        window.history.back();
    </script>
    ''', error_message=str(error1))
    return response, 500

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        button_value = request.form.get('button')
        if button_value == "update":
            return redirect("/update")
        elif button_value == "rent":
            return redirect("/rent")
        else:
            return redirect("/booked")
    return render_template("index.html")

@app.route("/rent", methods=['GET', 'POST'])
def rent():
    try:
        name = None
        model = None
        if request.method == "POST":
            name = request.form["name"]
            model = request.form["model"]
            home = request.form.get('home-button')
            if home == "home":
                return redirect("/")
            if name == "" or model == "":
                raise Exception("Enter a value")
            new_motor = Motor(name=name, model=model)
            db.session.add(new_motor)
            db.session.commit()
        motors = Motor.query.order_by(Motor.id).all()
        return render_template("rent.html", name=name, model=model, motors=motors)
    except SQLAlchemyError as e:
        return handle_sql_exception(e)
    except Exception as e1:
        return handle_exception(e1)

@app.route("/update", methods=['GET', 'POST'])
def view():
    if request.method == "POST":
        home = request.form.get('home-button')
        if home == "home":
            return redirect("/")
        if 'book' in request.form:
            motor_id = request.form['book']
            motor_to_book = Motor.query.get(motor_id)
            if motor_to_book:
                new_booking = Booked(name=motor_to_book.name, model=motor_to_book.model)
                db.session.add(new_booking)
                db.session.delete(motor_to_book)
                db.session.commit()
                return redirect("/update")
        elif 'edit' in request.form:
            motor_id = request.form['edit']
            return redirect(url_for('edit', id=motor_id))
        elif 'delete' in request.form:
            motor_id1 = request.form['delete']
            motor_to_delete = Motor.query.get(motor_id1)
            if motor_to_delete:
                db.session.delete(motor_to_delete)
                db.session.commit()
                return redirect("/update")
    motors = Motor.query.order_by(Motor.id).all()
    return render_template("update.html", motors=motors)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == "POST":
        home = request.form.get('home-button')
        can = request.form.get('cancel-button')
        if home == "home":
            return redirect("/")
        if can == "cancel":
            return redirect("/update")
        try:
            item = Motor.query.get_or_404(id)
            if item.name == request.form["name"] and item.model == request.form["model"]:
                raise Exception("Same bike name entered! Provide different value")
            item.name = request.form["name"]
            item.model = request.form["model"]
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e2:
            return handle_sql_exception(e2)
    motors = Motor.query.order_by(Motor.id).all()
    return render_template("edit.html", motors=motors)

@app.route('/booked', methods=['GET', 'POST'])
def booked():
    if request.method == "POST":
        home = request.form.get('home-button')
        if home == "home":
            return redirect("/")
        if 'revert' in request.form:
            booked_id = request.form['revert']
            motor_to_revert = Booked.query.get(booked_id)
            if motor_to_revert:
                item = Motor(name=motor_to_revert.name, model=motor_to_revert.model)
                db.session.add(item)
                db.session.delete(motor_to_revert)
                db.session.commit()
                return redirect("/booked")
    booked = Booked.query.order_by(Booked.id).all()
    return render_template("booked.html", booked=booked)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)

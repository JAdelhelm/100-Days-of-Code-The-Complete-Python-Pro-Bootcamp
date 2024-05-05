from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select, update
import json
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

# # Standard Solution
# 
# @app.route("/random",methods=["GET"])
# def get_random_cafe():
#     from random import randint, choice
#     with app.app_context():
#         rows_number = db.session.query(Cafe).count()
#         random_pick = str(randint(1, rows_number))
#         sql_pick_cafe = db.session.get(Cafe, random_pick)
#         db.session.commit()
#         return jsonify(cafe={
#             "id": sql_pick_cafe.id,
#             "name": sql_pick_cafe.name,
#             "map_url": sql_pick_cafe.map_url,
#             "img_url": sql_pick_cafe.img_url,
#             "location": sql_pick_cafe.location,
#             "seats": sql_pick_cafe.seats,
#             "has_toilet": sql_pick_cafe.has_toilet,
#             "has_wifi": sql_pick_cafe.has_wifi,
#             "has_sockets": sql_pick_cafe.has_sockets,
#             "can_take_calls": sql_pick_cafe.can_take_calls,
#             "coffee_price": sql_pick_cafe.coffee_price,
#         })


# # Better Solution - watch to_dict function in class Cafe
@app.route("/random")
def get_random_cafe():
    from random import randint, choice
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = choice(all_cafes)
    #Simply convert the random_cafe data record to a dictionary of key-value pairs. 
    return jsonify(cafe=random_cafe.to_dict())

# # Get all cafes
@app.route("/all")
def get_all_cafes():
    results = db.session.execute(select(Cafe)).scalars().all()
    # print(results,"\n\n")
    return jsonify(cafes={f"Cafe {column.id}": column.to_dict() for column in results})

# # Search for cafes
@app.route("/search")
def search_for_cafes():
    # Gets the query parameters for loc
    query_location = request.args.get('loc')
    cafes_in_location = db.session.execute(db.select(Cafe).where(Cafe.location == query_location)).scalars().all()

    if cafes_in_location:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes_in_location])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404        
    


# HTTP POST - Create Record
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form
        new_cafe = Cafe(name=data['name'],
                        map_url=data['map_url'],
                        img_url=data["img_url"],
                        location=data["location"],
                        seats=data['seats'],
                        has_toilet=json.loads(data['has_toilet'].lower()),
                        has_wifi=json.loads(data['has_wifi'].lower()),
                        has_sockets=json.loads(data["has_sockets"].lower()),
                        can_take_calls=json.loads(data["can_take_calls"].lower()),
                        coffee_price=data["coffee_price"])  

        db.session.add(new_cafe)  # add record to database
        db.session.commit()  # commit add request
        
    return jsonify({"response": {"success": "Successfully add new data"}})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    # print(request.method)
    if request.method == 'PATCH':
        with app.app_context():
            cafe_to_update = Cafe.query.get(cafe_id)
            new_cafe_price = request.args.get('new_price')
            # print('\n')
            # print(request.args)
            # print(new_cafe_price)
            # print(cafe_to_pick.to_dict())
            # print('\n')
            if cafe_to_update:
                cafe_to_update.coffee_price = new_cafe_price
                db.session.commit()
                return jsonify(response={"success": "Successfully updated the price."}), 200
            else:
                return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    return redirect(url_for('home'))

@app.errorhandler(404)
def invalid_route(e):
    return jsonify(error={'Not found': 'Sorry a cafe with that id was not found in the database.'})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.method == "DELETE":
        with app.app_context():
            get_secret_key = request.args.get("api-key")
            if get_secret_key == "TopSecretAPIKey":
                cafe_to_delete = Cafe.query.get(cafe_id)
                if cafe_to_delete:
                    db.session.delete(cafe_to_delete)
                    db.session.commit()
                    return jsonify(response={"success": "Successfully deleted the cafe."}), 200
                else:
                    db.session.commit()
                    return jsonify(error={'Not found': 'Sorry a cafe with that id was not found in the database.'}), 404             

            
            

if __name__ == '__main__':
    app.run(debug=True)

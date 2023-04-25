from flask import Blueprint, jsonify, abort, make_response
class Crystals:
    def __init__(self, id, name, color, powers):
        self.id = id
        self.name = name
        self.color = color
        self.powers = powers
        
# create helper function whose single responsibility is to validate id passed in and reurn the instance of the crsytal that is found
def validate_crystal(crystal_id):
    try:
        crystal_id = int(crystal_id)
    except:
        abort(make_response({"message": f"{crystal_id} is not a valid type ({type(crystal_id)}. Must be an integer)"}, 400))
    for crystal in crystals:
        if crystal_id == crystal.id:
            return crystal
        
    abort(make_response({"message": f"crystal {crystal_id} does not exist"}, 404))

# create a list of crystals
crystals = [
    Crystals(1, "Ameythyst", "Purple", "Infinite knowledge and wisdom"),
    Crystals(2, "Tiger's Eye", "Golden brown", "Strength, power, confidence, intelligence, daring"),
    Crystals(3, "Rose Quartz", "Pink", "Love, compassion, partnership")
]

# make blueprint to group all crystal routes together
crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

# decorator to accept the following messages
# determine representation and send back some response
@crystal_bp.route("", methods=["GET"])

# create crystal list, add dictionary data represntaiton of the crystal to the list
def handle_crystals():
    crystal_response = []
    for crystal in crystals:
        crystal_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
            })
        
    return jsonify(crystal_response)
        
        
# reuse decorator to make another instance of the blueprint class, pass in the crystal_id endpoint
# use angle brackets to let flask know that what ever is inside <> will be used in view function after
# localhost:5000/crystals/1 to search for crystal with crystal_id 1
@crystal_bp.route("/<crystal_id>", methods=["GET"])
def handle_crystal(crystal_id):
    crystal = validate_crystal(crystal_id)
    
    # don't need to jsonify because it's already written as a json object (double quotes, key value pairs)
    return {
        "id": crystal.id,
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers
    }


    # impictely returns None if condition not met
    # this is NOT acceptable in flask
    # must add error handling
    
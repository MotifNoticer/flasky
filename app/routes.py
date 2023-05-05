from flask import Blueprint, jsonify, abort, make_response, request
from app.models.crystals import Crystal
from app import db

# make blueprint to group all crystal routes together
crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

@crystal_bp.route("", methods=["POST"])
def create_crystal():
    request_body = request.get_json()
    
    new_crystal = Crystal(
        name = request_body["name"],
        color = request_body["color"],
        powers = request_body["powers"]
    )
    
    db.session.add(new_crystal)
    db.session.commit()
    
    return {"message": f"Crystal {request_body['name']} was created."}, 201
# decorator to accept the following messages
# determine representation and send back some response
# @crystal_bp.route("", methods=["GET"])

# create crystal list, add dictionary data represntaiton of the crystal to the list
# def handle_crystals():
#     crystal_response = []
#     for crystal in crystals:
#         crystal_response.append({
#             "id": crystal.id,
#             "name": crystal.name,
#             "color": crystal.color,
#             "powers": crystal.powers
#             })
        
#     return jsonify(crystal_response)  

# reuse decorator to make another instance of the blueprint class, pass in the crystal_id endpoint
# use angle brackets to let flask know that what ever is inside <> will be used in view function after
# localhost:5000/crystals/1 to search for crystal with crystal_id 1
# @crystal_bp.route("/<crystal_id>", methods=["GET"])
# def handle_crystal(crystal_id):
#     crystal = validate_crystal(crystal_id)
    
#     # don't need to jsonify because it's already written as a json object (double quotes, key value pairs)
#     return {
#         "id": crystal.id,
#         "name": crystal.name,
#         "color": crystal.color,
#         "powers": crystal.powers
#        }


    # impictely returns None if condition not met
    # this is NOT acceptable in flask
    # must add error handling
    
@crystal_bp.route("", methods=["GET"])
def read_all_crystals():

        color_query = request.args.get("color")
        if color_query:
            crystals = Crystal.query.filter_by(color=color_query)
        else:
            Crystal.query.all()
                    
        
        crystals_response = []
        crystals = Crystal.query.all()
        
        for crystal in crystals:
            crystals_response.append({
                "id": crystal.id,
                "name": crystal.name,
                "color": crystal.color,
                "powers": crystal.powers
            })
            
        return jsonify(crystals_response)
    
    # Define a route for getting a single crystal
    # GET /crystals/<crystal_id>
    
    # Create decorator with crystal id endpoint
@crystal_bp.route("/<crystal_id>", methods=["GET"])
def read_one_crystal(crystal_id):
        # Query our db
    # crystal = Crystal.query.get(crystal_id)
    crystal = handle_crystal(crystal_id)
        
        # show a single crystal: return the crystal dictionary
    return {
                "id": crystal.id,
                "name": crystal.name,
                "color": crystal.color,
                "powers": crystal.powers
            }, 200
    
    
@crystal_bp.route("/<crystal_id>", methods=["PUT"])
def update_crystal(crystal_id):
    
    # crystal = (crystal_id)
    crystal = handle_crystal(crystal_id)
    request_body = request.get_json()
    
    crystal.name = request_body["name"]
    crystal.color = request_body["color"]
    crystal.powers = request_body["powers"]
    
    db.session.commit()
        
    return {
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        }, 200
    
@crystal_bp.route("/<crystal_id>", methods=["DELETE"])
def delete_crystal(crystal_id):
    # crystal = Crystal.query.get(crystal_id)
    # call validate crystal instead
    
    crystal = handle_crystal(crystal_id)
    
    db.session.delete(crystal)
    db.session.commit()
    
    return make_response(f"Crystal #{crystal.id} sucessfully deleted.")

def handle_crystal(crystal_id):
    request_body = request.get_json()
    try:
        crystal_id = int(crystal_id)
    except:
        abort(make_response({"message":f"crystal {crystal_id} invalid"}, 400))
        
    crystal = Crystal.query.get(crystal_id)
    
    if not crystal:
        abort(make_respone({"message": f"crystal {crystal_id} does not exist"}, 404))
        
    return crystal
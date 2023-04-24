from flask import Blueprint, jsonify
class Crystals:
    def __init__(self, id, name, color, powers):
        self.id = id
        self.name = name
        self.color = color
        self.powers = powers
        
# create a list of crystals
crystals = [
    Crystals(1, "Ameythyst", "Purple", "Infinite knowledge and wisdom"),
    Crystals(2, "Tiger's Eye", "Golden brown", "Strength, power, confidence, intelligence, daring"),
    Crystals(3, "Rose Quartz", "Pink", "Love, compassion, partnership")
]

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

@crystal_bp.route("", methods=["GET"])

def hande_crystals():
    crystal_response = []
    for crystal in crystals:
        crystal_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
            })
        
        
    return jsonify(crystal_response)
        
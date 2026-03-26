from flask import Blueprint, request, jsonify
from models.contract_model import Contract
from services.validator_service import validate_data

validation_bp = Blueprint("validation", __name__)


@validation_bp.route("/<int:contract_id>", methods=["POST"])
def validate_request(contract_id):
    try:
        contract = Contract.query.get(contract_id)

        if not contract:
            return jsonify({"error": "Contract not found"}), 404

        data = request.get_json()

        result = validate_data(contract.schema, data)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": "Validation failed",
            "details": str(e)
        }), 500
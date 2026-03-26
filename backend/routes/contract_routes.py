from flask import Blueprint, request, jsonify
from extensions import db
from models.contract_model import Contract

contract_bp = Blueprint("contracts", __name__)


@contract_bp.route("", methods=["POST"])
def create_contract():
    try:
        data = request.get_json()

        # Validate input
        if not data:
            return jsonify({"error": "Request body must be JSON"}), 400

        name = data.get("name")
        schema = data.get("schema")

        if not name or not schema:
            return jsonify({"error": "name and schema are required"}), 400

        # Create contract
        contract = Contract(
            name=name,
            schema=schema
        )

        db.session.add(contract)
        db.session.commit()

        return jsonify({
            "id": contract.id,
            "name": contract.name,
            "schema": contract.schema,
            "version": contract.version,
            "created_at": contract.created_at
        }), 201

    except Exception as e:
        return jsonify({
            "error": "Something went wrong",
            "details": str(e)
        }), 500
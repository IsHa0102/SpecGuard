from flask import Blueprint, request, jsonify
from services.ai_service import generate_test_cases

ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/generate-tests", methods=["POST"])
def generate_tests():
    try:
        data = request.get_json()
        schema = data.get("schema")

        if not schema:
            return jsonify({"error": "Schema is required"}), 400

        result = generate_test_cases(schema)

        return jsonify({
            "ai_output": result
        }), 200

    except Exception as e:
        return jsonify({
            "error": "AI generation failed",
            "details": str(e)
        }), 500
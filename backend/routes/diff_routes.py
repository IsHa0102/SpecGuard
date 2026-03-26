from flask import Blueprint, request, jsonify
from services.diff_service import diff_schemas

diff_bp = Blueprint("diff", __name__)


@diff_bp.route("", methods=["POST"])
def get_diff():
    try:
        data = request.get_json()

        old_schema = data.get("old_schema")
        new_schema = data.get("new_schema")

        if not old_schema or not new_schema:
            return jsonify({"error": "Both old_schema and new_schema are required"}), 400

        result = diff_schemas(old_schema, new_schema)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": "Diff failed",
            "details": str(e)
        }), 500
import re

def validate_data(schema, data):
    errors = []

    for field, rules in schema.items():
        value = data.get(field)

        # Required check
        if rules.get("required") and field not in data:
            errors.append(f"{field} is required")
            continue

        # Skip if not present
        if value is None:
            continue

        field_type = rules.get("type")

        # Type checks
        if field_type == "string" and not isinstance(value, str):
            errors.append(f"{field} must be a string")

        elif field_type == "integer" and not isinstance(value, int):
            errors.append(f"{field} must be an integer")

        # Email format check
        if rules.get("format") == "email":
            if not re.match(r"[^@]+@[^@]+\.[^@]+", str(value)):
                errors.append(f"{field} must be a valid email")

        # Min value check
        if "min" in rules:
            if isinstance(value, int) and value < rules["min"]:
                errors.append(f"{field} must be >= {rules['min']}")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
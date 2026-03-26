def diff_schemas(old_schema, new_schema):
    old_fields = set(old_schema.keys())
    new_fields = set(new_schema.keys())

    added = list(new_fields - old_fields)
    removed = list(old_fields - new_fields)

    modified = []

    for field in old_fields & new_fields:
        if old_schema[field] != new_schema[field]:
            modified.append(field)

    return {
        "added": added,
        "removed": removed,
        "modified": modified
    }
# AI Prompt Guidelines — SpecGuard

## Purpose
Generate structured test cases from API schemas.

---

## Core Prompt Template

Given this API schema:
{schema}

Generate:
1. Valid test cases
2. Invalid test cases (edge cases, wrong types, missing fields)

Return ONLY JSON in the format:
{
  "valid_cases": [...],
  "invalid_cases": [...]
}

---

## Rules

- Output must be valid JSON
- Do not include explanations
- Do not hallucinate fields not present in schema
- Include edge cases (missing fields, wrong types, boundary values)
- Keep test cases realistic and minimal

---

## Example

Input Schema:
{
  "age": {"type": "integer", "min": 18}
}

Expected Output:
{
  "valid_cases": [{"age": 25}],
  "invalid_cases": [{"age": 10}, {"age": "abc"}]
}
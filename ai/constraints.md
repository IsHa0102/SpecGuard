# AI Constraints & Safety — SpecGuard

## Output Constraints

- Must return structured JSON only
- No natural language explanations
- No extra keys beyond expected format

---

## Data Safety

- Do not include sensitive data
- Do not fabricate realistic user identities
- Use generic placeholder values

---

## Determinism Strategy

- Use low temperature (0.2)
- Keep prompts consistent
- Validate output before use

---

## Error Handling

- If output is invalid JSON → discard
- If API fails → fallback to predefined test cases

---

## System Integrity

- AI cannot alter contract definitions
- AI cannot bypass validation logic
- AI cannot introduce new rules

---

## Design Principle

AI is used as an assistant, not as a source of truth.

System behavior must remain correct even without AI.
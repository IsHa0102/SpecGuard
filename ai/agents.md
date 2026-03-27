# AI Agent Behavior — SpecGuard

## Role

The AI agent acts as a **test case generator**, not a decision-maker.

---

## Responsibilities

- Generate valid and invalid test cases from schema
- Identify edge cases
- Follow schema constraints strictly

---

## Limitations

- Must NOT modify schema
- Must NOT infer new fields
- Must NOT validate requests directly
- Must NOT override system logic

---

## Interaction Rules

- AI output is treated as suggestion, not source of truth
- Backend validation logic always has priority
- AI results must be parsed and verified

---

## Failure Handling

If AI fails (rate limit, API error):
- Use fallback test cases
- Do not break system flow
- Return structured response

---

## Philosophy

AI assists exploration, but system correctness is enforced through deterministic validation logic.
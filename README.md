# SpecGuard 🚀  
### Contract-Driven API Validation System

---

## 🧠 Overview

SpecGuard is a small, focused system designed to ensure APIs remain **correct, predictable, and safe** as they evolve.

It enforces structured contracts, validates incoming data, detects schema changes, and uses AI to assist with generating test cases.

The goal is not feature quantity, but **clarity, correctness, and resilience**.

---

## ❗ Problem

In many systems:

- APIs accept invalid or inconsistent data  
- Contracts between frontend and backend are unclear  
- Schema changes silently break existing behavior  
- Bugs are discovered late and are hard to trace  

This leads to fragile systems that degrade over time.

---

## 💡 Solution

SpecGuard introduces a **contract-first approach**:

- Define API rules explicitly  
- Validate all incoming requests against those rules  
- Detect changes in schema before they cause issues  
- Use AI to generate test cases and explore edge cases  

---

## ⚙️ Core Features

### 🧾 Contract Management
- Define API schemas using simple JSON rules  
- Store contracts persistently  
- Acts as the source of truth for validation  

---

### 🧠 Request Validation
- Validates incoming payloads against defined contracts  
- Enforces:
  - Required fields  
  - Data types  
  - Constraints (e.g., min values)  
  - Format rules (e.g., email)  

- Prevents invalid states from entering the system  

---

### 🔍 Schema Diff (Change Detection)
- Compares two versions of a schema  
- Detects:
  - Added fields  
  - Removed fields  
  - Modified rules  

- Helps identify **breaking changes early**

---

### 🤖 AI Test Case Generation
- Generates valid and invalid test cases from schema  
- Helps uncover edge cases quickly  

**Important:**
- AI is used as an assistant, not a dependency  
- System remains functional even if AI fails (fallback implemented)  

---

## 🏗️ Architecture

The system follows a simple and predictable structure:
Route → Service → Model


### 🔹 Routes
- Handle HTTP requests and responses  
- No business logic  

### 🔹 Services
- Core logic (validation, diff, AI handling)  
- Reusable and testable  

### 🔹 Models
- Database representation (contracts)  
- Managed via SQLAlchemy  

---

## 🧱 Tech Stack

### Backend
- Python (Flask)  
- SQLAlchemy (ORM)  
- SQLite (database)  

### Frontend
- React (basic UI for interaction)  

### AI
- OpenAI API (with fallback support)  

---

## 🛡️ Design Principles

- **Simplicity over cleverness**  
- **Explicit validation over implicit behavior**  
- **Fail early and visibly**  
- **Separation of concerns**  
- **System should remain understandable as it evolves**  

---

## 🔐 Interface Safety

- Input validation prevents invalid data  
- Clear error messages for debugging  
- No silent failures  

---

## 🔄 Change Resilience

- Schema diff prevents unnoticed breaking changes  
- Validation ensures consistency across updates  

---

## 🧪 Verification

- Validation logic ensures correctness  
- API responses are deterministic  
- AI output is controlled and optional  

---

## 👀 Observability

- Clear error responses  
- Failures are visible and diagnosable  
- No hidden system behavior  

---

## 🤖 AI Usage (Controlled)

AI is used specifically for:

- Generating test cases from schema  
- Exploring edge cases  

### Constraints:
- Output must be structured  
- Prompts restrict hallucination  
- Fallback ensures system stability  

---

## ⚠️ Tradeoffs

- Schema is intentionally simple (not full JSON Schema support)  
- No authentication (out of scope for prototype)  
- AI output depends on prompt quality  
- UI is minimal and functional, not design-focused  

---

## 🚀 How to Run

### 1. Clone repository
git clone <your-repo-url>
cd specguard

### 2. Backend setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

### 3. Frontend setup
cd frontend
npm install
npm start

## 🧪 Example API Usage

### Create Contract
POST /contracts

### Validate Request
POST /validate/<contract_id>

### Schema Diff
POST /diff

### Generate AI Test Cases
POST /ai/generate-tests

## 📂 Project Structure
specguard/
backend/
routes/
services/
models/
database/
frontend/
src/pages/
ai/
prompts.md
agents.md
README.md


---

## 🔮 Future Improvements

- Schema versioning & history tracking  
- More expressive validation rules  
- Authentication & access control  
- Better UI/UX  
- Integration with CI/CD pipelines  

---

## 🎯 Key Insight

The focus of this system is not feature count, but:

> Building a system that remains **correct, understandable, and resilient** as it evolves.

---

## 👤 Author

Isha Sharma
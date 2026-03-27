import React, { useState } from "react";

function DiffViewer() {
  const [oldSchema, setOldSchema] = useState("");
  const [newSchema, setNewSchema] = useState("");
  const [result, setResult] = useState(null);
  const [aiResult, setAiResult] = useState(null);

  // 🔍 DIFF FUNCTION
  const handleDiff = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/diff", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          old_schema: JSON.parse(oldSchema),
          new_schema: JSON.parse(newSchema),
        }),
      });

      const data = await res.json();
      setResult(data);
    } catch (error) {
      alert("Invalid JSON or server error");
    }
  };

  // 🤖 AI TEST GENERATION
  const handleAI = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/ai/generate-tests", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          schema: JSON.parse(newSchema),
        }),
      });

      const data = await res.json();
      setAiResult(data);
    } catch (error) {
      alert("AI request failed");
    }
  };

  return (
    <div>
      <h2 style={{ marginTop: "20px" }}>Schema Diff 🔍</h2>

      <div style={{ display: "flex", gap: "20px" }}>
        <textarea
          rows="8"
          cols="40"
          placeholder="Old Schema"
          value={oldSchema}
          onChange={(e) => setOldSchema(e.target.value)}
        />

        <textarea
          rows="8"
          cols="40"
          placeholder="New Schema"
          value={newSchema}
          onChange={(e) => setNewSchema(e.target.value)}
        />
      </div>

      <br />

      <button onClick={handleDiff}>Compare</button>{" "}
      <button onClick={handleAI}>Generate AI Tests</button>

      <hr />

      {/* 🔍 DIFF RESULT */}
      {result && (
        <div>
          <h3>Diff Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}

      {/* 🤖 AI RESULT */}
      {aiResult && (
        <div>
          <h3>AI Generated Test Cases:</h3>
          <pre>{JSON.stringify(aiResult, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default DiffViewer;
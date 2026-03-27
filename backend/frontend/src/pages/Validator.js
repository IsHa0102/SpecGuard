import React, { useState } from "react";

function Validator() {
  const [contractId, setContractId] = useState("");
  const [payload, setPayload] = useState("");
  const [result, setResult] = useState(null);

  const handleValidate = async () => {
    const res = await fetch(`http://127.0.0.1:5000/validate/${contractId}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: payload,
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div>
      <h2>Validate Request</h2>

      <input
        placeholder="Contract ID"
        value={contractId}
        onChange={(e) => setContractId(e.target.value)}
      />

      <br /><br />

      <textarea
        rows="10"
        cols="50"
        placeholder="Enter JSON payload"
        value={payload}
        onChange={(e) => setPayload(e.target.value)}
      />

      <br /><br />

      <button onClick={handleValidate}>Validate</button>

      {result && (
        <pre>{JSON.stringify(result, null, 2)}</pre>
      )}
    </div>
  );
}

export default Validator;
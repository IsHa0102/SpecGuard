import React, { useState } from "react";

function ContractBuilder() {
  const [name, setName] = useState("");
  const [schema, setSchema] = useState("");

  const handleSubmit = async () => {
    const res = await fetch("http://127.0.0.1:5000/contracts", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name,
        schema: JSON.parse(schema),
      }),
    });

    const data = await res.json();
    alert(JSON.stringify(data, null, 2));
  };

  return (
    <div>
      <h2>Create Contract</h2>

      <input
        placeholder="Contract Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <br /><br />

      <textarea
        rows="10"
        cols="50"
        placeholder='Paste schema JSON here'
        value={schema}
        onChange={(e) => setSchema(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit}>Create</button>
    </div>
  );
}

export default ContractBuilder;
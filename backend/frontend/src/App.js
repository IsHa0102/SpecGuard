import React, { useState } from "react";
import ContractBuilder from "./pages/ContractBuilder";
import Validator from "./pages/Validator";
import DiffViewer from "./pages/DiffViewer";

function App() {
  const [page, setPage] = useState("contract");

  return (
    <div style={{ padding: 20 }}>
      <h1>SpecGuard 🚀</h1>

      <button onClick={() => setPage("contract")}>Create Contract</button>
      <button onClick={() => setPage("validate")}>Validate</button>
      <button onClick={() => setPage("diff")}>Diff</button>

      <hr />

      {page === "contract" && <ContractBuilder />}
      {page === "validate" && <Validator />}
      {page === "diff" && <DiffViewer />}
    </div>
  );
}

export default App;
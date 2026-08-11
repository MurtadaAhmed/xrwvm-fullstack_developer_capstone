import React from "react";
import { Routes, Route } from "react-router-dom";
// Import your existing Login panel [1, 2]
import LoginPanel from "./components/Login/Login";
// Import your new Register component [3, 4]
import Register from "./components/Register/Register";

function App() {
  return (
    <Routes>
      {/* Route for logging in [5] */}
      <Route path="/login" element={<LoginPanel />} />
      
      {/* Route for signing up / registration [4] */}
      <Route path="/register" element={<Register />} />
    </Routes>
  );
}

export default App;


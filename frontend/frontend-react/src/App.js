import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import TestEntryForm from "./pages/TestEntryForm";

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path="/test-form" element={<TestEntryForm />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;

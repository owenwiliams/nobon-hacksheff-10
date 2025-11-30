import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import TestEntryForm from "./pages/TestEntryForm";
import Sidebar from "./components/SidebarBody";
import SidebarButton from "./components/SidebarButton";

function App() {
  return (
    /*<Router>
      <Layout>
        <Routes>
          <Route path="/test-form" element={<TestEntryForm />} />
        </Routes>
      </Layout>
    </Router>*/

    <div className="webpage">
      <Sidebar />
      
      <div className="main">
        {/* page content */}
        <SidebarButton />
      </div>
    </div>

  );
}

export default App;

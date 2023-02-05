import "bootstrap/dist/css/bootstrap.min.css"
import "./App.css"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import OpeningPage from "./components/OpeningPage"
import Dashboard from "./components/Dashboard"

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<OpeningPage />} />
        <Route path="dashboard" element={<Dashboard/>} />
      </Routes>
    </BrowserRouter>
  )
}

export default App

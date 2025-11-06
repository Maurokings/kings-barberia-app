
import React from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import RegistrarCorte from './pages/RegistrarCorte'
import RegistrarGasto from './pages/RegistrarGasto'
import './index.css'

function App(){
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Login/>} />
        <Route path='/dashboard' element={<Dashboard/>} />
        <Route path='/registrar-corte' element={<RegistrarCorte/>} />
        <Route path='/registrar-gasto' element={<RegistrarGasto/>} />
      </Routes>
    </BrowserRouter>
  )
}

createRoot(document.getElementById('root')).render(<App/>)

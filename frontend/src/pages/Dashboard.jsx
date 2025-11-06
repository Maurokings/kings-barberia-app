
import React from 'react'
import { Link } from 'react-router-dom'

export default function Dashboard(){
  return (
    <div style={{padding:20}}>
      <header style={{display:'flex', alignItems:'center', justifyContent:'space-between'}}>
        <img src="/assets/logo-kings.png" alt="logo" style={{height:60}} />
        <div>
          <Link to="/registrar-corte" style={{marginRight:10}}>Registrar Corte</Link>
          <Link to="/registrar-gasto">Registrar Gasto</Link>
        </div>
      </header>
      <main style={{marginTop:20}}>
        <h1>Dashboard - Resumen rápido</h1>
        <p>Aquí se listarán totales diarios, por barbero y más (la UI está lista para conectar con la API).</p>
      </main>
    </div>
  )
}

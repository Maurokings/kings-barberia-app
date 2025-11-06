
import React, {useEffect, useState} from 'react'
import axios from 'axios'
export default function RegistrarCorte(){
  const [barberos, setBarberos] = useState([])
  const [servicios, setServicios] = useState([])
  const [form, setForm] = useState({barbero_id:'', servicio_id:'', monto:'', metodo_pago:'efectivo'})

  useEffect(()=>{ fetchData() },[])
  async function fetchData(){
    try{
      const b = await axios.get((import.meta.env.VITE_API_URL || '') + '/barberos')
      const s = await axios.get((import.meta.env.VITE_API_URL || '') + '/servicios')
      setBarberos(b.data); setServicios(s.data)
    }catch(err){ console.error(err) }
  }
  async function submit(e){
    e.preventDefault()
    try{
      await axios.post((import.meta.env.VITE_API_URL || '') + '/cortes', {
        barbero_id: parseInt(form.barbero_id),
        servicio_id: parseInt(form.servicio_id),
        monto: parseFloat(form.monto),
        metodo_pago: form.metodo_pago
      })
      alert('Corte registrado')
    }catch(err){ alert('Error al registrar') }
  }
  return (
    <div style={{padding:20}}>
      <h2>Registrar Corte</h2>
      <form onSubmit={submit}>
        <div>
          <label>Barbero</label><br/>
          <select value={form.barbero_id} onChange={e=>setForm({...form, barbero_id:e.target.value})}>
            <option value=''>Seleccionar</option>
            {barberos.map(b=> <option key={b.id} value={b.id}>{b.nombre}</option>)}
          </select>
        </div>
        <div>
          <label>Servicio</label><br/>
          <select value={form.servicio_id} onChange={e=>setForm({...form, servicio_id:e.target.value})}>
            <option value=''>Seleccionar</option>
            {servicios.map(s=> <option key={s.id} value={s.id}>{s.nombre} - {s.precio_sugerido}</option>)}
          </select>
        </div>
        <div>
          <label>Monto</label><br/>
          <input value={form.monto} onChange={e=>setForm({...form, monto:e.target.value})} />
        </div>
        <div>
          <label>Metodo de pago</label><br/>
          <select value={form.metodo_pago} onChange={e=>setForm({...form, metodo_pago:e.target.value})}>
            <option value='efectivo'>Efectivo</option>
            <option value='transferencia'>Transferencia</option>
          </select>
        </div>
        <button style={{marginTop:10, background:'#C9A227', padding:8, border:'none'}}>Registrar</button>
      </form>
    </div>
  )
}

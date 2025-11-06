
import React, {useState} from 'react'
import axios from 'axios'
export default function RegistrarGasto(){
  const [form, setForm] = useState({descripcion:'', monto:'', metodo_pago:'efectivo'})
  async function submit(e){
    e.preventDefault()
    try{
      await axios.post((import.meta.env.VITE_API_URL || '') + '/gastos', form)
      alert('Gasto registrado')
    }catch(err){ alert('Error al registrar gasto') }
  }
  return (
    <div style={{padding:20}}>
      <h2>Registrar Gasto</h2>
      <form onSubmit={submit}>
        <div>
          <label>Descripción</label><br/>
          <input value={form.descripcion} onChange={e=>setForm({...form, descripcion:e.target.value})} />
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

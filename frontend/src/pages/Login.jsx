
import React, {useState} from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

export default function Login(){
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const navigate = useNavigate()

  async function submit(e){
    e.preventDefault()
    try{
      const res = await axios.post((import.meta.env.VITE_API_URL || '') + '/auth/login', {username, password})
      localStorage.setItem('token', res.data.access_token)
      navigate('/dashboard')
    }catch(err){
      alert('Usuario o contraseña inválidos')
    }
  }

  return (
    <div style={{display:'flex', minHeight:'100vh', alignItems:'center', justifyContent:'center', background:'#000', color:'#fff'}}>
      <div style={{width:360, padding:20, background:'#111', borderRadius:8}}>
        <img src="/assets/logo-kings.png" alt="KINGS" style={{width:'100%', marginBottom:20}}/>
        <h2 style={{color:'#C9A227'}}>Ingresar</h2>
        <form onSubmit={submit}>
          <div style={{marginBottom:10}}>
            <input value={username} onChange={e=>setUsername(e.target.value)} placeholder="Usuario" style={{width:'100%', padding:8}} />
          </div>
          <div style={{marginBottom:10}}>
            <input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="Contraseña" style={{width:'100%', padding:8}} />
          </div>
          <button style={{width:'100%', padding:10, background:'#C9A227', border:'none', color:'#000'}}>Entrar</button>
        </form>
      </div>
    </div>
  )
}

import React from 'react'

export const form_register = () => {
  return (
    <div className='div-form'>
        <form action="/submit_registration" method='post'>

            <label className='first-name-label' htmlFor="first-name-input">Nombre:</label>
            <input type="text" id='first-name-input' name='first-name-input' required />
            
            <label className='last-name-label' htmlFor="last-name-input">Apellido:</label>
            <input type="text" id='last-name-input' name='last-name-input' required />

            <label className='email-label' htmlFor="email-input">e-mail</label>
            <input type="email" id='email' name='email' required />

            <input type="submit" value='Registrarse' />
        </form>
    </div>
  )
}

export default form_register
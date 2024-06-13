import { useState } from 'react'
import { Container } from '@mui/material';
import { Formik } from 'formik'
import * as yup from 'yup'

function Auth({ setUser }) {
    const [signup, setSignup] = useState(true)

    const signupSchema = yup.object().shape({
        username: yup.string().min(5, 'Username too Short!').max(15, 'Username too Long!'),
        password: yup.string().min(5, 'Password too Short!').max(15, 'Password too Long!'),
        passwordConfirmation: yup.string().oneOf([yup.ref('password')], 'Passwords must match')
    })
    const loginSchema = yup.object().shape({
        username: yup.string().required('username required'),
        password: yup.string().required('password required')
    })

    function toggleSignup() {
        setSignup((currentSignup) => !currentSignup)
    }

    const handleSubmit = (values) => {
        const endpoint = signup ? '/signup' : '/login'
        fetch(endpoint, {
            method: 'POST',
            headers: {
                "Content-Type": 'application/json'
            },
            body: JSON.stringify(values)
        }).then((resp) => {
            if (resp.ok) {
                resp.json().then((user) => {
                    setUser(user)
                    // navigate into site
                })
            } else { 
                
                console.log('errors? handle them')
            }
        })
    }

    return (
        <Container maxWidth='sm'>
            <button onClick={toggleSignup}>{signup ? 'Login instead!' : 'Register for an account'}</button>
            <Formik
                initialValues={{
                    username: '',
                    password: '',
                    passwordConfirmation: ''
                }}
                validationSchema={signup ? signupSchema : loginSchema}
                onSubmit={handleSubmit}
            >   
                {({handleSubmit, values, handleChange}) => (
                    <form className='form' onSubmit={handleSubmit}>
                        <label htmlFor='username'>Username:</label>
                        <input 
                            id="username" 
                            name="username" 
                            placeholder='Username'
                            required
                            value={values.username}
                            onChange={handleChange}
                        />
                        
                        <label htmlFor='password'>Password:</label>
                        <input 
                            id='password' 
                            name='password' 
                            type='password' 
                            placeholder='Password' 
                            value={values.password}
                            onChange={handleChange}
                        />
                    
                        {signup && <>
                            <label htmlFor='passwordConfirmation'>Password Confirmation:</label>
                            <input 
                                id="passwordConfirmation" 
                                name="passwordConfirmation"
                                type='password' 
                                placeholder="Password Confirmation" 
                                value={values.passwordConfirmation}
                                onChange={handleChange}
                            />
                        </>}
                        <button type="submit">Submit</button>
                    </form>
                )}
            </Formik>
        </Container>
    )
}

export default Auth;
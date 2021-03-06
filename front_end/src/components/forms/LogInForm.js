/**
 * Created by techbk on 20/03/2016.
 */


import React, {Component} from 'react'
import {reduxForm} from 'redux-form'
import { login } from '../../actions'
//
//const submit = (values, dispatch) => {
//  return new Promise((resolve, reject) => {
//    setTimeout(() => {
//      if (!['john', 'paul', 'george', 'ringo'].includes(values.username)) {
//        reject({username: 'User does not exist', _error: 'Login failed!'});
//      } else if (values.password !== 'redux-form') {
//        reject({password: 'Wrong password', _error: 'Login failed!'});
//      } else {
//        dispatch(showResults(values));
//        resolve();
//      }
//    }, 1000); // simulate server latency
//  });
//};

class LogInForm extends Component {
	render() {
		const {fields: {login, password1, password2}, handleSubmit, submitting} = this.props
		return (
			<form onSubmit={handleSubmit}>
				<div>
					<label>User Name</label>
					<input type="text" placeholder="First Name" {...login}/>
				</div>
				<div>
					<label>Password</label>
					<input type="password" placeholder="password" {...password1}/>
				</div>
				<div>
					<label>Re-Password</label>
					<input type="password" placeholder="password comfirm" {...password2}/>
				</div>
				<button type="submit">Sign Up!</button>
			</form>
		)
	}
}

SignUpForm = reduxForm({
		form: 'signin',
		fields: ['login', 'password1', 'password2']
	},
	undefined,
	{
		onSubmit: signin
	}
	)(SignUpForm)

export default LogInForm
/**
 * Created by techbk on 19/03/2016.
 */

import React, { Component, ProTypes } from 'react'
import { connect } from 'react-redux'
import { push } from 'react-router-redux'
import SignUpForm from '../components/forms/SignUpForm'
import { PageHeader } from 'react-bootstrap'

class SignUpPage extends Component {

	render(){
		return (
			<div>
				<PageHeader> Sign Up!!!</PageHeader>
				<div>
					<SignUpForm/>
				</div>
			</div>
		)
	}
}

export default SignUpPage

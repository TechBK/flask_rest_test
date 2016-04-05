/**
 * Created by techbk on 18/03/2016.
 */

import React, { Component } from 'react'
import { connect } from 'react-redux'
import { Link } from 'react-router'
import NavbarInstance from '../components/layout/Navbars'
import { Grid, Row, Col } from 'react-bootstrap'


export default class Layout extends Component {
	render(){
		return (
			<Grid fluid>
				<NavbarInstance/>
				<Row className="show-grid">
					<Col lg={6} sm={6} md={6} mdOffset={4} smOffset={3} lgOffset={2}>
						{this.props.children}
					</Col>
				</Row>
			</Grid>
		)
	}
}

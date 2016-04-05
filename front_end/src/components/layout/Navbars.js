/**
 * Created by techbk on 04/04/2016.
 */

import React, { Component } from 'react'
import { LinkContainer, IndexLinkContainer } from 'react-router-bootstrap'
import { Navbar, Nav,  NavItem, NavbarBrand, MenuItem, NavDropdown, Button, Input } from 'react-bootstrap'

export default class NavbarInstance extends Component  {
	render(){
		return (
			<Navbar staticTop>
				<Navbar.Header>
					<IndexLinkContainer to="/">
						<Navbar.Brand>
							<a href="#">Notes App</a>
						</Navbar.Brand>
					</IndexLinkContainer>
					<Navbar.Toggle />
				</Navbar.Header>
				<Navbar.Collapse>
					<Nav>
						<NavItem eventKey={1} href="#">Link</NavItem>
						<NavItem eventKey={2} href="#">Link</NavItem>
						<NavDropdown eventKey={3} title="Dropdown" id="basic-nav-dropdown">
							<MenuItem e	ventKey={3.1}>Action</MenuItem>
							<MenuItem eventKey={3.2}>Another action</MenuItem>
							<MenuItem eventKey={3.3}>Something else here</MenuItem>
							<MenuItem divider />
							<MenuItem eventKey={3.3}>Separated link</MenuItem>
						</NavDropdown>
					</Nav>
					<Nav pullRight>
						<Navbar.Form pullLeft>
							<Input type="text" placeholder="Search"/>
							{' '}
							<Button type="submit">Submit</Button>
						</Navbar.Form>
						<LinkContainer to="/login/"><MenuItem>Log In</MenuItem></LinkContainer>
						<LinkContainer to="/signup/"><MenuItem>Sign Up</MenuItem></LinkContainer>
					</Nav>
				</Navbar.Collapse>
			</Navbar>
		)
	}
}


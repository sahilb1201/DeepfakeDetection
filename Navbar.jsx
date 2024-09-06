import React from 'react'
import '../Navbar/Navbar.css'
import logo from '../../assets/main-logo.png'
import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <div className="navbar">
        <div class="logo">
            <img src={logo} alt="logo" />
            <div class="logo-text">
                <div class="main-text">DEEPGUARDIANS</div>
                <div class="sub-text">UNMASKING DEEPFAKES</div>
            </div>
        </div>
        <div class="nav-links">
          <ul>
            <li><Link style={{ textDecoration: 'none', color: 'white'}} to='/'>Home</Link></li>
            <li><Link style={{ textDecoration: 'none', color: 'white'}} to='/upload'>Detect</Link></li>
            <li><Link style={{ textDecoration: 'none', color: 'white'}} to='/about'>About</Link></li>
          </ul>
        </div>
        <Link to='/login'><button class="login-button">Login</button></Link>
    </div>
  )
}

export default Navbar
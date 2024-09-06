import React from 'react'
import '../GetStarded/GetStarded.css'
import { Link } from 'react-router-dom'

const GetStarded = () => {
  return (
    <div>
        <Link to='/upload'><button className="get-started-button">Get Started</button></Link>
    </div>
  )
}

export default GetStarded
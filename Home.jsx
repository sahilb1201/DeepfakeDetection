import React from 'react'
import Hero from '../Components/Hero/Hero'
import Description from '../Components/Description/Description'
import Desc from '../Components/Desc/Desc'
import GetStarded from '../Components/GetStarded/GetStarded'

const Home = () => {
  return (
    <div>
        <Hero />
        <GetStarded />
        <Description />
        <Desc />
    </div>
  )
}

export default Home
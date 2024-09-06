import React from 'react'
import video from '../../assets/home_video.mp4'
import '../Hero/Hero.css'

const Hero = () => {
  return (
    <div className="video-container">
        <video autoPlay muted loop className="background-video">
        <source src={video} type="video/mp4" />
        Your browser does not support the video tag.
        </video>
    </div>
  )
}

export default Hero
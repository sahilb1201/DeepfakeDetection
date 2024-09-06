import React from 'react'
import des1 from '../../assets/des1.jpeg'
import '../Description/Description.css'

const Description = () => {
  return (
    <div class="container">
    <div class="text-section">
      <h1>Detect deep fake easily in seconds</h1>
      <div class="feature">
        <i class="fas fa-cloud-upload-alt"></i>
        <div>
          <h2>Upload instantly</h2>
          <p>Upload your video, audio and pictures in one click in upload button and have patience for the Kavach to work for you.</p>
        </div>
      </div>
      <div class="feature">
        <i class="fas fa-crop-alt"></i>
        <div>
          <h2>Crop faces automatically</h2>
          <p>The automatic face-cropping feature in the Deep Fake Detector simplifies the analysis process by quickly identifying and isolating faces within videos. This ensures that the focus remains on key areas, enhancing detection accuracy and saving users time. It's a smart, efficient way to streamline deep fake identification.</p>
        </div>
      </div>
      <div class="feature">
        <i class="fas fa-check-circle"></i>
        <div>
          <h2>Easy to use</h2>
          <p>The Deep Fake Detector is incredibly easy to use, featuring an intuitive design that allows users to quickly upload and analyze videos with minimal effort. Clear instructions and a straightforward interface make the process accessible even for those with limited technical knowledge, ensuring a hassle-free experience for everyone.</p>
        </div>
      </div>
    </div>
    <div class="image-section">
      <img src={des1} alt="Description-1" />
    </div>
  </div>

  )
}

export default Description
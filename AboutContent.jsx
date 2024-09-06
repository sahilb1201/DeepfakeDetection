import React from 'react';
import '../AboutContent/AboutContent.css'
import mission from '../../assets/mission.png'
import artificial from '../../assets/artificial.png'

const AboutContent = () => {
  return (
    <>
    <h1 className='ok'>About DeepGuardians</h1>
    <div class="container2">
    <div class="text-section2">
      <div class="feature2">
        <div>
          <h2>Our Mission:</h2>
          <p>Our mission is to combat misinformation and protect the integrity of digital content by developing advanced AI-based tools to detect and authenticate deep fake videos. We aim to safeguard individuals, organizations, and society from the harmful impacts of manipulated media.</p>
        </div>
      </div>
      <div class="feature2">
        <div>
          <h2>What is DeepGuardians?</h2>
          <p> Deep Guardians is a dedicated team focused on developing innovative forensic techniques to identify deep fake videos. Using cutting-edge AI/ML technology, we aim to detect face-swap manipulations and other synthetic content, ensuring authenticity and security in the digital world.</p>
        </div>
      </div>
    </div>
    <div class="image-section2">
      <img src={mission} className='img-pic' alt="Description-1" />
    </div>
  </div>
  <div class="container2">
    <div class="image-section2">
        <img src={artificial}  alt="Description-1" />
    </div>
    <div class="text-section2">
        <div class="feature2">
            <div>
                <h2>Why DeepGuardians?</h2>
                <p>In a world increasingly affected by deep fakes and misinformation, Deep Guardians stands at the forefront of detection and prevention. We combine expertise in AI, machine learning, and digital forensics to provide robust, reliable solutions that help maintain trust in digital media.</p>
            </div>
        </div>
    <div class="feature2">
      <div>
        <h2>Our Technology:</h2>
        <p>We utilize advanced AI/ML techniques, including Convolutional Neural Networks, Recurrent Neural Networks, and Adversarial Training, to detect deep fakes. Our approach involves analyzing spatial, temporal, audio, and frequency inconsistencies to deliver accurate and comprehensive deep fake detection.</p>
      </div>
    </div>
  </div>
</div>
</>
  );
};

export default AboutContent;
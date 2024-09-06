import React from 'react';
import '../AboutContentlast/AboutContentlast.css'; // Import the CSS file
import project from '../../assets/project-management.png'

const AboutContentlast = () => {
  return (
    <div className="container1">
      <div className="text-section1">
        <div className="feature1">
          <div>
            <h2>Our Commitment to Privacy:</h2>
            <p>
              We are committed to maintaining the highest standards of privacy and security. Our solutions are designed to ensure the confidentiality of your data, with no compromises on the ethical handling of sensitive information and personal privacy.
            </p>
          </div>
        </div>
        <div className="feature1">
          <div>
            <h2>Join Us in the Fight:</h2>
            <p>
              Join Deep Guardians in our mission to fight misinformation. By leveraging the latest in AI and machine learning, we can work together to counteract the negative impact of deep fakes and promote truth and transparency in digital media.
            </p>
          </div>
        </div>
      </div>
      <div className="image-section1">
        <img src={project} alt="Description-1" />
      </div>
    </div>
  );
};

export default AboutContentlast;



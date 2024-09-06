import React from 'react';
import '../Footer/Footer.css';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="containerf">
        <div className="row">
          <div className="footer-col">
            <h4>company</h4>
            <ul>
              <li>about us</li>
              <li>our services</li>
              <li>privacy policy</li>
              <li>affiliate program</li>
            </ul>
          </div>
          <div className="footer-col">
            <h4>get help</h4>
            <ul>
              <li>FAQ</li>
              <li>Support</li>
              <li>Report a Deep Fake</li>
              <li>How It Works</li>
            </ul>
          </div>
          <div className="footer-col">
            <h4>Detection</h4>
            <ul>
              <li>Home</li>
              <li>Detection Methods</li>
              <li>Video Analysis</li>
              <li>Security Guidelines</li>
            </ul>
          </div>
          <div className="footer-col">
            <h4>follow us</h4>
            <div className="social-links">
              <ul>
                <li><i className="fab fa-facebook-f"></i></li>
                <li><i className="fab fa-twitter"></i></li>
                <li><i className="fab fa-instagram"></i></li>
                <li><i className="fab fa-linkedin-in"></i></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

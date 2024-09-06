import React, { useState } from "react";
import "../Detect/Detect.css";

const VideoUpload = () => {
  const [file, setFile] = useState(null);
  const [dragText, setDragText] = useState("Drag & Drop to Upload Video");
  const [preview, setPreview] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [processing, setProcessing] = useState(false);
  const [statusMessage, setStatusMessage] = useState("");

  const validExtension = "video/mp4";  // Only allowing mp4

  const handleFileInput = (e) => {
    const selectedFile = e.target.files[0];
    handleFile(selectedFile);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    setDragText("Release to Upload Video");
  };

  const handleDragLeave = () => {
    setDragText("Drag & Drop to Upload Video");
  };

  const handleDrop = (e) => {
    e.preventDefault();
    const droppedFile = e.dataTransfer.files[0];
    handleFile(droppedFile);
  };

  const handleFile = (selectedFile) => {
    if (selectedFile && selectedFile.type === validExtension) {
      setErrorMessage("");
      setFile(selectedFile);
      setProcessing(true);  // Show start processing button
      const reader = new FileReader();
      reader.onload = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(selectedFile);
    } else {
      setErrorMessage("Please input the video in the mp4 format only");
      setFile(null);
      setPreview(null);
      setProcessing(false);
    }
  };

  const handleStartProcess = async () => {
    try {
      const response = await fetch("http://localhost:5000/start-process", {
        method: 'GET',
      });
      const result = await response.json();
      if (response.ok) {
        setStatusMessage(result.message);  // Prints "Connection successful"
      } else {
        setStatusMessage("Connection unsuccessful!");
      }
    } catch (error) {
      setStatusMessage("Connection unsuccessful!");
    }
  };

  const handleCancel = () => {
    setFile(null);
    setPreview(null);
    setProcessing(false);  // Hide start processing button
    setDragText("Drag & Drop to Upload Video");
  };

  return (
    <div
      className={`drag-area ${file ? "active" : ""}`}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
    >
      {errorMessage && <p className="error-message">{errorMessage}</p>}

      {preview ? (
        <>
          <video width="400" controls>
            <source src={preview} type={file?.type} />
            Your browser does not support the video tag.
          </video>
          <div className="button-group">
            <button className="action-button" onClick={handleStartProcess}>
              Generate
            </button>
            <button className="action-button" onClick={handleCancel}>
              Cancel
            </button>
          </div>
          {statusMessage && <p>{statusMessage}</p>}
        </>
      ) : (
        <>
          <div className="icon">
            <i className="fas fa-cloud-upload-alt"></i>
          </div>
          <header>{dragText}</header>
          <span>OR</span>
          <button onClick={() => document.querySelector("input").click()}>
            Browse File
          </button>
          <input
            type="file"
            hidden
            onChange={handleFileInput}
            accept="video/mp4"
          />
        </>
      )}
    </div>
  );
};

export default VideoUpload;
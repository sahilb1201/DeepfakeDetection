import React from 'react'
import Navbar from './Components/Navbar/Navbar'
import './App.css'
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Login from './Pages/Login';
import Home from './Pages/Home';
import Upload from './Pages/Upload';
import About from './Pages/About';
import Footer from './Components/Footer/Footer';


const App = () => {
  return (
    <BrowserRouter>
    <Navbar />
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/login' element={<Login/>}/>
      <Route path='/upload' element={<Upload />} />
      <Route path='/about' element={<About />} />
    </Routes>
    <Footer />
    </BrowserRouter>
  )
}

export default App
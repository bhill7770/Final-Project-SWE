import React, { useState, useEffect } from 'react'
import { Link } from "react-router-dom";
import Searchbar from '../SearchBar';
import './profile.css';

import { useRef } from 'react';
import { useAuth } from './firebase';
import { signup } from "./firebase";
import { logout } from './firebase';
import { login } from './firebase';
import { upload } from './firebase';


export default function Profile() {

    const [photoURL, setPhotoURL] = useState("https://i.pinimg.com/474x/8f/e6/66/8fe66626ec212bb54e13fa94e84c105c.jpg");
    const [photo, setPhoto] = useState(null);
    const [loading, setLoading] = useState(false);
    const currentUser = useAuth();

    const emailRef = useRef();
    const passwordRef = useRef();

    async function handleSignup() {

        setLoading(true);
        try {
            await signup(emailRef.current.value, passwordRef.current.value);
        } catch {
            alert("Error! Information entered is already in use.")
        }
        setLoading(false);
    }


    async function handleUpdate() {

        setLoading(true);
        try {
            await login(emailRef.current.value, passwordRef.current.value);
        } catch {
            alert("Error! Information entered is already in use.")
        }
        setLoading(false);
    }


    async function handleRemove() {
        setLoading(true);
        try {
            await logout();

        } catch {
            alert("Error! Information entered is already in use.")
        }
        setLoading(false);
    }


    function handleChange(e) {
        if (e.target.files[0]) {
            setPhoto(e.target.files[0])
        }
    }

    function handleClick() {
        upload(photo, currentUser, setLoading);
    }

    useEffect(() => {
        if (currentUser?.photoURL) {
            setPhotoURL(currentUser.photoURL)
        }
    }, [currentUser])



    return (
        <main className="main" style={{ padding: "1rem 0" }}>
            <header
                style={{
                    color: '#6765c7',
                }}
            >
                <h1>PersonalPix</h1>
            </header>
            <nav id="navbar"
                style={{
                    color: '#6765c7',
                    border: "solid 10px",
                    padding: "10px",
                }}
            >
                <Link to="/home">Home</Link> |{" "}
                <Link to="/mylist">My Lists</Link> | {" "}
                <Link to="/profile">Profile</Link > | {" "}
                <Link to="/contactForm">Contact Form</Link > | {" "}
                <Link to="/search">Search</Link>

            </nav >

            <div className='fields'>
                <form>
                    <div>
                        <br></br>
                        <h1>Profile</h1>
                        <div> Currently logged in as: {currentUser?.email}</div><br></br>

                        <img src={photoURL} alt="avatar" className="avatar" /><br></br><br></br><hr />

                        <input type="file" onChange={handleChange} /><br></br><br></br>

                        <button disable={loading || !photo} onClick={handleClick}>UPLOAD</button><br></br>

                        {!currentUser &&
                            <>  <div className="fields">
                                <label>EMAIL</label><br></br>
                                <input ref={emailRef} placeholder="Email" /><br></br>
                                <br></br>
                                <label>PASSWORD</label><br></br>
                                <input ref={passwordRef} type="password" placeholder="Password" />

                            </div>
                                <button disabled={loading} onClick={handleSignup}> SAVE </button><br></br><br></br>
                                <button disabled={loading} onClick={handleUpdate}> UPDATE </button>
                            </>}

                        <br></br><br></br>
                        {currentUser && <> <button disabled={loading || !currentUser} onClick={handleRemove}> REMOVE </button></>}

                    </div>
                    <div id="main">
                    </div>

                </form>
            </div>

        </main >
    );
}




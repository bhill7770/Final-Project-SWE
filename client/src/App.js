import React, { useState, useEffect } from 'react'
import { BrowserRouter, Link, Route, Switch, NavLink } from 'react-router-dom'
import { IoIosSearch } from "react-icons/io";
import Login from './components/Login';
import Home from './components/home';

function App() {
    const [data, setData] = useState({})
    const [search, setSearch] = useState("");

    useEffect(() => {

    }, [])

    function handleChange(e) {
        setSearch(e.target.value)
        console.log(search)
    }

    function sendQuery() {
        console.log(search)
        var postData = { query: search }
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(postData),
        }).then(
            res => res.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }

    return (
        <div>
            <header
                style={{
                    color: '#9966ff',
                }}
            >
                <h1>PersonalPix</h1>
            </header>

            <nav id="navbar"
                style={{
                    color: '#9966ff',
                    border: "solid 10px",
                    padding: "10px",
                }}
            >
                <Link to="/home">Home</Link> |{" "}
                <Link to="/mylist">My List</Link> |{" "}
                <Link to="/profile">Profile</Link>

                <NavLink to= "/home">Home</NavLink>
                
                <input type="text" placeholder="Search" onChange={handleChange}></input>
                <button type="button" onClick={() => sendQuery()}><IoIosSearch /></button>

            </nav>
            <Login/>
                
            {(typeof data.moviename === 'undefined') ? (
                <p>Loading...</p>
            ) : (
                data.moviename.map((nam, i) => (
                    <p key={i}>{nam}</p>
                ))
            )}
            
        </div>
    )
}

export default App
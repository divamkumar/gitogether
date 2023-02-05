import React, { useState } from "react"
import { resolvePath, Navigate } from "react-router-dom"

// import ReactDOM from 'react-dom/client';

export default function Auth(props) {
  // const navigate = useNavigate();
  const [authenticated, setauthenticated] = useState(null)

  // Signin/Signup toggle functions
  let [authMode, setAuthMode] = useState("signin")

  const changeAuthMode = () => {
    setAuthMode(authMode === "signin" ? "signup" : "signin")
  }

  // Form submit function
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}))
  }

  const handleSubmit = (event) => {
    event.preventDefault();

    var formdata = new FormData()

    formdata.append("fullname", inputs.fullname)
    formdata.append("username", inputs.username)
    formdata.append("password", inputs.password)

    var requestOptions = {
      method: 'POST',
      body: formdata,
      redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/"+authMode, requestOptions)
      .then(response => {
        return response.text()
        // if (response === "200") {
        //   console.log(response);
        //   // localStorage.setItem("authenticated", true)
        //   // navigate("/dashboard");
        // }
        // console.log(response)
      })
      .then(result => {
        if (result === "200") {
          // localStorage.setItem("authenticated", true)
          setauthenticated(true)
        } else alert("fuck") 
      })
      .catch(error => console.log('error', error));
  }

  if (authMode === "signin") {
    return authenticated ?  <Navigate replace to="/dashboard" /> : (
      <div className="Auth-form-container">
        <form className="Auth-form" onSubmit={handleSubmit}>
          <div className="Auth-form-content">
            <h3 className="Auth-form-title">Sign In</h3>
            <div className="text-center">
              Not registered yet?{" "}
              <span className="link-primary" onClick={changeAuthMode}>
                <a href="#">Sign Up</a>
              </span>
            </div>
            <div className="form-group mt-3">
              <label>GitHub Username</label>
              <input
                type="text"
                name="username"
                placeholder="GitHub Username"
                value={inputs.username || ""} 
                onChange={handleChange}
                className="form-control mt-1"
              />
            </div>
            <div className="form-group mt-3">
              <label>Password</label>
              <input
                type="password"
                name="password"
                placeholder="Gitogether Password"
                value={inputs.password || ""} 
                onChange={handleChange}
                className="form-control mt-1"
              />
            </div>
            <div className="d-grid gap-2 mt-3">
              <button type="submit" className="btn btn-primary">
                Submit
              </button>

            </div>
            <p className="text-center mt-2">
              Forgot <a href="#">password?</a>
            </p>
          </div>
        </form>
      </div>
    )
  }

  return (
    <div className="Auth-form-container">
      <form className="Auth-form" onSubmit={handleSubmit}>
        <div className="Auth-form-content">
          <h3 className="Auth-form-title">Sign Up</h3>
          <div className="text-center">
            Already registered?{" "}
            <span className="link-primary" onClick={changeAuthMode}>
              <a href="#">Sign In</a>
            </span>
          </div>
          <div className="form-group mt-3">
            <label>Full Name</label>
            <input
              type="text"
              name="fullname"
              placeholder="e.g Jane Doe"
              value={inputs.fullname || ""}
              onChange={handleChange}
              className="form-control mt-1"
            />
          </div>
          <div className="form-group mt-3">
            <label>GitHub Username</label>
            <input
              type="text"
              name="username"
              placeholder="GitHub Username"
              value={inputs.username || ""} 
              onChange={handleChange}
              className="form-control mt-1"
            />
          </div>
          <div className="form-group mt-3">
            <label>Password</label>
            <input
              type="password"
              name="password"
              placeholder="Gitogether Password"
              value={inputs.password || ""} 
              onChange={handleChange}
              className="form-control mt-1"
            />
          </div>
          <div className="d-grid gap-2 mt-3">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
          <p className="text-center mt-2">
            Forgot <a href="#">password?</a>
          </p>
        </div>
      </form>
    </div>
  )
}

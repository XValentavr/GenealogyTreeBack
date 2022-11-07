import React, {useState} from "react";
import styles from "./Login.css"
import Input from "../UI/Input";
import Button from "../UI/Button";
import SocialLoginOrRegister from "../UI/SocialLoginOrRegister";

const Login = props => {
    const [confirmLogin, setConfirmLogin] = useState(false);
    const onSubmitLoginHandler = event => {
        event.preventDefault()
        setConfirmLogin(true)
        props.onClosedLogin(confirmLogin)
    }
    return (
        <React.Fragment>
            {!confirmLogin && (
                <div className="container">
                    <form className="form-1">
                        <h1>Login</h1>
                        <label htmlFor="email">Email</label>
                        <input type="email" name="email" id="email" required/>
                        <label htmlFor="password">Password</label>
                        <input type="password" name="password" id="password" required/>
                        <span>Forgot Password</span>
                        <button>Login</button>

                        <p>Or SignUp Using</p>
                        <div className="icons">
                            <a href="https://www.facebook.com/" target="blank"
                            ><i className="fab fa-facebook-f">Facebook</i
                            ></a>
                            <a href="https://twitter.com/" target="blank"
                            ><i className="fab fa-twitter">Twitter</i
                            ></a>
                            <a href="https://mail.google.com/" target="blank"
                            ><i className="fab fa-google">Google</i
                            ></a>
                        </div>
                    </form>
                </div>)
            }
        </React.Fragment>
    );
}
export default Login
import React from "react";
import classes from './Nav.module.css'

const Nav = props => {
    const openFeedbackHandler = event => {
        props.openFeedbackOrAuthHandler(!props.initialIsOpened)
        props.formType(event.target.id)
    }
    return (
        <div className={classes.wrapper}>
            <ul>
                <li>Домашня</li>
                <li>Про нас</li>
                <li id='feedback' onClick={openFeedbackHandler}>Зв'язок з нами</li>
                <li>Авторизація</li>
            </ul>
        </div>
    );
}
export default Nav
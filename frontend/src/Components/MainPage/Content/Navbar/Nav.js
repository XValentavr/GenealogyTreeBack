import React from "react";
import classes from './Nav.module.css'

const Nav = props => {
    const openFeedbackHandler = () => {
        props.portalFeedbackHandler(!props.initialIsOpened)
    }
    return (
        <div className={classes.wrapper}>
            <ul>
                <li>Домашня</li>
                <li>Про нас</li>
                <li onClick={openFeedbackHandler}>Зв'язок з нами</li>
                <li>Авторизація</li>
            </ul>
        </div>
    );
}
export default Nav
import React, {Fragment} from "react";
import classes from './Button.module.css'

const Button = props => {
    return (
        <Fragment>
            <label>{props.label}</label>
            <button className={classes.created_button} type={props.type}>
                {props.buttonText}</button>
        </Fragment>
    );
}
export default Button
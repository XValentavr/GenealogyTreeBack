import React from "react";
import classes from './LabelCard.module.css'

const LabelCard = props => {
    return (
        <label  spellCheck="true"  htmlFor={props.htmlFor} className={classes.MainLabel}>{props.children}</label>
    );
}
export default LabelCard
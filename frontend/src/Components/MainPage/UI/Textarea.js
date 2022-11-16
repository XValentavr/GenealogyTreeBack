import React from "react";
import classes from './Textarea.module.css'
import LabelCard from "../Card/LabelCard";

const Textarea = props => {
    return (
        <div className={props.inputClass}>
            <textarea rows="10" cols="50" id="Інформація" className={classes.created_textarea}/>
            <LabelCard htmlFor={props.id}>{props.label}</LabelCard>
        </div>
    );
}
export default Textarea
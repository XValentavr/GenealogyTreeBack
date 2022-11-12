import React, {Fragment} from "react";
import classes from './Input.module.css'
import LabelCard from "../Card/LabelCard";

const Input = props => {
    return (
        <div className={props.inputClass}>
            <input className={classes.created_input} type={props.type} name={props.name} required/>
            <LabelCard>{props.label}</LabelCard>
        </div>
    );
}
export default Input
import React from "react";
import styles from './Input.module.css'

const Input = props => {
    return (
            <div className={`${styles.control}`}>
                <label htmlFor={props.formId}>{props.label}</label>
                <input
                    type={props.type}
                    id={props.formId}
                    placeholder={props.placeholder}
                />
            </div>
    );
}
export default Input
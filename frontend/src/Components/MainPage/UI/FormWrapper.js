import React from "react";
const FormWrapper = props => {
    return (
        <div className={props.wrapper}>
            <div className={props.inner}>
                {props.children}
            </div>
        </div>
    );
}
export default FormWrapper
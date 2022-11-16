import React from "react";
const FormWrapper = props => {
    return (
            <div className={props.inner}>
                {props.children}
            </div>
    );
}
export default FormWrapper
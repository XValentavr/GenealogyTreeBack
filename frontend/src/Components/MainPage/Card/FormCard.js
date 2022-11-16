import React from "react";
const FormCard = props => {
    return (
            <div className={props.innerClass}>
                {props.children}
            </div>
    );
}
export default FormCard
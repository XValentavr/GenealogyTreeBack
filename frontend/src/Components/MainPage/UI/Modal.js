import React, {Fragment} from "react";
import classes from './Modal.module.css'
import ReactDOM from "react-dom";
const portalFeedback = document.getElementById('overlays')
const Overlay = props => {
    return (
        <div className={classes.modal}>
            {props.children}
        </div>
    );
}
const Modal = props => {
    return (
        <Fragment>
            {ReactDOM.createPortal(<div className={classes.backdrop} onClick={props.onClose}/>, portalFeedback)}
            {ReactDOM.createPortal(<Overlay>{props.children}</Overlay>, portalFeedback)}
        </Fragment>
    );
}
export default Modal
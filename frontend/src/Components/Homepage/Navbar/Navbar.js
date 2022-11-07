import React from "react";
import styles from './Navbar.module.css'
import OpenButton from "./OpenButton";
import MainContent from "./MainContent";
import CloseButton from "./CloseButton";
import Card from "../Card/Card";

const Navbar = props => {
    const isOpenedFeedbackHandler = flagIfOpenedFeedback => props.onOpenFeedback(flagIfOpenedFeedback)
    const isOpenedLoginHandler = flagIsOpenedLogin => props.onOpenLogin(flagIsOpenedLogin)

    return (
        <React.Fragment>
            <Card setClass={styles["menu-outer"]}>
                <OpenButton/>
                <MainContent onOpenFeedbackParent={isOpenedFeedbackHandler} onOpenLoginParent={isOpenedLoginHandler}/>
            </Card>
            {!props.onOpenNav ? <CloseButton onClose={props.onCloseNav}/> : props.onCloseNav(false)}
        </React.Fragment>
    )
};
export default Navbar
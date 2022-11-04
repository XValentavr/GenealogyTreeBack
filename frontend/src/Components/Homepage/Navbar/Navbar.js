import React from "react";
import styles from './Navbar.module.css'
import OpenButton from "./OpenButton";
import MainContent from "./MainContent";
import CloseButton from "./CloseButton";

const Navbar = props => {
    return (
        <div>
            <div className={styles["menu-outer"]}>
                <OpenButton/>
                <MainContent/>
            </div>
            <CloseButton/>
        </div>
    )
};
export default Navbar
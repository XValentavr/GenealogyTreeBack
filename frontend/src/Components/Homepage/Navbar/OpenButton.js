import React from "react";
import styles from './Navbar.module.css'

const OpenButton = props => {
    return (
        <div className={styles["menu-icon"]}>
            {new Array(3).fill('').map(() => <div className={styles.bar}></div>)}
        </div>
    )
};
export default OpenButton
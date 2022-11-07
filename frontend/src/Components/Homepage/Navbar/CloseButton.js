import React, {useState} from "react";
import styles from './Navbar.module.css'

const CloseButton = props => {
    return (

            <a className={styles["menu-close"]} onClick={props.onClose}>
                <div className={styles["menu-icon"]}>
                    {new Array(2).fill('').map(() => <div className={styles.bar} key={Math.random().toString()}></div>)}
                </div>
            </a>
    );
}
export default CloseButton
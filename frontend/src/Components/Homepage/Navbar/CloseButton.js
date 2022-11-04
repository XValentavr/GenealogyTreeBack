import React, {useState} from "react";
import styles from './Navbar.module.css'

const CloseButton = props => {
    const [isOpened, setIsOpened] = useState(false)
    const onClosedHandler = () => setIsOpened(true)
    return (
        !isOpened ?
            <a className={styles["menu-close"]} onClick={onClosedHandler}>
                <div className={styles["menu-icon"]}>
                    {new Array(2).fill('').map(() => <div className={styles.bar}></div>)}
                </div>
            </a> : setIsOpened(false)
    );
}
export default CloseButton
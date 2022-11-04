import React from "react";
import styles from './AboutUs.module.css'
import AboutUsContent from "./AbounUsContent";
import AboutUsTitle from "./AboutUsTitle";
import AboutUsImage from "./AboutUsImage";

const AboutUs = props => {
    return (
        <section className={styles.section}>
            <div className={styles.container}>
                <div className={styles['content-section']}>
                    <AboutUsTitle/>
                    <AboutUsContent/>
                </div>
                <AboutUsImage/>
            </div>
        </section>
    );
}
export default AboutUs
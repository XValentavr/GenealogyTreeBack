import React from "react";
import styles from './AboutUs.module.css'
import AboutUsContent from "./AboutUsContent";
import AboutUsTitle from "./AboutUsTitle";
import AboutUsImage from "./AboutUsImage";
import Card from "../Card/Card";
import AboutUsOurWorkers from "./AboutUsOurWorkers";

const AboutUs = props => {
    return (
        <section id="AboutUs" className={styles.section}>
            <div className={styles.container}>
                <Card setClass={styles['content-section']}>
                    <AboutUsTitle/>
                    <AboutUsContent/>
                </Card>
                <AboutUsImage/>
                <div className={styles["inner-container"]}>
                    <AboutUsOurWorkers/>
                    <AboutUsOurWorkers/>
                    <AboutUsOurWorkers/>
                    <AboutUsOurWorkers/>
                    <AboutUsOurWorkers/>
                    <AboutUsOurWorkers/>
                    <AboutUsOurWorkers/>
                    <AboutUsOurWorkers/>

                </div>
            </div>
        </section>
    );
}
export default AboutUs
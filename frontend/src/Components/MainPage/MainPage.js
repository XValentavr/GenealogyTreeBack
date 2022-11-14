import React, {useContext, useState} from "react";
import Nav from "./Content/Navbar/Nav";
import AboutUs from "./Content/AboutUs/AboutUs";
import Homepage from "./Content/Homepage/Homepage";
import Form from "./Content/Feedback/Form";
import FeedbackContext from "./store/feedback/feedback-context";

const MainPage = props => {

    const feedbackCtx = useContext(FeedbackContext)

    const openFeedbackHandler = isOpened => feedbackCtx.closeFeedback(isOpened)

    return (
        <React.Fragment>
            <Nav openFeedbackHandler={openFeedbackHandler} initialIsOpened={feedbackCtx.isOpenFeedback}/>
            {feedbackCtx.isOpenFeedback ? <Form/> :
                <React.Fragment>
                    <Homepage/>
                    <AboutUs/>
                </React.Fragment>
            }
        </React.Fragment>
    );
}
export default MainPage
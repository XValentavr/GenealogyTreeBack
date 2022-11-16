import React, {Fragment, useContext, useState} from "react";
import Nav from "./Content/Navbar/Nav";
import AboutUs from "./Content/AboutUs/AboutUs";
import Homepage from "./Content/Homepage/Homepage";
import FeedbackOrAuthForm from "./Content/FeedbackOrAuth/FeedbackOrAuthForm";
import FeedbackOrAuthContext from "./store/FeedbackOrAuth/feedbackOrAuth-context";

const MainPage = props => {

    const [formType, setFormType] = useState('')

    const setFormTypeHandler = formType => setFormType(formType)

    const feedbackOrAuthCtx = useContext(FeedbackOrAuthContext)

    const openFeedbackOrAuthHandler = isOpened => feedbackOrAuthCtx.closeFeedbackOrAuth(isOpened)
    return (
        <Fragment>
            <Nav formType={setFormTypeHandler} openFeedbackOrAuthHandler={openFeedbackOrAuthHandler}
                 initialIsOpened={feedbackOrAuthCtx.isOpenFeedbackOrAuth}/>
            {feedbackOrAuthCtx.isOpenFeedbackOrAuth && formType === "feedback" ?
                <FeedbackOrAuthForm formType={formType}/> :
                <React.Fragment>
                    <Homepage/>
                    <AboutUs/>
                </React.Fragment>
            }
        </Fragment>
    );
}
export default MainPage
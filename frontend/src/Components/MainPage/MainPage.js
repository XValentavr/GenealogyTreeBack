import React, {useState} from "react";
import Nav from "./Content/Navbar/Nav";
import AboutUs from "./Content/AboutUs/AboutUs";
import Homepage from "./Content/Homepage/Homepage";
import Form from "./Content/Feedback/Form";

const MainPage = props => {
    const [isOpenFeedback, setIsOpenFeedback] = useState(false)

    const portalFeedbackHandler = isOpened => {
        setIsOpenFeedback(isOpened)
    }
    return (
        <React.Fragment>
            <Nav portalFeedbackHandler={portalFeedbackHandler} initialIsOpened={isOpenFeedback}/>
            {isOpenFeedback ? <Form/> :
                <React.Fragment>
                    <Homepage/>
                    <AboutUs/>
                </React.Fragment>
            }
        </React.Fragment>
    );
}
export default MainPage
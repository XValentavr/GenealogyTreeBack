import Navbar from "../Navbar/Navbar";
import AboutUs from "../AboutUs/AboutUs";
import React, {useEffect, useState} from "react";
import Feedback from "../Feedback/Feedback";
import Login from "../Authorization/Login";
import Guarantee from "../Guarantee/Guarantee";
import Previous from "../PrevWorks/Previous";

const MainPage = () => {
    const [isOnOpenOrClosedFeedback, setIsOnOpenOrClosedFeedback] = useState(false)
    const [isOnOpenOrClosedLogin, setIsOnOpenOrClosedLogin] = useState(false)
    const [isOnOpenAboutUs, setIsOnOpenAboutUs] = useState(false)

    const onOpenFeedbackHandler = flagIsSetOpened => setIsOnOpenOrClosedFeedback(flagIsSetOpened)

    const onClosedFeedbackHandler = flagIsSetClosed => setIsOnOpenOrClosedFeedback(flagIsSetClosed)

    const onOpenLoginHandler = flagIsSetOpenLogin => setIsOnOpenOrClosedLogin(flagIsSetOpenLogin)

    const onClosedLoginHandler = flagIsSetClosedLogin => setIsOnOpenOrClosedLogin(flagIsSetClosedLogin)


    const [isOpenedNav, setIsOpenedNav] = useState(false)
    const onClosedNavHandler = value => setIsOpenedNav(value)

    return (
        isOnOpenOrClosedFeedback ?
            <React.Fragment>
                < Feedback onClosedFeedback={onClosedFeedbackHandler}/>
            </React.Fragment>
            :
            (isOnOpenOrClosedLogin ?
                <React.Fragment>
                    <Login onClosedLogin={onClosedLoginHandler}/>
                </React.Fragment>
                : <React.Fragment>
                    <AboutUs/>
                    <Guarantee/>
                    <Previous/>
                    <Navbar onCloseNav={onClosedNavHandler} onOpenFeedback={onOpenFeedbackHandler}
                            onOpenLogin={onOpenLoginHandler} onOpenNav={isOpenedNav}/>
                </React.Fragment>)
    )
};
export default MainPage
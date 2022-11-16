import React, {useState} from "react";
import FeedbackOrAuthContext from "./feedbackOrAuth-context";


const FeedbackOrAuthProvider = props => {
    const [isOnFeedbackOrAuth, setIsOnFeedbackOrAuth] = useState(false)

    const isOpenFeedbackOrAuthHandler = () => setIsOnFeedbackOrAuth(!isOnFeedbackOrAuth)

    const feedbackOrAuthContext = {
        isOpenFeedbackOrAuth: isOnFeedbackOrAuth,
        closeFeedbackOrAuth: isOpenFeedbackOrAuthHandler
    }
    return (
        <FeedbackOrAuthContext.Provider value={feedbackOrAuthContext}>
            {props.children}
        </FeedbackOrAuthContext.Provider>
    );
}
export default FeedbackOrAuthProvider
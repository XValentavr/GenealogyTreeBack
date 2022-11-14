import React, {useState} from "react";
import FeedbackContext from "./feedback-context";


const FeedbackProvider = props => {
    const [isOnFeedback, setIsOnFeedback] = useState(false)

    const isOpenFeedbackHandler = () => setIsOnFeedback(!isOnFeedback)

    const feedbackContext = {
        isOpenFeedback: isOnFeedback,
        closeFeedback: isOpenFeedbackHandler
    }
    return (
        <FeedbackContext.Provider value={feedbackContext}>
            {props.children}
        </FeedbackContext.Provider>
    );
}
export default FeedbackProvider
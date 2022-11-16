import React from "react";

const FeedbackContext = React.createContext({
    isOpenFeedback: false,
    closeFeedback: flag => {}
});
export default FeedbackContext;
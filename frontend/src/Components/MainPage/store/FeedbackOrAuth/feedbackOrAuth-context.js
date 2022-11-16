import React from "react";

const FeedbackOrAuthContext = React.createContext({
    isOpenFeedbackOrAuth: false,
    closeFeedbackOrAuth: flag => {
    },
});
export default FeedbackOrAuthContext;
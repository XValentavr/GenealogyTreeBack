import React from "react";
import './App.css';
import MainPage from "./Components/MainPage/MainPage";
import FeedbackOrAuthProvider from "./Components/MainPage/store/FeedbackOrAuth/FeedbackOrAuthProvider";
function App() {
    return (
        <FeedbackOrAuthProvider>
                <MainPage/>
        </FeedbackOrAuthProvider>
    );
}

export default App;

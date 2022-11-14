import React from "react";
import './App.css';
import MainPage from "./components/MainPage/MainPage";
import FeedbackProvider from "./components/MainPage/store/feedback/FeedbackProvider";

function App() {
    return (
        <FeedbackProvider>
            <MainPage/>
        </FeedbackProvider>
    );
}

export default App;

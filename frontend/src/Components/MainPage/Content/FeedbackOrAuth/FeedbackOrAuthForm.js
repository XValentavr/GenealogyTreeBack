import React, {useContext, useState} from "react";
import classes from './Feedback.module.css'
import Input from "../../UI/Input";
import Button from "../../UI/Button";
import FormCard from "../../Card/FormCard";
import LabelCard from "../../Card/LabelCard";
import Modal from "../../UI/Modal";
import FeedbackOrAuthContext from "../../store/FeedbackOrAuth/feedbackOrAuth-context";
import Textarea from "../../UI/Textarea";
import Feedback from "./Feedback";

const FeedbackOrAuthForm = props => {
    const [formIsValid, setFormIsValid] = useState(false)

    const onCheckIsValidHandler = flag => setFormIsValid(flag)

    const feedbackOrAuthCtx = useContext(FeedbackOrAuthContext)

    const closeFeedbackOrAuthHandler = isOpened => feedbackOrAuthCtx.closeFeedbackOrAuth(!isOpened)

    const submitHandler = event => {
        event.preventDefault()
        feedbackOrAuthCtx.closeFeedbackOrAuth(false)
    }
    if (props.formType === "feedback") {
        return (
            <Feedback closeFeedbackOrAuthHandler={closeFeedbackOrAuthHandler}
                      submitHandler={submitHandler}
                      onCheckIsValidHandler={onCheckIsValidHandler}
                      formIsValid={formIsValid}
            />)
    }
}
export default FeedbackOrAuthForm
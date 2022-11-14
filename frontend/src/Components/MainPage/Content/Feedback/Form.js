import React, {useContext, useState} from "react";
import classes from './Form.module.css'
import Input from "../../UI/Input";
import Button from "../../UI/Button";
import FormWrapper from "../../Card/FormWrapper";
import LabelCard from "../../Card/LabelCard";
import Modal from "../../UI/Modal";
import FeedbackContext from "../../store/feedback/feedback-context";
import Textarea from "../../UI/Textarea";

const Form = props => {
    const [formIsValid, setFormIsValid] = useState(false)

    const onCheckIsValidHandler = flag => {
        setFormIsValid(flag)
    }
    const feedbackCtx = useContext(FeedbackContext)

    const closeFeedbackHandler = isOpened => feedbackCtx.closeFeedback(!isOpened)

    const submitHandler = event => {
        event.preventDefault()
        feedbackCtx.closeFeedback(false)
    }
    return (
        <Modal onClose={closeFeedbackHandler}>
            <FormWrapper inner={classes["login-box"]}>
                <h2>Зв'язок з нами</h2>
                <form onSubmit={submitHandler}>
                    <Input onCheckIsValid={onCheckIsValidHandler} id="Full name" inputClass={classes["user-box"]}
                           type="text"
                           name="Full name"
                           label="Ваші дані"/>
                    <Input onCheckIsValid={onCheckIsValidHandler} id="Email" inputClass={classes["user-box"]}
                           type="email" label="Пошта" name="Email"/>
                    <Textarea inputClass={classes["user-box"]} id="Entered text" label="Ваше зверненя"
                              name="Entered text"/>
                    <Button disabled={!formIsValid} type="submit" buttonText="Відправити">
                    </Button>
                </form>
            </FormWrapper>
        </Modal>);
}
export default Form
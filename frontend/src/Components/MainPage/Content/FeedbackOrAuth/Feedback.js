import React from "react";
import Modal from "../../UI/Modal";
import FormCard from "../../Card/FormCard";
import classes from "./Feedback.module.css";
import Input from "../../UI/Input";
import Textarea from "../../UI/Textarea";
import Button from "../../UI/Button";

const Feedback = props => {
    return (
        <Modal onClose={props.closeFeedbackOrAuthHandler}>
            <FormCard innerClass={classes["login-box"]}>
                <h2>Зв'язок з нами</h2>
                <form onSubmit={props.submitHandler}>
                    <Input onCheckIsValid={props.onCheckIsValidHandler} id="Full name" inputClass={classes["user-box"]}
                           type="text"
                           name="Full name"
                           label="Ваші дані"/>
                    <Input onCheckIsValid={props.onCheckIsValidHandler} id="Email" inputClass={classes["user-box"]}
                           type="email" label="Пошта" name="Email"/>
                    <Textarea inputClass={classes["user-box"]} id="Entered text" label="Ваше зверненя"
                              name="Entered text"/>
                    <Button disabled={!props.formIsValid} type="submit" buttonText="Відправити">
                    </Button>
                </form>
            </FormCard>
        </Modal>
    );
}
export default Feedback
import React, {useState} from "react";
import styles from './Feedback.module.css'
import Button from "../UI/Button";
import Input from "../UI/Input";

const Feedback = props => {
    const [confirmSendFeedback, setConfirmSendFeedback] = useState(false)
    const onSubmitSendFeedbackHandler = event => {
        event.preventDefault()
        setConfirmSendFeedback(true)
        props.onClosedFeedback(confirmSendFeedback)
    }
    return (
        <React.Fragment>
            {!confirmSendFeedback && (<div className={styles.backdrop}>
                <header className={styles.header}>
                    <h2>Зв'язок з нами</h2>
                    <Button onSubmit={onSubmitSendFeedbackHandler} type="submit">Назад</Button>
                </header>
                <Input type="email" formId="email" placeholder="Введіть email"/>
                <Input type="text" formId="text" placeholder="Введіть ім'я"/>
                <Input type="text" formId="context" placeholder="Введіть текст"/>
                <footer className={styles.actions}>
                    <Button onSubmit={onSubmitSendFeedbackHandler} type="submit">Okay</Button>
                </footer>
            </div>)
            }
        </React.Fragment>
    );
}
export default Feedback
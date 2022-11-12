import React from "react";
import classes from './Form.module.css'
import Input from "../../UI/Input";
import Button from "../../UI/Button";
import FormWrapper from "../../UI/FormWrapper";
import LabelCard from "../../Card/LabelCard";

const Form = props => {
    return (
        <FormWrapper wrapper={classes.wrapper} inner={classes["login-box"]}>
            <h2>Зв'язок з нами</h2>
            <form>
                <Input inputClass={classes["user-box"]} type="text" name="ФІО" label="Ваші дані"/>
                <Input inputClass={classes["user-box"]} type="email" label="Пошта" name="Пошта"/>
                <div className={classes["user-box"]}>
                    <textarea/>
                    <LabelCard>Ваша інформація</LabelCard>
                </div>
                <Button type="submit" buttonText="Відправити">
                </Button>
            </form>
        </FormWrapper>
    )
        ;
}
export default Form
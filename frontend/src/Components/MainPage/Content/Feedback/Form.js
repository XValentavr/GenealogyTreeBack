import React from "react";
import classes from './Form.module.css'
import Input from "../../UI/Input";
import Button from "../../UI/Button";
import FormWrapper from "../../Card/FormWrapper";
import LabelCard from "../../Card/LabelCard";
import SectionCard from "../../Card/SectionCard";

const Form = props => {
    return (
        <SectionCard cssClass={"feedback"}>
            <FormWrapper inner={classes["login-box"]}>
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
        </SectionCard>);
}
export default Form
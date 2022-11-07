import React from "react";

const MainContent = props => {
    const onIsOpenFeedbackHandler = event => {
        event.preventDefault()
        props.onOpenFeedbackParent(true)
    }
    const onIsOpenLoginHandler = event => {
        event.preventDefault()
        props.onOpenLoginParent(true)
    }
    return (
        <nav>
            <ul>
                <li><a href="#AboutUs">Про нас</a></li>
                <li>
                    <a href="" onClick={onIsOpenFeedbackHandler}>Зворотній зв'язок
                    </a>
                </li>
                <li><a href="#guarantee">Гарантії</a></li>
                <li><a href="#previousWorks">Минулі роботи</a></li>
                <li><a href="" onClick={onIsOpenLoginHandler}>Авторизуватися</a></li>
            </ul>
        </nav>
    )
}
export default MainContent
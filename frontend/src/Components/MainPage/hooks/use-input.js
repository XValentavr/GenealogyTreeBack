import React, {useReducer} from "react";

const initialInputState = {
    value: '',
    isTouched: false
}

const ValidationChecker = (field, type) => {
    if (type === 'text') {
        return field.trim() !== '';
    } else if (type === 'email') {
        return field.includes('@')
    }
}

const inputStateReducer = (state, action) => {
    if (action.type === 'INPUT') return {value: action.value, isTouched: state.isTouched}
    if (action.type === 'BLUR') return {value: state.value, isTouched: true}
    return initialInputState
}
const useInput = (fieldType) => {
    const [inputState, dispatch] = useReducer(inputStateReducer, initialInputState)

    const isValid = ValidationChecker(inputState.value, fieldType)

    const errorDetected = !isValid && inputState.isTouched
    const valueInputHandler = event => {
        dispatch({
            type: "INPUT", value: event.target.value
        })
    }
    const valueBlurHandler = event => {
        dispatch({
            type: "BLUR", value: event.target.value
        })
    }
    return {
        value: inputState.value,
        isValid,
        errorDetected,
        valueInputHandler,
        valueBlurHandler
    }
}
export default useInput
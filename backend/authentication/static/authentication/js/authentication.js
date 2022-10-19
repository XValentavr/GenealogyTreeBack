function get_data_from_authentication_form() {
    const formData = new FormData(document.getElementById('authenticationform'));
    const user_reg = {}
    for (const [key, value] of formData) {
        {
            user_reg[key] = value
        }
    }

    if (user_reg.password !== user_reg.re_password) {
        const passworderror = document.getElementById('passworderror')
        passworderror.innerText = 'Паролі не співпадають.'
        passworderror.style.display = 'block'
        window.setTimeout("passworderror.style.display='none';", 5000);
    } else
        return user_reg
}

async function post_request_to_authenticate_user() {
    const myresponse = await fetch('http://localhost:8000/auth/api/v1/token/login/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(get_data_from_authentication_form())
    });
    const result = myresponse.status;
    if (result === 200) {
        window.location.href = 'http://localhost:8000/'
    } else if (result === 401) {
        create_bad_request_while_auth(await myresponse.json(), get_data_from_authentication_form())
    }
}

function create_bad_request_while_auth(json) {
    if (json.detail) {
        const dataerror = document.getElementById('dataerror')
        dataerror.innerText = 'Невірно вказані логін чи пароль. Перевірте правильність введених даних'
        dataerror.style.display = 'block'
        window.setTimeout("dataerror.style.display='none';", 5000);
    }
}

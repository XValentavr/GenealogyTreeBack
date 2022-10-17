function get_data_from_register_form() {
    const formData = new FormData(document.getElementById('registration'));
    const user_reg = {}
    for (const [key, value] of formData) {
        {
            user_reg[key] = value
        }
    }
    return user_reg
}

async function post_request_to_create_user() {
    const myresponse = await fetch('http://localhost:8000/auth/api/v1/users/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(get_data_from_register_form())
    });
    const result = myresponse.status;
    if (result === 201) {
        window.location.href = 'http://localhost:8000/'
    } else if (result === 400) {
        create_bad_request(await myresponse.json())
    }
}

function create_bad_request(json) {
    if (json.email) {
        const emailerror = document.getElementById('emailerror')
        emailerror.innerText = 'Користувач з такою поштою вже існує.'
        emailerror.style.display = 'block'
        window.setTimeout("emailerror.style.display='none';", 5000);
    } else if (json.password) {
        const passworderror = document.getElementById('passworderror')
        passworderror.innerText = 'Ваш пароль дуже короткий. Додайте букви, цифри і спеціальні знаки.'
        passworderror.style.display = 'block'
        window.setTimeout("passworderror.style.display='none';", 5000);
    }
}
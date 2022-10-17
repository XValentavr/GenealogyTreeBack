function get_data_from_set_new_password_form() {
    const formData = new FormData(document.getElementById('setnewpassword'));
    const newpass = {}
    for (const [key, value] of formData) {
        {
            newpass[key] = value
        }
    }
    if (newpass.new_password !== newpass.re_new_password) {
        const newpassworderror = document.getElementById('newpassworderror')
        newpassworderror.innerText = 'Паролі не співпадають.'
        newpassworderror.style.display = 'block'
        window.setTimeout("newpassworderror.style.display='none';", 5000);
    } else {
        delete newpass['re_new_password']
        let array = window.location.pathname.split('/');
        newpass['token'] = array[array.length - 1]
        newpass['uid'] = array[array.length - 2]
        return newpass
    }
}

async function post_request_to_set_new_password() {
    const myresponse = await fetch('http://localhost:8000/auth/api/v1/users/reset_password_confirm/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(get_data_from_set_new_password_form())
    });
    if (myresponse.status === 204) {
        window.location.href = 'http://localhost:8000/'
    } else if (myresponse.status === 400) {
        create_bad_new_pass_request(myresponse.json())
    }
}

function create_bad_new_pass_request(json) {
    if (json.detail) {
        const newpasserror = document.getElementById('newpassworderror')
        newpasserror.innerText = 'Ваш пароль дуже короткий. Додайте букви, цифри і спеціальні знаки.'
        newpasserror.style.display = 'block'
        window.setTimeout("newpasserror.style.display='none';", 5000);
    }
}


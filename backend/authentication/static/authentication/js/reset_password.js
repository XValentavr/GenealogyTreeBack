function get_data_from_reset_form() {
    const formData = new FormData(document.getElementById('resetpass'));
    const reset = {}
    for (const [key, value] of formData) {
        {
            reset[key] = value
        }
    }
    return reset
}

async function post_request_to_reset_password() {
    const myresponse = await fetch('http://localhost:8000/auth/api/v1/users/reset_password/', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(get_data_from_reset_form())
    });
    if (myresponse.status === 204) {
        window.location.href = 'http://localhost:8000/'
    }
}


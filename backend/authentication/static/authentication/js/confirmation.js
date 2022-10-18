const nums = document.querySelectorAll('.nums span');

function get_token_and_uid() {
    let array = window.location.href.split('/');

    let token = array[array.length - 1];
    let uid = array[array.length - 2];
    return {'token': token, 'uid': uid}
}

const myresponse = fetch('http://localhost:8000/auth/api/v1/users/activation/', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(get_token_and_uid())
});
if (myresponse.status !== 401)
    runAnimation();

function runAnimation() {
    nums.forEach((num, idx) => {
        const penultimate = nums.length - 1;
        num.addEventListener('animationend', (e) => {
            if (e.animationName === 'goIn' && idx !== penultimate) {
                num.classList.remove('in');
                num.classList.add('out');
            } else if (e.animationName === 'goOut' && num.nextElementSibling) {
                num.nextElementSibling.classList.add('in');
            } else {
                window.location.href = 'http://localhost:8000/'
            }
        });
    });
}



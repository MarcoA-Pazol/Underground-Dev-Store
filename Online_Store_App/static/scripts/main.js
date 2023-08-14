document.addEventListener('DOMContentLoaded', () => {
    const loginIcon = document.getElementById('login_icon');
    const sesionAcordeon = document.querySelector('.sesion_acordion');

    loginIcon.addEventListener('click', () => {
        if (sesionAcordeon.style.display === 'block') {
            sesionAcordeon.style.display = 'none';
        } else {
            sesionAcordeon.style.display = 'block';
        }
    });
});
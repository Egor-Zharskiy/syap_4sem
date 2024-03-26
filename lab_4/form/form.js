document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    function isValidPhoneNumber(phoneNumber) {
        if (!/^\d+$/.test(phoneNumber)) {
            return 'Phone number should contain only digits.';
        }

        return null; // Возвращаем null, если нет ошибок
    }

    function isValidPassword(password) {
        if (password.length < 6) {
            return 'Password should be at least 6 characters long.';
        }

        return null; // Возвращаем null, если нет ошибок
    }

    registerForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const fullName = registerForm.querySelector('[name="fullName"]').value.trim();
        const phoneNumberElement = registerForm.querySelector('[name="phoneNumber"]');
        const phoneNumber = phoneNumberElement ? phoneNumberElement.value.trim() : '';
        const emailElement = registerForm.querySelector('[name="email"]');
        const email = emailElement ? emailElement.value.trim() : '';
        const passwordElement = registerForm.querySelector('[name="password"]');
        const password = passwordElement ? passwordElement.value.trim() : '';

        let errorMessage = '';

        if (fullName === '') {
            errorMessage += 'Full Name is required.\n';
        }

        const phoneNumberError = isValidPhoneNumber(phoneNumber);
        if (phoneNumberError) {
            errorMessage += phoneNumberError + '\n';
        }

        // if (!isValidEmail(email)) {
        //     errorMessage += 'Invalid email address.\n';
        // }

        const passwordError = isValidPassword(password);
        if (passwordError) {
            errorMessage += passwordError + '\n';
        }

        if (errorMessage !== '') {
            alert(errorMessage);
            return;
        }

        // Если мы дошли до этого момента, значит форма валидна
        // Можно выполнить дополнительные действия и переключиться на форму авторизации
        alert('Registration successful!');
        registerForm.reset();
        switchForms();
    });

    function switchForms() {
        loginForm.style.display = 'block';
        registerForm.style.display = 'none';
    }
});

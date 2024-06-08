const names = document.querySelector('#name');
const emails = document.querySelector('#email');
const phones = document.querySelector('#phone');
const passwords = document.querySelector('#password');
const confirmPassword = document.querySelector('#confirm-password');

const form = document.querySelector('#signup-form');

const user = (username) => {
    const condition1 = new RegExp("^(?=.{5,})");
    return condition1.test(username);
};

const phoneCheck = (phoneno) => {
    const condition2 = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/;
    return condition2.test(phoneno);
};

const emailCheck = (email) => {
    const condition3 = new RegExp(/\S+@\S+\.\S+/);
    return condition3.test(email);
};

const passwordCheck = (password) => {
    const condition = new RegExp("^(?=.{8,})");
    return condition.test(password);
};

function confirmPasswordCheck(confirmpassword) {
    const password = passwords.value.trim();
    if (password !== confirmpassword) {
        return false;
    }
    return true;
}

const showError = (input, message) => {
    const formgroup = input.parentElement;
    formgroup.classList.remove('success');
    formgroup.classList.add('error');

    // show the error message
    const error = formgroup.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    const formgroup = input.parentElement;

    formgroup.classList.remove('error');
    formgroup.classList.add('success');

    // hide the error message
    const error = formgroup.querySelector('small');
    error.textContent = '';
};

const checkName = () => {
    let valid = false;
    const username = names.value.trim();
    if (!user(username)) {
        showError(names, 'At least 5 characters required');
    } else {
        showSuccess(names);
        valid = true;
    }
    return valid;
};

const checkPhone = () => {
    let valid = false;
    const phoneno = phones.value.trim();
    if (!phoneCheck(phoneno)) {
        showError(phones, 'Invalid phone number');
    } else {
        showSuccess(phones);
        valid = true;
    }
    return valid;
};

const checkEmail = () => {
    let valid = false;
    const email = emails.value.trim();
    if (!emailCheck(email)) {
        showError(emails, 'Invalid email format');
    } else {
        showSuccess(emails);
        valid = true;
    }
    return valid;
};

const checkPassword = () => {
    let valid = false;
    const password = passwords.value.trim();
    if (!passwordCheck(password)) {
        showError(passwords, 'Password should be at least 8 characters long');
    } else {
        showSuccess(passwords);
        valid = true;
    }
    return valid;
};

const checkConfirmPassword = () => {
    let valid = false;
    const confirmPasswordValue = confirmPassword.value.trim();
    if (!confirmPasswordCheck(confirmPasswordValue)) {
        showError(confirmPassword, 'Passwords do not match');
    } else {
        showSuccess(confirmPassword);
        valid = true;
    }
    return valid;
};

form.addEventListener('submit', function (e) {
    e.preventDefault();

    let isNameValid = checkName();
    let isPhoneValid = checkPhone();
    let isEmailValid = checkEmail();
    let isPasswordValid = checkPassword();
    let isConfirmPasswordValid = checkConfirmPassword();

    let isFormValid =
        isNameValid &&
        isPhoneValid &&
        isEmailValid &&
        isPasswordValid &&
        isConfirmPasswordValid;

    if (isFormValid) {
        form.submit();
    }
});


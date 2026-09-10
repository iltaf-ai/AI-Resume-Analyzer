const registerForm = document.getElementById("registerForm");

if (registerForm) {
    const message = document.getElementById("message");
    const registerBtn = document.getElementById("registerBtn");

    registerForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const username = document.getElementById("username").value;
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        registerBtn.disabled = true;
        registerBtn.textContent = "Creating Account...";

        try {
            const response = await fetch("/register", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    username: username,
                    email: email,
                    password: password
                })
            });

            const data = await response.json();

            message.textContent = data.message;

            if (response.ok) {
                registerForm.reset();

                setTimeout(() => {
                    window.location.href = "/login";
                }, 1000);
            }

        } catch (error) {
            message.textContent = "Something went wrong.";
        } finally {
            registerBtn.disabled = false;
            registerBtn.textContent = "Create Account";
        }
    });
}


const loginForm = document.getElementById("loginForm");

if (loginForm) {
    const message = document.getElementById("message");
    const loginBtn = document.getElementById("loginBtn");

    loginForm.addEventListener("submit", async function (event) {
        event.preventDefault();

        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        loginBtn.disabled = true;
        loginBtn.textContent = "Logging in...";

        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            });

            const data = await response.json();

            message.textContent = data.message;

            if (response.ok && data.token) {
                localStorage.setItem("token", data.token);

                setTimeout(() => {
                    window.location.href = "/dashboard";
                }, 500);
            }

        } catch (error) {
            message.textContent = "Something went wrong.";
        } finally {
            loginBtn.disabled = false;
            loginBtn.textContent = "Login";
        }
    });
}
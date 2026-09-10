
const resumeForm = document.getElementById("resumeForm");
const resumeFile = document.getElementById("resumeFile");
const uploadBtn = document.getElementById("uploadBtn");
const message = document.getElementById("message");

resumeForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const file = resumeFile.files[0];

    if (!file) {
        message.textContent = "Please select a PDF file.";
        return;
    }

    const token = localStorage.getItem("token");

    if (!token) {
        window.location.href = "/login";
        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    uploadBtn.disabled = true;
    uploadBtn.textContent = "Analyzing...";

    try {

        const response = await fetch("/upload", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`
            },
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            message.textContent = data.message;
        } else {
            message.textContent = data.detail || data.message;
        }

    } catch (error) {

        message.textContent = "Something went wrong.";

    } finally {

        uploadBtn.disabled = false;
        uploadBtn.textContent = "Analyze Resume";
    }
});


const logoutBtn = document.getElementById("logoutBtn");

logoutBtn.addEventListener("click", function () {

    localStorage.removeItem("token");

    window.location.href = "/login";
});


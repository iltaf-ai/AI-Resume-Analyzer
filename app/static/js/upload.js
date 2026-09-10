
const token = localStorage.getItem("token");

const uploadForm = document.getElementById("uploadForm");
const resumeFile = document.getElementById("resume");
const fileName = document.getElementById("fileName");
const uploadBtn = document.getElementById("uploadBtn");
const message = document.getElementById("message");


if (!token) {
    window.location.href = "/login";
}


resumeFile.addEventListener("change", function () {

    if (resumeFile.files.length > 0) {

        fileName.textContent =
            resumeFile.files[0].name;

    } else {

        fileName.textContent =
            "No file selected";
    }

});


uploadForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    if (resumeFile.files.length === 0) {

        message.textContent =
            "Please select your resume.";

        return;
    }


    const file = resumeFile.files[0];


    if (file.type !== "application/pdf") {

        message.textContent =
            "Only PDF files are allowed.";

        return;
    }


    const formData = new FormData();

    formData.append("file", file);


    uploadBtn.disabled = true;

    uploadBtn.textContent =
        "Analyzing Resume...";

    message.textContent =
        "AI is analyzing your resume. Please wait...";


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

            message.textContent =
                data.message || "Resume analyzed successfully.";

            setTimeout(function () {

                window.location.href =
                    "/analysis";

            }, 1000);

        } else {

            message.textContent =
                data.detail ||
                data.message ||
                "Resume upload failed.";

        }

    } catch (error) {

        message.textContent =
            "Something went wrong. Please try again.";

    } finally {

        uploadBtn.disabled = false;

        uploadBtn.textContent =
            "Analyze Resume";

    }

});


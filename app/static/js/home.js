
const registerButtons = document.querySelectorAll(
    'a[href="/register"]'
);

registerButtons.forEach(button => {

    button.addEventListener("click", function () {
        console.log("Opening registration page");
    });

});


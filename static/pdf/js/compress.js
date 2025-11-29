const dropzone = document.getElementById("dropzone");
const fileInput = document.getElementById("fileInput");
const filename = document.getElementById("filename");
const submitBtn = document.getElementById("submitBtn");

// Enable button function
function enableButton() {
    submitBtn.disabled = false;
    submitBtn.classList.add("enabled");
}

dropzone.addEventListener("click", () => fileInput.click());

dropzone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropzone.classList.add("dragover");
});

dropzone.addEventListener("dragleave", () => {
    dropzone.classList.remove("dragover");
});

dropzone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropzone.classList.remove("dragover");

    const file = e.dataTransfer.files[0];

    if (file && file.type === "application/pdf") {
        fileInput.files = e.dataTransfer.files;

        filename.innerText = "Selected: " + file.name;
        filename.style.display = "block";

        enableButton();
    } else {
        alert("Please upload a valid PDF.");
    }
});

fileInput.addEventListener("change", function () {
    if (this.files.length > 0) {
        filename.innerText = "Selected: " + this.files[0].name;
        filename.style.display = "block";

        enableButton();
    }
});
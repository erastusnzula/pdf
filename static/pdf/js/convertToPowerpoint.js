const dropzone = document.getElementById("dropzone");
const fileInput = document.getElementById("fileInput");
const filename = document.getElementById("filename");
const submitBtn = document.getElementById("submitBtn");

function enableButton() {
    submitBtn.disabled = false;
    submitBtn.classList.add("enabled");
}
function disableButton() {
    submitBtn.disabled = true;
    submitBtn.classList.remove("enabled");
}

dropzone.onclick = () => fileInput.click();

dropzone.addEventListener("dragover", e => {
    e.preventDefault();
    dropzone.classList.add("dragover");
});
dropzone.addEventListener("dragleave", () => dropzone.classList.remove("dragover"));

dropzone.addEventListener("drop", e => {
    e.preventDefault();
    dropzone.classList.remove("dragover");

    const file = e.dataTransfer.files[0];
    if (!file || file.type !== "application/pdf") {
        alert("Please upload a valid PDF.");
        return;
    }

    fileInput.files = e.dataTransfer.files;
    filename.style.display = "block";
    filename.textContent = "Selected: " + file.name;

    enableButton();
});

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        filename.style.display = "block";
        filename.textContent = "Selected: " + fileInput.files[0].name;
        enableButton();
    } else {
        filename.style.display = "none";
        disableButton();
    }
});
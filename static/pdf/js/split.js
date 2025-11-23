// Drag & Drop logic
const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");
const preview = document.getElementById("preview");

dropArea.onclick = () => {
    fileInput.click()
    document.getElementById("successMessage").style.display = "none";
};


dropArea.addEventListener("dragover", e => {
    e.preventDefault();
    dropArea.style.background = "#e4efff";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.style.background = "#f0f6ff";
});

dropArea.addEventListener("drop", e => {
    e.preventDefault();
    dropArea.style.background = "#f0f6ff";
    fileInput.files = e.dataTransfer.files;
    showPreview();
});

fileInput.onchange = showPreview;

function showPreview() {
    const file = fileInput.files[0];
    if (file) preview.textContent = "Selected: " + file.name;
}

// Submit
document.getElementById("submitBtn").onclick = function(){
    document.getElementById("submitBtn").innerText = "Splitting please wait..."
    const file = fileInput.files[0];
    const parts = document.getElementById("partsCount").value;

    if (!file){ alert("Please upload a PDF file."); return; }
    if (!parts || parts < 2){ alert("Enter a valid number of parts."); return; }

    const formData = new FormData();
    formData.append("pdf", file);
    formData.append("parts", parts);
    formData.append("csrfmiddlewaretoken",
        document.querySelector("[name=csrfmiddlewaretoken]").value
      );
    

    fetch("/split/", {
        method: "POST",
        body: formData,
    }).then(res => res.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement("a");
        a.href = url;
        a.download = "split_pdf.zip";
        a.click();
        document.getElementById("submitBtn").innerText = "Split"
        document.getElementById("successMessage").style.display = "block";
    }).catch(err => console.error(err));
};

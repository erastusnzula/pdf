const uploadArea = document.getElementById("uploadArea");
const pdfInput = document.getElementById("pdfInput");
const fileName = document.getElementById("fileName");
const passwordInput = document.getElementById("passwordInput");
const encryptBtn = document.getElementById("encryptBtn");
const encryptForm = document.getElementById("encryptForm");

let selectedPDF = null;

/* --- Drag and drop events --- */
uploadArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  uploadArea.style.background = "#e0f0ff";
});

uploadArea.addEventListener("dragleave", () => {
  uploadArea.style.background = "#f8fbff";
});

uploadArea.addEventListener("drop", (e) => {
  e.preventDefault();
  selectedPDF = e.dataTransfer.files[0];
  pdfInput.files = e.dataTransfer.files;
  fileName.textContent = selectedPDF.name;
  validateForm();
});

/* Manual browse selection */
pdfInput.addEventListener("change", () => {
  selectedPDF = pdfInput.files[0];
  fileName.textContent = selectedPDF.name || "";
  validateForm();
});

/* Enable submit only when PDF + password exist */
function validateForm() {
  if (selectedPDF && passwordInput.value.trim() !== "") {
    encryptBtn.disabled = false;
    encryptBtn.classList.add("enabled");
  } else {
    encryptBtn.disabled = true;
    encryptBtn.classList.remove("enabled");
  }
}

passwordInput.addEventListener("keyup", validateForm);

/* Auto-download after submitting */
encryptForm.addEventListener("submit", async function(e) {
  e.preventDefault();

  const formData = new FormData(encryptForm);

  const response = await fetch("", {
    method: "POST",
    body: formData
  });

  const blob = await response.blob();
  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "encrypted.pdf";
  a.click();
  URL.revokeObjectURL(url);
});

const drop = document.getElementById("dropZone");
const fileInput = document.getElementById("pdf");
const fileName = document.getElementById("fileName");
const submitBtn = document.getElementById("submitBtn");

drop.addEventListener("click", () => fileInput.click());

drop.addEventListener("dragover", e => {
  e.preventDefault();
  drop.style.background = "#dcecff";
});

drop.addEventListener("dragleave", e => {
  drop.style.background = "#eef6ff";
});

drop.addEventListener("drop", e => {
  e.preventDefault();
  drop.style.background = "#eef6ff";

  const file = e.dataTransfer.files[0];
  fileInput.files = e.dataTransfer.files;

  fileName.textContent = file.name;
  submitBtn.disabled = false;
});

fileInput.addEventListener("change", () => {
  if (fileInput.files.length > 0) {
    fileName.textContent = fileInput.files[0].name;
    submitBtn.disabled = false;
  }
});
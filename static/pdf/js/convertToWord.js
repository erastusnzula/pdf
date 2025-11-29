const dropzone = document.getElementById('dropzone');
const fileInput = document.getElementById('fileInput');
const filename = document.getElementById('filename');
const submitBtn = document.getElementById('submitBtn');

function enableSubmit() {
    submitBtn.disabled = false;
    submitBtn.classList.add('enabled');
}
function disableSubmit() {
    submitBtn.disabled = true;
    submitBtn.classList.remove('enabled');
}

dropzone.addEventListener('click', () => fileInput.click());

dropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.classList.add('dragover');
});
dropzone.addEventListener('dragleave', () => dropzone.classList.remove('dragover'));
dropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.classList.remove('dragover');

    const file = e.dataTransfer.files[0];
    if (!file) return;

    if (file.type !== 'application/pdf') {
        alert('Please upload a PDF file.');
        return;
    }

    fileInput.files = e.dataTransfer.files;
    filename.textContent = 'Selected: ' + file.name;
    filename.style.display = 'block';
    enableSubmit();
});

fileInput.addEventListener('change', function() {
    if (this.files && this.files.length > 0) {
        const f = this.files[0];
        filename.textContent = 'Selected: ' + f.name;
        filename.style.display = 'block';
        enableSubmit();
    } else {
        filename.style.display = 'none';
        disableSubmit();
    }
});

// Optional: client-side size check (example: 50MB limit)
document.getElementById('convertForm').addEventListener('submit', function(e) {
    const f = fileInput.files[0];
    if (!f) {
        e.preventDefault();
        alert('Please select a PDF first.');
        return;
    }
    const maxBytes = 50 * 1024 * 1024; // 50MB
    if (f.size > maxBytes) {
        e.preventDefault();
        alert('File too large. Please upload a file smaller than 50MB.');
        return;
    }

    // Let the form submit normally (server will convert and return .docx)
});
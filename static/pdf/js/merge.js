
  
const MAX_SIZE = 20 * 1024 * 1024; // 20MB

const form = document.getElementById('mergeForm');
const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('fileInput');
const filesContainer = document.getElementById('files');
const browseBtn = document.getElementById('browseBtn');
const clearBtn = document.getElementById('clearBtn');
const browseText = document.getElementById('browseText');
const loader = document.getElementById('loader');
const successMsg = document.getElementById('successMsg');
const mergeBtn = document.getElementById("mergeBtn");

let files = [];

function formatBytes(bytes){
  const k = 1024, sizes = ['B','KB','MB','GB'];
  const i = Math.floor(Math.log(bytes)/Math.log(k));
  return (bytes/Math.pow(k,i)).toFixed(2)+' '+sizes[i];
}

function updateUI(){
  filesContainer.innerHTML = '';

  if (files.length === 0) {
    filesContainer.innerHTML =
      '<div style="color:var(--muted);padding:12px;border-radius:8px">No files selected</div>';
    return;
  }
  mergeBtn.disabled = false;
  mergeBtn.classList.add("enabled");

  files.forEach((file, idx)=>{
    const card = document.createElement('div');
    card.className = 'file-card';

    const thumb = document.createElement('div');
    thumb.className = 'thumb';
    thumb.textContent = "PDF";

    const meta = document.createElement('div');
    meta.className = 'meta';

    const name = document.createElement('b');
    name.textContent = file.name;

    const info = document.createElement('small');
    info.textContent = formatBytes(file.size);

    meta.appendChild(name);
    meta.appendChild(info);

    const actions = document.createElement('div');
    actions.className = 'file-actions';

    const remove = document.createElement('button');
    remove.className = 'remove';
    remove.textContent = 'Remove';
    remove.onclick = () => { files.splice(idx,1); updateUI(); };

    actions.appendChild(remove);

    card.appendChild(thumb);
    card.appendChild(meta);
    card.appendChild(actions);

    filesContainer.appendChild(card);
  });
}



function addFiles(selected){
  [...selected].forEach(f=>{
    if (!f.type.includes("pdf")){
      alert(`${f.name} is not a PDF file`);
      return;
    }
    if (f.size > MAX_SIZE){
      alert(`${f.name} is too large`);
      return;
    }
    files.push(f);
  });
  updateUI();
}

function clearAll(){
  files = [];
  updateUI();
}

// Drag & drop events
['dragenter','dragover'].forEach(ev=>{
  dropArea.addEventListener(ev, e=>{
    e.preventDefault();
    dropArea.classList.add('highlight');
  });
});

['dragleave','drop'].forEach(ev=>{
  dropArea.addEventListener(ev, e=>{
    e.preventDefault();
    dropArea.classList.remove('highlight');
  });
});

dropArea.addEventListener('drop', e=>{
  addFiles(e.dataTransfer.files);
});

browseBtn.onclick = ()=> fileInput.click();
browseText.onclick = ()=> fileInput.click();

fileInput.onchange = e=>{
  addFiles(e.target.files);
  fileInput.value = '';
};

clearBtn.onclick = clearAll;

updateUI();

// 🔥 SEND TO DJANGO BACKEND + AUTO-DOWNLOAD
form.addEventListener("submit", async function(e){
  e.preventDefault();

  if (files.length === 0){
    alert("Select at least one PDF");
    return;
  }

  loader.style.display = "block";

  const formData = new FormData();
  files.forEach(f => formData.append("pdfs", f));

  // include CSRF
  formData.append("csrfmiddlewaretoken",
    document.querySelector("[name=csrfmiddlewaretoken]").value
  );

  const res = await fetch(form.action, {
    method: "POST",
    body: formData
  });

  loader.style.display = "none";

  if (!res.ok){
    alert("Error merging PDFs");
    return;
  }

  // AUTO-DOWNLOAD merged PDF
  const blob = await res.blob();
    // Extract filename from response header
    const disposition = res.headers.get("Content-Disposition");
    let filename = "merged.pdf"; // fallback

    if (disposition && disposition.includes("filename=")) {
      filename = disposition
        .split("filename=")[1]
        .split(";")[0]
        .replace(/['"]/g, "");
    }

    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;
    link.style.display = "none";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    clearAll();
    successMsg.innerText = `✅ Files successfully merged as ${filename}!`
    successMsg.style.display = "block";
});

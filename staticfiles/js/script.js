// static/js/translator.js

// === URLs ===
const uploadUrl = window.uploadUrlDjango; // vem do template

// Gera URL de progresso
function progressoUrlBase(filename) {
    return `/progresso_pdf/${encodeURIComponent(filename)}/`;
}

// === Elementos ===
const uploadArea   = document.getElementById('uploadArea');
const pdfFile      = document.getElementById('pdfFile');
const uploadContent= document.getElementById('uploadContent');
const fileInfo     = document.getElementById('fileInfo');
const fileName     = document.getElementById('fileName');
const fileSize     = document.getElementById('fileSize');

const form          = document.getElementById('pdfForm');
const progressWrapper = document.getElementById('progressWrapper');
const progressBar   = document.getElementById('progressBar');
const progressText  = document.getElementById('progressText');
const downloadWrapper = document.getElementById('downloadLinkWrapper');

// === Eventos ===
uploadArea.addEventListener('click', () => pdfFile.click());

pdfFile.addEventListener('change', () => {
    if (pdfFile.files.length > 0) {
        uploadArea.classList.add('file-uploaded');
        uploadContent.classList.add('hidden');
        fileInfo.classList.remove('hidden');
        fileName.textContent = pdfFile.files[0].name;
        fileSize.textContent = (pdfFile.files[0].size / 1024 / 1024).toFixed(2) + " MB";
    }
});

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!pdfFile.files[0]) return alert("Escolha um arquivo PDF.");

    progressWrapper.classList.remove('hidden');
    progressBar.style.width = '0%';
    progressText.textContent = 'Preparando upload...';
    downloadWrapper.innerHTML = '';

    const formData = new FormData();
    formData.append('arquivo', pdfFile.files[0]);
    formData.append('idioma_destino', document.getElementById('selectedLanguageInput').value);

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    try {
        const resp = await fetch(uploadUrl, {
            method: 'POST',
            body: formData,
            headers: { 'X-CSRFToken': csrfToken }
        });

        const data = await resp.json();
        if (data.status !== 'ok') throw new Error('Erro ao enviar arquivo.');

        const filename = data.filename;

        const interval = setInterval(async () => {
            const respProgress = await fetch(progressoUrlBase(filename));
            const progressData = await respProgress.json();

            progressBar.style.width = progressData.progresso + '%';
            progressText.textContent = `Traduzindo PDF... ${progressData.progresso}%`;

            if (progressData.download_link) {
                clearInterval(interval);
                progressBar.style.width = '100%';
                progressText.textContent = `PDF traduzido!`;
                downloadWrapper.innerHTML =
                    `<a href="${progressData.download_link}" download
                        class="bg-green-600 hover:bg-green-700 text-white py-3 px-6 rounded-xl">
                        Baixar PDF Traduzido</a>`;
            }
        }, 500);

    } catch (err) {
        alert(err.message);
        progressWrapper.classList.add('hidden');
        progressBar.style.width = '0%';
        progressText.textContent = '';
    }
});

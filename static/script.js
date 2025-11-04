function toggleControls() {
    const controls = document.getElementById('controls');
    controls.classList.toggle('show');
}

document.getElementById('temperature').oninput = function() {
    document.getElementById('temp-value').textContent = this.value;
};
document.getElementById('top-p').oninput = function() {
    document.getElementById('top-p-value').textContent = this.value;
};
document.getElementById('top-k').oninput = function() {
    document.getElementById('top-k-value').textContent = this.value;
};

function sendMessage() {
    const promptInput = document.getElementById('prompt');
    const prompt = promptInput.value.trim();
    if (!prompt) return;

    const temperature = parseFloat(document.getElementById('temperature').value);
    const topP = parseFloat(document.getElementById('top-p').value);
    const topK = parseInt(document.getElementById('top-k').value);

    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="message user">${prompt}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    fetch('/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
            prompt: prompt,
            temperature: temperature,
            top_p: topP,
            top_k: topK
        })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="message bot">${data.response || data.error}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
        promptInput.value = '';
    })
    .catch(() => {
        chatBox.innerHTML += `<div class="message bot">Error occurred</div>`;
    });
}
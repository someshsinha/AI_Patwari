// Voice Recognition  
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;  
const recognition = new SpeechRecognition();  
recognition.lang = 'hi-IN';  

const voiceBtn = document.getElementById('voiceBtn');  
const voiceInput = document.getElementById('voiceInput');  
const sendBtn = document.getElementById('sendBtn');  
const blockchainData = document.getElementById('blockchainData');  

// Voice to Text  
voiceBtn.addEventListener('click', () => {  
    recognition.start();  
    voiceBtn.textContent = "Listening...";  
});  

recognition.onresult = (event) => {  
    const transcript = event.results[0][0].transcript;  
    voiceInput.value = transcript;  
    voiceBtn.textContent = "🎤 Speak in Hindi";  
};  

// Generate Deed  
sendBtn.addEventListener('click', async () => {  
    const text = voiceInput.value;  
    if (!text) return;  

    const response = await fetch('/generate_deed', {  
        method: 'POST',  
        headers: { 'Content-Type': 'application/json' },  
        body: JSON.stringify({ text })  
    });  

    const result = await response.json();  
    
    if (result.success) {  
        // Show QR  
        window.open(`/deed/${result.deed.id}`, '_blank');  
        // Update blockchain view  
        blockchainData.textContent = JSON.stringify(result.deed, null, 2);  
    }  
});  
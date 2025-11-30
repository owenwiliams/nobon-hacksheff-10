const chatBox = document.querySelector('.chat-box');
const sendBtn = document.getElementById('sendButton');
const userInput = document.getElementById('userInput');
const chatBody = document.querySelector('.chat-box-body');

// Send message
sendBtn.addEventListener('click', () => {
  const text = userInput.value.trim();
  if (!text) return;
  
  const userMessage = document.createElement('div');
  userMessage.classList.add('message', 'user');
  userMessage.textContent = text;
  chatBody.appendChild(userMessage);
  
  userInput.value = '';
  
  const botMessage = document.createElement('div');
  botMessage.classList.add('message', 'bot');
  botMessage.textContent = "Got it! We'll get back to you soon.";
  chatBody.appendChild(botMessage);
  
  chatBody.scrollTop = chatBody.scrollHeight;
});
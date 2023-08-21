// Test func
async function callPythonFunction() {
    const result = await eel.my_python_function('Hello from JS')();
    document.getElementById('output').textContent = result;
}


function setupChatInputListener() {
    const input = document.querySelector('.input-box input');

    input.addEventListener('keydown', function (event) {
        if (event.keyCode === 13) {
            sendMessage();
        }
    });
}

// navigation
async function navigate(page) {
    const contentDiv = document.getElementById('content');
    const response = await eel.load_page(page)();
    contentDiv.innerHTML = response;
}


// ======= CHAT =======


// send message
async function sendMessage() {
    const input = document.querySelector('.input-box input');
    const messageText = input.value.trim();

    if (messageText !== '') {
        const messagesDiv = document.querySelector('.messages');
        const newMessageDiv = document.createElement('div');
        newMessageDiv.classList.add('message', 'sent');
        newMessageDiv.textContent = messageText;
        messagesDiv.appendChild(newMessageDiv);

        // Clear the input field
        input.value = '';

        // Simulate a response after a short delay
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
        const response = await eel.send_msg(messageText)();
        receiveMessage(response);
    }
}

// receive message
async function receiveMessage(answer) {
    const messagesDiv = document.querySelector('.messages');
    const newMessageDiv = document.createElement('div');
    newMessageDiv.classList.add('message', 'received');
    newMessageDiv.textContent = answer;
    messagesDiv.appendChild(newMessageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

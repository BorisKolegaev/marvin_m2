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
        const response = await eel.send_message(messageText)();
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

//  VOICE
// animation


let animationPaused = false;

eel.expose(toggleAnimation);
function toggleAnimation() {
    const circle = document.getElementById('circle');
	element.classList.remove("spin");
}

eel.expose(pulse);
function pulse() {
  var element = document.getElementById("circle");
  /*element.classList.remove("spin");*/
  element.classList.add("pulse");
}

eel.expose(spin);
function spin() {
  var element = document.getElementById("circle");
  /*element.classList.remove("pulse");*/
  element.classList.add("spin");
}

eel.expose(stop_pulse);
function stop_pulse() {
  var element = document.getElementById("circle");
  element.classList.remove("pulse");
}

eel.expose(stop_spin);
function stop_spin() {
  var element = document.getElementById("circle");
  element.classList.remove("spin");
}

async function start_voice_control() {
    const response = await eel.start_voice_control()();
}

async function stop_voice_control() {
    const response = await eel.stop_voice_control()();
}


// ADMIN PANEL

// gen_image
async function gen_image() {
    const input = document.querySelector('#img-prompt');
    const img_prompt = input.value.trim();
    if (img_prompt !== '') {
        const response = await eel.gen_image(img_prompt)();
        const generatedImg = document.getElementById('generated-img');
        generatedImg.src = 'static/img.jpg'
    }
}

// gen_txt
async function gen_txt() {
    const input = document.querySelector('#text-prompt');
    const txt_prompt = input.value.trim();
    if (txt_prompt !== '') {
        const response = await eel.gen_txt(txt_prompt)();
        const generatedTxt = document.getElementById('generated-text');
        console.log(response);
        generatedTxt.value = response;
    }
}

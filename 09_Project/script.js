const chat = document.getElementById("chat");

function sendMessage(){

    const input = document.getElementById("question");

    const text = input.value.trim();

    if(text==="") return;

    chat.innerHTML += `
        <div class="user-message">
            ${text}
        </div>
    `;

    input.value="";

    // Dummy Response
    setTimeout(()=>{

        chat.innerHTML += `
            <div class="bot-message">
                This response will come from your RAG backend.
            </div>
        `;

        chat.scrollTop = chat.scrollHeight;

    },800);

}
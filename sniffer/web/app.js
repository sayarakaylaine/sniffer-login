// Adiciona um "listener" para o evento de envio do formulário
document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Cria um objeto 'data' com os dados do formulário (usuário e senha)
    const data = {
      username: document.getElementById('username').value,  
      password: document.getElementById('password').value,
    };

    // Envia os dados para o servidor via HTTP POST usando fetch
    fetch('http://localhost:5000/login', {
      method: 'POST',  // Define o método da requisição como POST
      headers: { 'Content-Type': 'application/json' },  // Especifica que estamos enviando JSON
      body: JSON.stringify(data),  // Converte o objeto 'data' para uma string JSON
    })
    .then(res => alert("Requisição enviada!"));  // Exibe um feedback
});

const BASE_URL = "http://localhost:5000/produtos"; // Altere para sua URL base se necessário

// Função para criptografar o código
async function encryptCodigo(codigo) {
    const encoder = new TextEncoder();
    const data = encoder.encode(codigo);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
}

// Adicionar Produto
document.getElementById("add-product-form")?.addEventListener("submit", async (event) => {
    event.preventDefault();

    const codigo = document.getElementById("codigo").value;
    const nome = document.getElementById("nome").value;
    const preco = document.getElementById("preco").value;
    const estoque = document.getElementById("estoque").value;

    try {
        // Criptografar o código
        const encryptedCodigo = await encryptCodigo(codigo);

        const response = await axios.post(`${BASE_URL}/add`, {
            codigo: encryptedCodigo,
            nome,
            preco,
            estoque
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        });
        alert("Produto adicionado com sucesso!");
        event.target.reset();
    } catch (error) {
        alert("Erro ao adicionar produto: " + error.response.data.error);
    }
});

// Buscar Produto
document.getElementById("search-product-form")?.addEventListener("submit", async (event) => {
    event.preventDefault();

    const codigo = document.getElementById("codigo").value;

    try {
        // Criptografar o código
        const encryptedCodigo = await encryptCodigo(codigo);

        const response = await axios.get(`${BASE_URL}/produto`, { params: { codigo: encryptedCodigo } });
        localStorage.setItem("produto", JSON.stringify(response.data));
        window.location.href = "/frontend/templates/mostrar_produto.html";
    } catch (error) {
        alert("Erro ao buscar produto: " + error.response.data.error);
    }
});

// Mostrar Produto
if (window.location.pathname.endsWith("/mostrar_produto.html")) {
    const produto = JSON.parse(localStorage.getItem("produto"));

    if (produto) {
        document.getElementById("product-details").innerHTML = `
            <p><strong>Código:</strong> ${produto.codigo}</p>
            <p><strong>Nome:</strong> ${produto.nome}</p>
            <p><strong>Preço:</strong> ${produto.preco}</p>
            <p><strong>Estoque:</strong> ${produto.estoque}</p>
        `;
    } else {
        document.getElementById("product-details").innerHTML = "<p>Produto não encontrado.</p>";
    }
}

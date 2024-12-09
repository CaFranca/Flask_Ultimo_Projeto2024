// Função para abrir o modal e exibir os detalhes do produto
function abrirModal(produto) {
    document.getElementById("produtoNome").textContent = produto.nome;
    document.getElementById("produtoDescricao").textContent = produto.descricao;
    document.getElementById("produtoPreco").textContent = produto.preco;
    document.getElementById("produtoModal").style.display = 'block'; // Exibe o modal
}

// Função para fechar o modal
function fecharModal() {
    document.getElementById("produtoModal").style.display = 'none'; // Oculta o modal
}

// Adiciona os eventos de clique nos botões "Ver Detalhes"
document.querySelectorAll(".detalhes-btn").forEach(button => {
    button.addEventListener('click', function() {
        const produtoId = this.getAttribute('data-id'); // Pega o ID do produto
        // Faz uma requisição AJAX para obter os detalhes do produto
        fetch(`/produto/${produtoId}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error); // Se o produto não for encontrado, exibe um alerta
                } else {
                    abrirModal(data); // Caso contrário, exibe o modal com os detalhes
                }
            })
            .catch(error => console.error('Erro ao carregar detalhes:', error));
    });
});

// Fechar o modal ao clicar no botão "Fechar"
document.getElementById("fecharModal").addEventListener('click', fecharModal);

// Fechar o modal ao clicar fora do conteúdo do modal
window.onclick = function(event) {
    if (event.target === document.getElementById("produtoModal")) {
        fecharModal();
    }
};

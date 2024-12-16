function toggleContent(button) // Declara a função para mostrar/ocultar o conteúdo
{
  const targetId = button.getAttribute('data-target'); // Verifica se foi selecionado o grupo "formulario1" (Livro, Categoria, Autor) ou "formulario2" (Empréstimo, AdicionarUsuário+)
  const content = document.getElementById(targetId); // Seleciona a div formulario1 ou formulario2

  content.classList.toggle('show'); // Liga ou desliga o "show" (mostrar). Quando show está ligado, nada mais tem do que o mesmo estilo da div normal.
  // Quando show está "desligado", a div é "formularios-esconder", e tem display none.
  button.classList.toggle('active'); // Caso o botão seja apertado, ele gira 90º
}

# Calculadora em Python

Uma aplicação de calculadora com interface gráfica desenvolvida em Python e Flet, criada para demonstrar princípios de arquitetura de software, programação orientada a objetos (POO) e persistência de dados.

## 🚀 Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Flet:** Framework para construção da interface gráfica (GUI).

## 💡 Arquitetura e Estrutura do Projeto

Este projeto foi estruturado para separar a lógica de negócio da interface do usuário, seguindo o princípio de **separação de responsabilidades**. Isso garante um código mais limpo, modular e fácil de manter e expandir.

O projeto é dividido em três arquivos principais:

1.  `calculator.py`: Contém a classe `Calculator`, responsável por toda a **lógica de cálculo**. A implementação foi feita sem o uso de `eval()` para garantir maior **segurança e controle** sobre as operações.
2.  `history.py`: Contém a classe `HistoryManager`, que gerencia a **persistência dos dados**. Ela é responsável por salvar e recuperar o histórico de cálculos de um arquivo de texto, demonstrando conhecimento em **entrada/saída de dados (I/O)**.
3.  `main.py`: O arquivo principal, que age como a camada de apresentação. Ele instancia e integra as classes `Calculator` e `HistoryManager` à interface gráfica criada com **Flet**.

## ✨ Funcionalidades

* Realiza operações aritméticas básicas (+, -, x, ÷).
* **Histórico de Cálculos:** Salva cada operação concluída em um arquivo `history.txt`.
* **Lógica Segura:** Implementação de uma lógica de cálculo própria, evitando o uso de `eval()` para maior segurança.
* **Código Modular:** Arquitetura clara com classes e arquivos separados, facilitando a leitura e futuras expansões.

## ⚙️ Como Executar

1.  Clone este repositório.
2.  Certifique-se de ter o Python instalado.
3.  Instale as dependências com pip:
    `pip install flet`
4.  Execute a aplicação:
    `python main.py`

---

Com essa nova estrutura, você mostra para o recrutador que entende de arquitetura, POO, segurança, I/O de arquivos e organização de código em Python. Isso eleva seu projeto a um nível profissional e o destaca de verdade.
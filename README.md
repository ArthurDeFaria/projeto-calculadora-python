# Calculadora em Python

Uma aplicação de calculadora com interface gráfica desenvolvida em Python e Flet, criada para demonstrar princípios de arquitetura de software, programação orientada a objetos (POO) e persistência de dados.

---

## 🚀 Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **Flet:** Framework para construção da interface gráfica (GUI).

---

## 💡 Arquitetura e Estrutura do Projeto

Este projeto foi estruturado para separar a lógica de negócio da interface do usuário, seguindo o princípio de **separação de responsabilidades**. Isso garante um código mais limpo, modular e fácil de manter e expandir.

O projeto é dividido em três arquivos principais:

* **`calculator.py`**: Contém a classe `Calculator`, responsável por toda a **lógica de cálculo**. A implementação foi feita sem o uso de `eval()` para garantir maior **segurança e controle** sobre as operações.
* **`history.py`**: Contém a classe `HistoryManager`, que gerencia a **persistência dos dados**. Ela é responsável por salvar e recuperar o histórico de cálculos de um arquivo de texto, demonstrando conhecimento em **entrada/saída de dados (I/O)**.
* **`main.py`**: O arquivo principal, que age como a camada de apresentação. Ele instancia e integra as classes `Calculator` e `HistoryManager` à interface gráfica criada com Flet.

---

## ✨ Funcionalidades

* Realiza operações aritméticas básicas (+, -, x, ÷).
* **Histórico de Cálculos:** Salva cada operação concluída em um arquivo `history.txt`.
* **Lógica Segura:** Implementação de uma lógica de cálculo própria, evitando o uso de `eval()` para maior segurança.
* **Código Modular:** Arquitetura clara com classes e arquivos separados, facilitando a leitura e futuras expansões.

---

## 🎨 Design e Usabilidade Aprimorados

Além da arquitetura robusta, a interface do usuário foi aprimorada com foco em design e usabilidade. O projeto agora utiliza:

* **Padrões de Cores e Estilo:** Cores e bordas arredondadas foram aplicadas para criar um visual moderno e consistente.
* **Constantes de Design:** Parâmetros como tamanho dos botões e cores foram padronizados usando constantes, tornando o código mais limpo e facilitando futuras alterações de design.
* **Melhoria de Acessibilidade:** O tamanho do texto nos botões foi aumentado para garantir maior legibilidade e uma experiência de usuário mais acessível.

---

## ⚙️ Como Executar

1.  Clone este repositório.
2.  Certifique-se de ter o Python instalado.
3.  Instale as dependências com pip: `pip install flet`
4.  Execute a aplicação: `python main.py`
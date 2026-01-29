# ⚽ Soccer Player Statistics – Python

Sistema simples em Python para cadastro e análise de estatísticas de jogadores de futebol, permitindo registrar gols por partida, calcular totais e consultar o desempenho individual de cada jogador.

---

## 📌 Funcionalidades

- Cadastro de jogadores
- Registro de gols por partida
- Cálculo automático do total de gols
- Listagem geral dos jogadores com estatísticas
- Consulta detalhada de um jogador específico
- Validação de entradas do usuário

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Estruturas de dados nativas:
  - Listas (`list`)
  - Dicionários (`dict`)
- Controle de fluxo:
  - `while`
  - `for`
  - `enumerate`
- Boas práticas de cópia de dados (`copy()`)

---

## ▶️ Como Executar o Projeto

1. Certifique-se de ter o Python 3 instalado:
   ```bash
   python --version
   ```
2. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/soccer-player-statistics-python.git
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd soccer-player-statistics-python
   ```
4. Execute o programa:
   ```bash
   python main.py
   ```
   
---

## 🧠 Exemplo de Uso

```text
Nome do Jogador: João
Quantas partidas João: 3
Quantos gols na partida 1: 1
Quantos gols na partida 2: 0
Quantos gols na partida 3: 2
Quer continuar? [S/N] N
```

Saída esperada:

```text
COD NOME       GOLS        TOTAL
0   João       [1, 0, 2]      3
```
---

## 🔎 Consulta de Jogador

- O sistema permite consultar um jogador pelo código:
```text
Mostrar dados de qual jogador? (999 para parar): 0
-- LEVANTAMENTO DO JOGADOR João
No jogo 1 fez 1 gols
No jogo 2 fez 0 gols
No jogo 3 fez 2 gols
```
## 🎯 Objetivo do Projeto

- Projeto desenvolvido com fins educacionais para praticar:
    - Estruturas de dados em Python
    - Entrada e saída de dados
    - Lógica de programação 
    - Organização de informações em listas e dicionários

## 🚀 Melhorias Futuras

- Refatoração para uso de funções
    - Implementação com Programação Orientada a Objetos (POO)
    - Persistência de dados em arquivos (JSON ou CSV)
    - Interface gráfica 
    - Melhor tratamento de erros

## 👨‍💻 Autor

**Elias Rodrigues**

Projeto desenvolvido para estudo e prática em Python.

## 📄 Licença

Este projeto é livre para uso educacional e pessoal.
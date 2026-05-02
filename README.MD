# 💧 Controle de Níveis de Água

Este projeto foi desenvolvido com o objetivo de simular o monitoramento de um reservatório de água utilizando Python <img width="22" height="22" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />.

O sistema exibe no terminal mensagens de alerta com cores diferentes, conforme o nível de água identificado, facilitando a visualização da situação do reservatório.

---

## 📌 Objetivo da Atividade

Desenvolver um sistema simples que:

- Utilize uma lista para representar os níveis do reservatório
- Associe cada nível a uma mensagem de alerta
- Exiba mensagens coloridas no terminal
- Utilize a biblioteca `colorama`
- Aplique funções

---

## 🛠 Tecnologias utilizadas

- Python 3<img width="22" height="22" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" />
- Biblioteca `colorama`

---

## 📚 Conceitos aplicados

- Bibliotecas externas
- Listas
- Funções
- Estruturas condicionais (`if`, `elif`, `else`)

---

## ⚙️ Funcionamento

O sistema trabalha com cinco níveis de água:

| Nível | Situação               | Cor       |
|------|----------------------|----------|
| 1    | Muito baixo (crítico) | Vermelho |
| 2    | Baixo                | Amarelo |
| 3    | Médio                | Verde |
| 4    | Alto                 | Ciano |
| 5    | Muito alto (alerta)  | Azul |

Cada nível retorna uma mensagem específica com sua respectiva cor no terminal.

---

## ▶️ Execução do programa

### 1. Instale a biblioteca necessária

```bash
pip install colorama
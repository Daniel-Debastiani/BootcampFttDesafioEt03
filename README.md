# BootcampFttDesafioEt02

# API de Gerenciamento de Personagens

Esta é uma API desenvolvida em Flask para gerenciar personagens de programas de animação.

## Rotas

- **POST /personagens/criar**: Cria um novo personagem.
- **GET /personagens/obter**: Retorna todos os personagens cadastrados.

## Requisitos

- Python 3.x
- Flask

## Criar um personagem

POST /personagens/criar

{
    "nome": "Goku",
    "descricao": "O lendário guerreiro Saiyajin",
    "imagem": "https://i.pinimg.com/564x/99/4a/bf/994abf73480680ccdc64d6ae3705d04c.jpg",
    "programa": "Dragon Ball Z",
    "animador": "Akira Toriyama"
}


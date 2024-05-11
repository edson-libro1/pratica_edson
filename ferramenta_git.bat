#!/bin/bash

clear

echo "Status do repositório Git:"
git status

# Adiciona todos os arquivos ao staging
git add .

# Limpa a tela
clear

echo "Adicionando arquivos..."

echo "Escreva a mensagem de commit:"
read commit_message

git commit -m "$commit_message"

clear

echo "Status do repositório Git após o commit:"
git status

git push

echo "Atualização realizada com sucesso!"

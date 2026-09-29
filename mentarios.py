# Fluxo que você vai usar 90% do tempo

#   Alterou arquivos:
#       git status

#   Adiciona:
#       git add .

#   Cria commit:
#       git commit -m "Descrição da alteração"

#   Envia para GitHub:
#       git push




# 1. Verificar a situação atual

#   git status

#   Mostra:
#   Em qual branch você está (master ou main)
#   Arquivos modificados
#   Arquivos novos
#   Arquivos prontos para commit

# Exemplo:

# On branch master
#   modified: programa.py
#   Significa que você alterou o arquivo programa.py, mas ainda não salvou essa alteração no Git.

# 2. Ver o histórico de commits

#   git log

#   Mostra todos os commits.

#   Versão resumida:

#   git log --oneline

#   Exemplo:
#   a3f4b21 Corrigido bug
#   b7c9d55 Primeiro commit

# 3. Adicionar arquivos para o commit
#   Adicionar um arquivo específico:

#   git add programa.py

#   Adicionar tudo:
   
#   git add .
   
#   O ponto (.) significa: "adicione todas as alterações da pasta atual".

# 4. Criar um commit:
#   Depois do add:
   
#   git commit -m "Adiciona sistema de cadastro"
   
#   O commit é como uma foto do projeto naquele momento.

# 5. Enviar para o GitHub:
 
#   git push

#   Ou:

#   git push origin master

#   ou

#   git push origin main

#   (depende do nome da sua branch)

# 6. Baixar alterações do GitHub:

#   git pull

#   Busca e atualiza seu projeto local.

# 7. Ver qual branch você está usando:

#   git branch

#   Exemplo:
#   * master
#   O asterisco mostra a branch atual.

# 8. Ver para qual GitHub o projeto está conectado:

#   git remote -v

#   Exemplo:
#   origin  https://github.com/rafdasil/rafael.git (fetch)
#   origin  https://github.com/rafdasil/rafael.git (push)

#   Lembra daquele repositório que você estava tentando enviar? Esse comando confirma se ele está conectado corretamente.

# 9. Criar uma nova branch

#   git branch nova-funcionalidade

# 10. Trocar de branch:

#   git checkout nova-funcionalidade

#   ou na forma moderna:

#   git switch nova-funcionalidade

# 11. Criar e entrar na branch de uma vez:

#   git switch -c nova-funcionalidade
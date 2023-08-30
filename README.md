
# Seletive - Django

O Seletive é um sistema robusto desenvolvido em Django, projetado para otimizar o gerenciamento de candidaturas em vagas de emprego. Ao oferecer uma abordagem organizada e eficaz, o Seletive simplifica o processo seletivo, desde o cadastro de empresas até o acompanhamento das tarefas e comunicação.

## Tecnologias e práticas utilizadas

 - Python
 - Django 
 - SQLite
 - HTML/CSS
 
## Funcionalidades
 - Cadastrar/Excluir empresas;
 - Adicionar vagas disponíveis;
 - Fazer filtros de empresas de acordo com as tecnologias utilizadas;
 - Criar tarefas para ser feitas durante o processo seletivo;
 - Envio de emails para as empresas;

## Requisitos
### Para executar o projeto em sua máquina local, você precisará ter o Python 3 instalado. Além disso, recomendamos utilizar um ambiente virtual para instalar as dependências necessárias.

## Instalação

### Clone este repositório em sua máquina local.

- Crie um ambiente virtual:
```
python3 -m venv myenv
```
- Ative o ambiente virtual:
```
source myenv/bin/activate
```
- Instale as dependências:
```
pip install -r requirements.txt
```
- Execute as migrações do banco de dados:
```
python manage.py migrate
```
- Crie um superusuário:
```
python manage.py createsuperuser
```
- Execute o servidor:
```
python manage.py runserver
```
## Utilização
Após a instalação, o sistema estará disponível em seu navegador através do endereço http://localhost:8000. Para acessar a área administrativa, utilize as credenciais do superusuário criado na instalação.

## Contribuição
Contribuições são bem-vindas! Se você quiser contribuir para este projeto, por favor siga estas instruções:

- Faça um fork deste repositório.
- Crie um branch com suas alterações:
```git checkout -b minha-alteracao```
- Faça o commit das suas alterações:
```git commit -m 'Minha alteração'```
- Faça o push para o branch:
```git push origin minha-alteracao```
- Abra um pull request para o branch principal.
## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

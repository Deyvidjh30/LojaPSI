# LojaPSI — versão corrigida

Projeto Django da LojaPSI para estudos.

## O que foi corrigido

- Categoria e fabricante agora possuem telas próprias para listar, cadastrar, editar e excluir.
- Os links de Categoria e Fabricante do menu agora apontam para rotas que realmente existem.
- Cadastro e edição de produto agora validam categoria e fabricante antes de salvar.
- A categoria e o fabricante selecionados são realmente vinculados ao produto.
- Corrigido o salvamento da edição de produto, que podia falhar silenciosamente.
- Busca e filtros de produto foram corrigidos.
- Validação de preço e upload de imagem foram simplificados e corrigidos.
- Corrigido o formulário de edição do usuário para usar os dados enviados pelo POST.
- Admin ganhou pesquisa e filtros para categoria, fabricante e produto.
- Removidos `__pycache__` e arquivos compilados do projeto entregue.

## Rodar no GitHub Codespaces

Entre na pasta que contém o arquivo `manage.py` antes de executar os comandos abaixo.

### 1. Conferir a pasta

```bash
ls
```

Deve aparecer algo parecido com:

```text
manage.py  loja  lojaAdmin  requirements.txt
```

Se `manage.py` não aparecer:

```bash
cd LojaPSI-main
```

### 2. Criar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Verificar o projeto

```bash
python manage.py check
```

O resultado esperado termina com:

```text
System check identified no issues (0 silenced).
```

### 5. Atualizar o banco

```bash
python manage.py makemigrations
python manage.py migrate
```

Se aparecer `No changes detected`, está tudo certo.

### 6. Criar um administrador

Se ainda não existir:

```bash
python manage.py createsuperuser
```

### 7. Iniciar

```bash
python manage.py runserver 0.0.0.0:8000
```

No Codespaces, abra a porta `8000` pelo botão **Open in Browser**.

## Ordem recomendada para testar

1. Acesse `/admin/` e faça login.
2. Acesse **Categoria** e cadastre uma categoria.
3. Acesse **Fabricante** e cadastre um fabricante.
4. Acesse **Produto > Novo produto**.
5. Confira as duas listas suspensas.
6. Crie um produto com categoria e fabricante.
7. Edite o produto e troque categoria/fabricante.
8. Abra **Ver** e confirme os dados.
9. Teste os filtros de categoria e fabricante.

## Se você já tinha um banco antigo

Não apague `db.sqlite3` se quiser preservar os dados.

Primeiro tente:

```bash
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

Se quiser começar do zero, faça backup:

```bash
cp db.sqlite3 db.sqlite3.backup
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

## Estrutura

```text
LojaPSI-main/
├── manage.py
├── requirements.txt
├── loja/
│   ├── models/
│   ├── views/
│   ├── urls/
│   ├── templates/
│   └── static/
└── lojaAdmin/
    ├── settings/
    └── urls.py
```

## Rotas principais

- `/` — Home
- `/categoria/` — categorias
- `/fabricante/` — fabricantes
- `/produto/` — produtos
- `/admin/` — painel administrativo
- `/login/` — login
- `/register/` — cadastro
- `/carrinho/` — carrinho
- `/favorito/` — favoritos

## Codespaces

Use `0.0.0.0:8000` no `runserver`. O `settings.py` já possui os domínios `github.dev` e `app.github.dev` na configuração de CSRF.

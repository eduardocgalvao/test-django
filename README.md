# 🐍 Estudos de Django

Este repositório foi criado para documentar meu aprendizado com o framework Django. Aqui, coloco em prática conceitos de desenvolvimento web backend, seguindo o padrão MVT (Model-View-Template).

## 🚀 Tecnologias Utilizadas

*   **Python 3.x**
*   **Django 5.x**
*   **SQLite** (Banco de dados padrão)
*   **Virtualenv** (Ambiente virtual)

## 🛠️ Como rodar o projeto localmente

Siga os passos abaixo para configurar o ambiente em sua máquina:

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/test-django.git
    cd test-django
    ```

2.  **Crie e ative o ambiente virtual:**
    ```bash
    # No Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    
    # No Windows
    # python -m venv venv
    # venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install django
    
    # Se tiver um arquivo requirements.txt:
    # pip install -r requirements.txt
    ```

4.  **Execute as migrações (Banco de Dados ):**
    ```bash
    python manage.py migrate
    ```

5.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```
    O projeto estará disponível em `http://127.0.0.1:8000/`.

## 📚 Conceitos Estudados

Até agora, este projeto cobre:

- [x] Configuração de ambiente virtual.
- [x] Criação de Apps e rotas (URLs ).
- [x] Criação de Superuser e gerenciamento pelo Admin.
- [ ] Integração com banco de dados (Models).
- [ ] Criação de Views e Templates.

## ⚠️ Solução de Problemas Comuns

**Erro: `Port already in use`**

Se ao tentar rodar o servidor você receber o erro de porta ocupada, use o comando abaixo para liberar a porta 8000:

```bash
sudo fuser -k 8000/tcp
```

Ou rode em outra porta:

```bash
python manage.py runserver 8001
```

---
Feito com ☕ por Eduardo Galvão

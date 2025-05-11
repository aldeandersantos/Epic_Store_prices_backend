# 🎮 Epic Store Backend 🚀

## 📋 Visão Geral

Este projeto é um backend desenvolvido em Django para interagir com a Epic Games Store API, permitindo listar jogos em promoção e gerenciar um catálogo local de jogos da Epic Games. 🕹️

## ✨ Funcionalidades

- 🔍 Buscar jogos da Epic Games Store
- 📊 Filtrar jogos com desconto
- 💾 Salvar informações dos jogos no banco de dados
- 📱 API RESTful para integração com aplicativos mobile
- 🗑️ Gerenciamento do catálogo de jogos (listagem, busca, atualização, exclusão)

## 🛠️ Tecnologias Utilizadas

- 🐍 Python 3.x
- 🎯 Django 5.2.1
- 🔄 Django REST Framework 3.16.0
- 🗃️ SQLite (padrão do Django)
- 🔌 Epic Games Store API

## 🚀 Como Começar

### 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/aldeandersantos/Epic_Store_prices_backend.git
cd Epicstore_backend
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py migrate
```

5. Inicie o servidor:
```bash
python manage.py runserver
```

## 🔌 Endpoints da API

### 📋 Listar Todos os Jogos
```
GET /api/games/
```

### 🎯 Obter Jogo Específico
```
GET /api/game/
Body: {"game_slug": "url_slug"}
```

### 🔄 Atualizar Catálogo de Jogos
```
POST /api/update/?start=0&range=2
```

### 🗑️ Limpar Catálogo
```
DELETE /api/clear/
```

## 📱 Integração com Frontend

Este backend foi projetado para ser consumido por um aplicativo mobile Android, oferecendo uma experiência semelhante ao aplicativo "Sales for Steam". ✨

## 🔧 Configuração

Para configurar variáveis de ambiente, crie um arquivo `.env` na raiz do projeto:

```
DEBUG=True
SECRET_KEY=your-secret-key
```

## 👨‍💻 Contribuição

Sinta-se à vontade para contribuir com este projeto! 🙌
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes. 📝

## 🙏 Agradecimentos

- 🎮 [epicstore_api](https://github.com/SD4RK/epicstore_api) pela API
- 👾 Todos os desenvolvedores de jogos incríveis!

---

⭐️ Desenvolvido para gamers que adoram boas promoções! ⭐️
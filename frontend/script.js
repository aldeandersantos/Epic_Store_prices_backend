let currentPage = 1;
const PAGE_SIZE = 15;

async function fetchGames(page = 1) {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('games').innerHTML = '';
    try {
        const response = await fetch(`http://localhost:8000/api/games/?page_size=${PAGE_SIZE}&page=${page}`);
        if (!response.ok) throw new Error('Erro ao buscar jogos');
        let games = await response.json();
        console.log('Resposta da API:', games);
        if (games.Content && typeof games.Content === 'string') {
            try {
                games = JSON.parse(games.Content);
            } catch (e) {
                games = [];
            }
        }
        renderGames(games);
    } catch (e) {
        document.getElementById('games').innerHTML = '<p>Erro ao carregar jogos.</p>';
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
}

function renderPagination() {
    const pagDiv = document.getElementById('pagination');
    pagDiv.innerHTML = `
        <button onclick="changePage(currentPage-1)" ${currentPage === 1 ? 'disabled' : ''}>Anterior</button>
        <span>Página ${currentPage}</span>
        <button onclick="changePage(currentPage+1)">Próxima</button>
    `;
}

function changePage(page) {
    if (page < 1) return;
    currentPage = page;
    fetchGames(currentPage);
    renderPagination();
}

function renderGames(games) {
    if (!games.length) {
        document.getElementById('games').innerHTML = '<p>Nenhum jogo encontrado.</p>';
        return;
    }
    document.getElementById('games').innerHTML = games.map(game => {
        let img = game.image_url || game.image || (game.images && game.images[0] && (game.images[0].url || game.images[0])) || 'https://via.placeholder.com/220x120?text=Sem+Imagem';
        let preco = (game.price !== undefined && game.price !== null) ? Number(game.price).toFixed(2) : 'N/A';
        let precoDesconto = (game.discounted_price !== undefined && game.discounted_price !== null) ? Number(game.discounted_price).toFixed(2) : null;
        let precoDescontoHtml = precoDesconto === null
            ? `<span style="font-weight:bold;font-size:1.18rem;">GRÁTIS</span>`
            : `<span style="font-weight:bold;font-size:1.18rem;">R$ ${precoDesconto}</span>`;
        let nomeUrl = encodeURIComponent(game.title || '');
        let link = `https://store.epicgames.com/pt-BR/browse?q=${nomeUrl}&sortBy=relevancy&sortDir=DESC&count=40`;
        return `
            <div class="game-card" onclick="window.open('${link}', '_blank')" style="cursor:pointer;">
                <img src="${img}" alt="${game.title || 'Sem título'}">
                <h2>${game.title || 'Sem título'}</h2>
                <p><strong>Preço atual:</strong> ${precoDescontoHtml}</p>
                <p><strong>Preço padrão:</strong> ${preco !== 'N/A' ? 'R$ ' + preco : 'N/A'}</p>
            </div>
        `;
    }).join('');
}

document.addEventListener('DOMContentLoaded', () => {
    fetchGames(currentPage);
    renderPagination();
});

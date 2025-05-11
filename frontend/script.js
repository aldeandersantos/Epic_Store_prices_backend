async function fetchGames() {
    document.getElementById('loading').style.display = 'block';
    document.getElementById('games').innerHTML = '';
    try {
        const response = await fetch('http://localhost:8000/api/games/');
        if (!response.ok) throw new Error('Erro ao buscar jogos');
        let games = await response.json();
        console.log('Resposta da API:', games); // <-- Adicione esta linha
        // Se vier um objeto com a chave Content, tenta fazer o parse
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

function renderGames(games) {
    if (!games.length) {
        document.getElementById('games').innerHTML = '<p>Nenhum jogo encontrado.</p>';
        return;
    }
    document.getElementById('games').innerHTML = games.map(game => {
        // Tenta encontrar a imagem em diferentes campos
        let img = game.image_url || game.image || (game.images && game.images[0] && (game.images[0].url || game.images[0])) || 'https://via.placeholder.com/220x120?text=Sem+Imagem';
        // Tenta encontrar o preço
        let preco = (game.price !== undefined && game.price !== null) ? Number(game.price).toFixed(2) :
                    (game.discounted_price !== undefined && game.discounted_price !== null) ? Number(game.discounted_price).toFixed(2) : 'N/A';
        return `
            <div class="game-card">
                <img src="${img}" alt="${game.title || 'Sem título'}" style="width:100%;height:120px;object-fit:cover;border-radius:4px 4px 0 0;">
                <h2>${game.title || 'Sem título'}</h2>
                <p><strong>Preço:</strong> ${preco !== 'N/A' ? 'R$ ' + preco : 'N/A'}</p>
            </div>
        `;
    }).join('');
}

// Carrega ao abrir
document.addEventListener('DOMContentLoaded', fetchGames);

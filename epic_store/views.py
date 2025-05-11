from .serializers import GameSerializer
from epicstore_api import EpicGamesStoreAPI
from rest_framework.decorators import api_view
from rest_framework.response import Response
from epic_store.services.game_updater import save_game_from_api
from .models import Game
from datetime import datetime, timezone
import time



@api_view(['GET'])
def list_games(request):
    games = Game.objects.all()
    serializer = GameSerializer(games, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_game(request):
    try:
        api = EpicGamesStoreAPI()
        body_data = request.data
        game_slug = body_data.get('game_slug', [])
        print(f"Game slug: {game_slug}")
        game = api.get_product(game_slug)
        return Response(game, status=200)
    except Game.DoesNotExist:
        return Response({"error": "Game not found."}, status=404)


@api_view(['POST'])
def update_games(request):
    api = EpicGamesStoreAPI(locale='pt-BR', country='BR')
    start = int(request.GET.get("start", 0))
    range_count = int(request.GET.get("range", 2))
    count = 40
    all_games = []

    try:
        for i in range(0, range_count):
            result = api.fetch_store_games(
                start=start,
                count=count,
                sort_by='relevancy',
                sort_dir='DESC',
                with_price=True
            )
            elements = result['data']['Catalog']['searchStore']['elements']
            all_games.extend(elements)
            #time.sleep(1)
            start += count
        if not all_games:
            return Response({"message": "No games found."}, status=404)
        
        jogos_filtrados = []
        agora = datetime.now(timezone.utc)
        for game in all_games:
            price = game.get('price')
            if not price:
                continue
            price_info = price.get('totalPrice', {})
            original = price_info.get('originalPrice')
            discount = price_info.get('discountPrice')
            effective_date = game.get('effectiveDate')

            if original is None or discount is None or effective_date is None:
                continue

            if discount == original:
                continue

            try:
                data_lancamento = datetime.fromisoformat(effective_date.replace('Z', '+00:00'))
                if data_lancamento > agora:
                    continue
            except Exception:
                continue

            jogos_filtrados.append(game)
            save_game_from_api(game)
        nomes_jogos = [game.get('title') for game in jogos_filtrados]
        
        return Response({"filtered_games": nomes_jogos}, status=200)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return Response({"error": str(e)}, status=500)

@api_view(['DELETE'])
def delete_games(request):
    deleted_count, _ = Game.objects.all().delete()
    if deleted_count == 0:
        return Response({"message": "No games to delete."}, status=200)
    return Response({"message": "Games deleted successfully."}, status=200)
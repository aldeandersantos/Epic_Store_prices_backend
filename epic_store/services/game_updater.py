from epic_store.models import Game

def save_game_from_api(game_data):
    title = game_data.get('title')
    slug = game_data.get('urlSlug') or game_data.get('id')
    description = game_data.get('description', '')
    images = game_data.get('keyImages', [])
    image_url = images[0]['url'] if images and 'url' in images[0] else ''
    price_info = game_data.get('price', {}).get('totalPrice', {})
    price = price_info.get('originalPrice', 0) / 100 if price_info.get('originalPrice') else None
    discounted_price = price_info.get('discountPrice', 0) / 100 if price_info.get('discountPrice') else None
    currency = price_info.get('currencyCode', 'BRL')

    game = Game.objects.update_or_create(
        slug=slug,
        defaults={
            'title': title,
            'description': description,
            'image_url': image_url,
            'price': price,
            'discounted_price': discounted_price,
            'currency': currency,
        }
    )
    return game
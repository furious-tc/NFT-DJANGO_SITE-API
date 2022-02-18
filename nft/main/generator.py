import requests
import web3

def filters(req):
    static_attributes = ['Empathy', 'Accountability', 'Ambition', 'Conviction', 'Curiosity', 'Empathy', 'Gratitude', 'Humility', 'Kind Candor', 'Kindness', 'Optimist', 'Patience', 'Self-awareness', 'Tenacity', 'Special']
    static_spectaculars = ['Hologram', 'Bubble Gum', 'Diamond', 'Gold', 'Hologram', 'Lava']
    static_frames = ['Rainbow', 'Black', 'Caviar', 'Champange', 'Clear', 'Emerald', 'Fur', 'Galaxy', 'Gold', 'Granite', 'Marble', 'Neon', 'Pearl', 'Rainbow', 'Silver', 'Wood']

    attributes = (req.getlist('attributes')[0]).split(sep=',', maxsplit=-1)

    spectaculars = (req.getlist('spectaculars')[0]).split(sep=',', maxsplit=-1)
    token_frames = (req.getlist('token-frames')[0]).split(sep=',', maxsplit=-1)
    try:
        cursor = (req.getlist('cursor')[0]).split(sep=',', maxsplit=-1)
    except:
        pass

    attribute = []
    spectacular = []
    token_frame = []

    if '' in attributes:
        attribute = 'Accountability%22%2C%22Ambition%22%2C%22Conviction%22%2C%22Curiosity%22%2C%22Empathy%22%2C%22Gratitude%22%2C%22Humility%22%2C%22Kind%20Candor%22%2C%22Kindness%22%2C%22Optimism%22%2C%22Patience%22%2C%22Self-awareness%22%2C%22Tenacity%22%2C%22Special'
    else:
        for i in attributes:
            if i.capitalize() in static_attributes:
                attribute.append(f'{i.capitalize()}%22,%22')
        attribute = ''.join(attribute)
        attribute = attribute[:-7]
    if '' in spectaculars:
        spectacular = 'Bubble%20Gum%22%2C%22Diamond%22%2C%22Gold%22%2C%22Hologram%22%2C%22Lava'
    else:
        for i in spectaculars:
            if i.capitalize() in static_spectaculars:
                spectacular.append(f'{i.capitalize()}%22,%22')
        spectacular = ''.join(spectacular)
        spectacular = spectacular[:-7]
    if '' in token_frames:
        token_frame = 'Black%22%2C%22Caviar%22%2C%22Champagne%22%2C%22Clear%22%2C%22Emerald%22%2C%22Fur%22%2C%22Galaxy%22%2C%22Gold%22%2C%22Granite%22%2C%22Marble%22%2C%22Neon%22%2C%22Pearl%22%2C%22Rainbow%22%2C%22Silver%22%2C%22Wood'
    else:
        for i in token_frames:
            if i.capitalize() in static_frames:
                token_frame.append(f'{i.capitalize()}%22,%22')
        token_frame = ''.join(token_frame)
        token_frame = token_frame[:-7]

    if '' in cursor:
        url = f"https://api.x.immutable.com/v1/orders?include_fees=true&status=active&sell_token_address=0xac98d8d1bb27a94e79fbf49198210240688bb1ed&sell_metadata=%7B%22Attribute%22%3A%5B%22{attribute}%22%5D%2C%22Spectacular%22%3A%5B%22{spectacular}%22%5D%2C%22Token%20Frame%22%3A%5B%22{token_frame}%22%5D%7D&buy_token_type=ETH&order_by=buy_quantity&direction=asc&page_size=30&cursor="
    else:
        url = f"https://api.x.immutable.com/v1/orders?include_fees=true&status=active&sell_token_address=0xac98d8d1bb27a94e79fbf49198210240688bb1ed&sell_metadata=%7B%22Attribute%22%3A%5B%22{attribute}%22%5D%2C%22Spectacular%22%3A%5B%22{spectacular}%22%5D%2C%22Token%20Frame%22%3A%5B%22{token_frame}%22%5D%7D&buy_token_type=ETH&order_by=buy_quantity&direction=asc&page_size=30&cursor={cursor[0]}"

    return url


def response(request):
    url = 'https://api.x.immutable.com/v1/orders?include_fees=true&status=active&sell_token_address=0xac98d8d1bb27a94e79fbf49198210240688bb1ed&sell_metadata={"Attribute":["Accountability","Ambition","Conviction","Curiosity","Empathy","Gratitude","Humility","Kind Candor","Kindness","Optimism","Patience","Self-awareness","Tenacity","Special"],"Spectacular":["Bubble Gum","Diamond","Gold","Hologram","Lava"],"Token Frame":["Black","Caviar","Champagne","Clear","Emerald","Fur","Galaxy","Gold","Granite","Marble","Neon","Pearl","Rainbow","Silver","Wood"]}&buy_token_type=ETH&page_size=30&cursor='
    if request.GET != {}:
        try:
            url = filters(request.GET)
        except AttributeError:
            pass
        except IndexError:
            pass

    data = requests.get(url.replace('\n', '')).json()
    for i, c in enumerate(data["result"]):
        data_price = c['buy']['data']['quantity']
        price = round(web3.Web3.fromWei(int(data_price), 'ether'), 4)
        data["result"][i]["buy"]["data"]["price"] = price
    return data
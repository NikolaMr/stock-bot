class NED:

    stock_name_ticker_map = {
        'pltr': 'pltr',
        'palantir': 'pltr',
        'tesla': 'tsla',
        'novonordisk': 'novo-b.co',
        'ibm': 'ibm',
        'upwork': 'upwk',
        'upwk': 'upwk',
        'gamestop': 'gme',
        'gme': 'gme',
        'race': 'race',
        'ferrari': 'race',
        'xpeng': 'xpev',
        'xpev': 'xpev',
        'nndm': 'nndm',
        'sofi': 'sofi',
        'nio': 'nio',
        'sony': 'sony',
        'google': 'googl',
        'googl': 'googl',
        'nokia': 'nok',
        'nok': 'nok',
        'rivian': 'rivn',
        'rivn': 'rivn'
    }

    @staticmethod
    def get_ticker_symbol(stock_name_or_symbol):
        return NED.stock_name_ticker_map.get(stock_name_or_symbol.lower())

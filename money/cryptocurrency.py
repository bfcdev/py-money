"""Module defining currencies and currency utilities"""

from enum import Enum

#pylint: disable=too-many-lines


class Coin(Enum):
    """ Enumerates all supported cryptocurrencies"""
    BTC = "BTC"
    XRP = "XRP"
    ETH = "ETH"
    XLM = "XLM"
    BCH = "BCH"
    EOS = "EOS"
    LTC = "LTC"
    BSV = "BSV"
    ADA = "ADA"
    XMR = "XMR"
    TRX = "TRX"
    MIOTA = "MIOTA"
    DASH = "DASH"
    XEM = "XEM"
    BNB = "BNB"
    NEO = "NEO"
    ETC = "ETC"
    ZEC = "ZEC"
    BTG = "BTG"
    XTZ = "XTZ"
    VET = "VET"
    DOGE = "DOGE"
    MKR = "MKR"


class CoinHelper(object):
    """Utilities for cryptocurrencies"""

    _COIN_DATA = {
        Coin.BTC: {
            'display_name': 'Bitcoin',
            'default_fraction_digits': 8,
            'sub_unit': 1e8,
            'mineable': True,
        },
        Coin.XRP: {
            'display_name': 'Ripple',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.ETH: {
            'display_name': 'Ethereum',
            'default_fraction_digits': 8,
            'sub_unit': 1e8,
            'mineable': True,
        },
        Coin.XLM: {
            'display_name': 'Stellar',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.BCH: {
            'display_name': 'Bitcoin Cash',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.EOS: {
            'display_name': 'EOS',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.LTC: {
            'display_name': 'Litecoin',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.BSV: {
            'display_name': 'Bitcoin SV',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.ADA: {
            'display_name': 'Cardano',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.XMR: {
            'display_name': 'Monero',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.TRX: {
            'display_name': 'Tron',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.MIOTA: {
            'display_name': 'IOTA',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.DASH: {
            'display_name': 'DASH',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.XEM: {
            'display_name': 'NEM',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.BNB: {
            'display_name': 'Binance Coin',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.NEO: {
            'display_name': 'NEO',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.ETC: {
            'display_name': 'Ethereum Classic',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.ZEC: {
            'display_name': 'Zcash',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.BTG: {
            'display_name': 'Bitcoin Gold',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.XTZ: {
            'display_name': 'Tezos',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.VET: {
            'display_name': 'VeChain',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
        Coin.DOGE: {
            'display_name': 'Dogecoin',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': True,
        },
        Coin.MKR: {
            'display_name': 'Maker',
            'default_fraction_digits': 6,
            'sub_unit': 1e6,
            'mineable': False,
        },
    }

    @classmethod
    def decimal_precision_for_currency(cls, currency: Currency) -> int:
        """Returns the decimal precision for a currency (number of digits after the decimal)"""
        return cls._CURRENCY_DATA[currency]['default_fraction_digits']

    @classmethod
    def sub_unit_for_currency(cls, currency: Currency) -> int:
        """Returns the sub unit for a currency.
        (eg, the subunit for USD is 100 because there are 100 cents in a dollar)

        """
        return cls._CURRENCY_DATA[currency]['sub_unit']



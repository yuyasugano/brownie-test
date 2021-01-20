import pytest
import click

configurations = {
    'dai': {'token': '0x6b175474e89094c44da98b954eedeac495271d0f', 'whale': '0x70178102AA04C5f0E54315aA958601eC9B7a4E08'},
    'usdt': {'token': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'whale': '0x1062a747393198f70f71ec65a582423dba7e5ab3'},
    'usdc': {'token': '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', 'whale': '0xa191e578a6736167326d05c119ce0c90849e84b7'},
    'eth': {'token': '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2', 'whale': '0x2f0b23f53734252bda2277357e97e1517d6b042a'},
    'yfi': {'token': '0x0bc529c00C6401aEF6D220BE8C6Ea1667F6Ad93e', 'whale': '0xba37b002abafdd8e89a1995da52740bbc013d992'},
    'link': {'token': '0x514910771AF9Ca656af840dff83E8264EcF986CA', 'whale': '0x98c63b7b319dfbdf3d811530f2ab9dfe4983af9d'},
    'snx': {'token': '0xC011a73ee8576Fb46F5E1c5751cA3B9Fe0af2a6F', 'whale': '0xb671f2210b1f6621a2607ea63e6b2dc3e2464d1f'},
    'aave': {'token': '0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9', 'whale': '0x25f2226b597e8f9514b3f68f00f494cf4f286491'},
}

@pytest.fixture(scope='function', autouse=True)
def isolation(fn_isolation):
    pass

@pytest.mark.parametrize('config', configurations)
def test_defi(chain, accounts, interface, config):
    whales = accounts.at(configurations[config]['whale'], force=True)
    tokens = interface.ERC20(configurations[config]['token'], owner=whales)
    uniswap = interface.UniswapRouter('0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D', owner=whales)
    factory = interface.UniswapFactory('0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f', owner=whales)
    uni = interface.ERC20('0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984', owner=whales)
    scale = 10 ** tokens.decimals()
    def print_price():
        print(
            'price', uniswap.getAmountsOut(scale, [tokens, uni])[-1] / 1e8,
            'liquidity', tokens.balanceOf(factory.getPair(uni, tokens)) / scale,
        )
    print_price()


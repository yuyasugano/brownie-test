import pytest
import click

@pytest.fixture(scope='function', autouse=True)
def isolation(fn_isolation):
    pass

def test_flashloan(accounts, interface, chain, Flashloan):
    # prepare contracts
    user = accounts[0]
    flashloan = Flashloan.deploy({'from': user})
    wethAddress = '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
    weth = interface.WETH(wethAddress)

    # execute a flashloan for 100 WETH
    tx = flashloan.initiateFlashLoan('0x1E0447b19BB6EcFdAe1e4AE1694b0C3659614e4e', wethAddress, 100 * 10 ** weth.decimals())
    tx.info()
    contractBalance = weth.balanceOf(flashloan.address)
    print(click.style(f'remained weth wei: {contractBalance} {weth.symbol()}', fg='green', bold=True))
    assert contractBalance == wethBalance - 2, 'something went wrong'

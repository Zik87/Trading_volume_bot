# Игнорирует предупреждение об устаревшем пакете ,который скоро перестанет поддерживаться
import warnings
warnings.filterwarnings("ignore")


from x10.perpetual.accounts import StarkPerpetualAccount
import datetime
import requests
from web3 import Web3
from eth_account import Account


RPC = 'https://arbitrum.therpc.io'






def main():
    acc = Account.from_key(pr_key)
    checksum_address = Web3.to_checksum_address(acc.address)


if __name__ == "__main__":

    with open('test_wallet.txt') as file:
        pr_key = file.readline()

    main()
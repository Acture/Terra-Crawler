from terra_sdk.client.lcd import LCDClient
import requests
import sys
import time
import pandas as pd





terra = LCDClient(chain_id="columbus-5", url="https://lcd.terra.dev")
address = 'terra18728g9afafn3z4xz8nkdfecpr7xuqhyh7mlg6d'
hash1 = '2C9754CAB80E05CF1A5DE457AC9656E16BF09A096A722F6A8E4DA1582932ABF8'

def balance(wallet_address:str):
	b = list(terra.bank.balance(wallet_address))[0]
	print (b)

def get_balance(wallet_address:str):
	b = list(terra.bank.balance(wallet_address))[0]
	return b

def address_transactions(wallet_address:str):
	num = '10'
	with requests.get('https://fcd.terra.dev/v1/txs?account='+wallet_address+'&limit='+num,timeout = 2) as r:
		j = r.json()
		temp = []
		for i in range(len(j.get('txs'))-1):
			temp.append([j.get('txs')[i].get('timestamp'),j.get('txs')[i].get('id'),j.get('txs')[i].get('chainId'),j.get('txs')[i].get('txhash'),j.get('txs')[i].get('gas_used'),j.get('txs')[i].get('gas_wanted')])
		df = pd.DataFrame(temp)
		df.columns = ['timestamp','id', 'chainId', 'txhash', 'gas_used', 'gas_wanted']
	print(df)

def get_address_transactions(wallet_address:str, num: str):
	with requests.get('https://fcd.terra.dev/v1/txs?account='+wallet_address+'&limit='+num,timeout = 2) as r:
		j = r.json()
		temp = []
		for i in range(5):
			temp.append([j.get('txs')[i].get('timestamp'),j.get('txs')[i].get('id'),j.get('txs')[i].get('chainId'),j.get('txs')[i].get('txhash'),j.get('txs')[i].get('gas_used'),j.get('txs')[i].get('gas_wanted')])
		df = pd.DataFrame(temp)
		df.columns = ['timestamp','id', 'chainId', 'txhash', 'gas_used', 'gas_wanted']
	return df

def latest_transaction(wallet_address:str, num: str):
	with requests.get('https://fcd.terra.dev/v1/txs?account='+wallet_address+'&limit='+num,timeout = 2) as r:
		result = r.json().get('txs')[0].get('id')
	print(result)

def get_latest_transaction(wallet_address:str, num: str):
	with requests.get('https://fcd.terra.dev/v1/txs?account='+wallet_address+'&limit='+num,timeout = 2) as r:
		result = r.json().get('txs')[0].get('id')
	return result

def transaction(txhash:str):
	result = terra.tx.tx_info(txhash).tx
	print (result)

def get_transaction(txhash:str):
	return terra.tx.tx_info(txhash)


def monitor(address:str,sleeptime:str):
	sleeptime = int(sleeptime)
	try:
		while True:
			print('钱包余额：{a},最近交易ID：{b}'.format(a = get_balance(address), b = get_latest_transaction(address,'10')))
			time.sleep(sleeptime)
	except KeyboardInterrupt:
		print('Interrupted')


def main():
	if sys.argv[1] == '-?':
		print('Package Needed:terra_sdk.client.lcd, requests, sys, time, pandas')
		print('Monitor: -m address sleeptime')
		print('Balance: -b wallet_address')
		print('Transactions: -ta wallet_address')
		print('Hash: -th hash')
	if sys.argv[1] == '-m':
		monitor(sys.argv[2],sys.argv[3])
	if sys.argv[1] == '-b':
		balance(sys.argv[2])
	if sys.argv[1] == '-ta':
		address_transactions(sys.argv[2])
	if sys.argv[1] == '-th':
		transaction(sys.argv[2])


if __name__ == '__main__':
	main()
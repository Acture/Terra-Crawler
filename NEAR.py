import requests
import json

url = "https://rpc.mainnet.near.org"

payload = json.dumps({
    "jsonrpc": "2.0",
    "id": "dontcare",
    "method": "query",
    "params": {
        "request_type": "view_account",
        "finality": "final",
        "account_id": "761423a47dd1fb20e400ee517f2c675d2797030cd342a43712b3087d1c447851"
    }
})
headers = {
	'Content-Type': 'application/json',
	'User-Agent':'PostmanRuntime/7.29.0',
	'Accept':'*/*',
	'Accept-Encoding':'gzip, deflate, br',
	'Connection':"keep-alive"
}
proxies = {"http":'127.0.0.1:1080',"SOCKS5":'127.0.0.1:1080'}

response = requests.post(url, headers=headers, data=payload, timeout=2, proxies=proxies)

print(response.text)

http post https://rpc.testnet.near.org jsonrpc=2.0 id=dontcare method=query \
  params:='{
    "request_type": "view_account",
    "finality": "final",
    "account_id": "nearkat.testnet"
  }'

http post https://rpc.testnet.near.org jsonrpc=2.0 id=dontcare method=query params:='{"request_type": "view_account","finality": "final","account_id": "761423a47dd1fb20e400ee517f2c675d2797030cd342a43712b3087d1c447851"}'
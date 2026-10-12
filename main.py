import requests

url = "https://api.dexscreener.com/latest/dex/search"

params = {
    "q":"SOL/USDC"
}

response = requests.get(url, params=params,timeout=10)

print(response.status_code)

data = response.json()
tokens = []
print(f"{'NAME':<20}{'SYMBOL':<15}{'PRICE':>15}{'VOLUME 24H':>20}")
print("-" * 70)

for pair in data["pairs"]:
    if pair["chainId"] == "solana":
        name = pair["baseToken"]["name"]
        symbol = pair["baseToken"]["symbol"]
        price = pair["priceUsd"]
        volume = pair["volume"]["h24"]

        tokens.append({"name":name,"symbol":symbol,"price":price,"volume":volume})
tokens = sorted(tokens,key = lambda token:token["volume"],reverse = True)
for token in tokens:
    if token["volume"] > 10000:
        print(f'{token["name"][:20]:<22}{token["symbol"][:12]:<15}{token["price"]:>15}{token["volume"]:>20,.2f}')

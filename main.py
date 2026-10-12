import time
import requests

url = "https://api.dexscreener.com/latest/dex/search"
now = time.time()
params = {
    "q":"SOL/USDC"
}

response = requests.get(url, params=params,timeout=10)

print(response.status_code)

data = response.json()
tokens = []
print(f"{'NAME':<20}{'SYMBOL':<15}{'PRICE':>15}{'VOLUME 24H':>20}{'CREATED':>20}")
print("-" * 90)

for pair in data["pairs"]:
    if pair["chainId"] == "solana":
        name = pair["baseToken"]["name"]
        symbol = pair["baseToken"]["symbol"]
        price = pair["priceUsd"]
        volume = pair["volume"]["h24"]

        created = pair.get("pairCreatedAt")

        if created is not None:
            age_hours = (now-created/1000)/3600
            if 0 <= age_hours < 24:
                tokens.append({"name":name,"symbol":symbol,"price":price,"volume":volume,"created":age_hours})
tokens = sorted(tokens,key = lambda token:(token["created"],token["volume"]),reverse = True)
for token in tokens:
    if token["volume"] > 10000:
        print(f'{token["name"][:20]:<22}{token["symbol"][:12]:<15}{token["price"]:>15}{token["volume"]:>20,.2f}{token["created"]:>20,.2f}')

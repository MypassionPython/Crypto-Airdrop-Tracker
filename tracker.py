import json

def load_airdrops(file="airdrops.json"):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)

def display_airdrops(airdrops):
    print("🚀 Crypto Airdrop Tracker\n")
    for a in airdrops:
        print(f"🔹 {a['name']} ({a['token']})")
        print(f"   Status: {a['status']}")
        print(f"   Link: {a['link']}\n")

if __name__ == "__main__":
    airdrops = load_airdrops()
    display_airdrops(airdrops)



import requests
import sys

URL = "https://positive-rodent-113635.upstash.io"
TOKEN = "gQAAAAAAAbvjAAIgcDEwZjYwYzdkOWM3ZDg0MWZlOTNlMzBjNjE2YWNiOWQ0Mg"

emotion = sys.argv[1]

requests.get(
    f"{URL}/set/emotion/{emotion}",
    headers={"Authorization": f"Bearer {TOKEN}"}
)

print("Emotion set to:", emotion)
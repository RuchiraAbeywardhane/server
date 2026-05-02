import requests
import runpod

URL = "https://positive-rodent-113635.upstash.io/get/emotion"
TOKEN = "gQAAAAAAAbvjAAIgcDEwZjYwYzdkOWM3ZDg0MWZlOTNlMzBjNjE2YWNiOWQ0Mg"

def handler(event):
    res = requests.get(
        URL,
        headers={"Authorization": f"Bearer {TOKEN}"}
    )
    emotion = res.json().get("result") or "neutral"
    return {
        "emotion": emotion
    }

runpod.serverless.start({"handler": handler})

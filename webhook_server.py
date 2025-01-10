from flask import Flask, request, jsonify
import hmac
import hashlib

from decouple import config

DISCORD_CHANNEL_ID = "957671450955894864"  # Replace with your Discord channel ID
BOT_KEY = config('BOT_KEY')
GITHUB_SECRET = config('DISCORD_WEBHOOK')

app = Flask(__name__)

# Verify GitHub payloads
def verify_signature(payload, signature):
  mac = hmac.new(GITHUB_SECRET.encode(), payload, hashlib.sha256).hexdigest()
  return hmac.compare_digest(f"sha256={mac}", signature)

@app.route("/webhook", methods=["POST"])
def github_webhook():
  # Verify request
  payload = request.data
  signature = request.headers.get("X-Hub-Signature-256", "")
  if not verify_signature(payload, signature):
    return "Invalid signature", 401

  event = request.headers.get("X-GitHub-Event", "")
  data = request.json

  if event == "issues":
    action = data.get("action")
    issue = data.get("issue", {})
    title = issue.get("title")
    url = issue.get("html_url")

    if action == "opened":
      notify_discord(f":hourglass: New issue created: {title} - {url}")
    elif action == "closed":
      notify_discord(f":white_check_mark: Issue closed: {title} - {url}")

  return jsonify({"status": "ok"})

# Notify Discord channel
def notify_discord(message):
  import requests
  url = f"https://discord.com/api/v10/channels/{DISCORD_CHANNEL_ID}/messages"
  headers = {"Authorization": f"Bot {BOT_KEY}"}
  payload = {"content": message}
  requests.post(url, json=payload, headers=headers)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

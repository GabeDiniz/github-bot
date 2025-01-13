from flask import Flask, request, jsonify
import hmac
import hashlib
import requests
from decouple import config

# Fetch secrets from .env
BOT_KEY = config('BOT_KEY')
GITHUB_SECRET = config('DISCORD_WEBHOOK')

# Repository-to-Discord Channel Mapping
REPO_TO_CHANNEL = {
  "GabeDiniz/discord-bot-v2": "957671450955894864",  
}

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
  data = request.json   # json payload received from GitHub Webhook

  # Identify repository
  repo_full_name = data.get("repository", {}).get("full_name")  # Example: "owner/repo"
  if not repo_full_name or repo_full_name not in REPO_TO_CHANNEL:
    # Catch error: return ignored if repo is not setup to be notified (check REPO_TO_CHANNEL)
    return jsonify({"status": "ignored", "reason": "Repository not mapped"}), 200

  discord_channel_id = REPO_TO_CHANNEL[repo_full_name]

  # Handle events
  if event == "issues":
    action = data.get("action")
    issue = data.get("issue", {})
    title = issue.get("title")
    url = issue.get("html_url")

    if action == "opened":
      notify_discord(discord_channel_id, f":hourglass: New issue created: {title} - {url}")
    elif action == "closed":
      notify_discord(discord_channel_id, f":white_check_mark: Issue closed: {title} - {url}")

  return jsonify({"status": "ok"})

# Notify Discord channel
def notify_discord(channel_id, message):
  url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
  headers = {"Authorization": f"Bot {BOT_KEY}"}
  payload = {"content": message}
  requests.post(url, json=payload, headers=headers)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)

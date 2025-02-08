# 🐙 GitHub Discord Bot

This project is a Discord bot integrated with GitHub webhooks to provide real-time notifications about issue events (created/closed) and merge request events in specific repositories. The bot listens to webhook events via a Flask server and sends notifications to a designated Discord channel.

# 📁 File Structure and Explanation

`main.py`
Purpose: The main bot file that connects to Discord and handles basic setup.

`webhook_server.py`
Purpose: Flask-based webhook server that listens to GitHub events.

- verify_signature(payload, signature): Validates incoming webhook payloads for security.
- github_webhook(): Handles incoming webhook requests and sends appropriate notifications to Discord.
- notify_discord(message): Sends a message to the specified Discord channel.

# 👨‍💻 For Developer

## Steps to Run (local)

#### Step 1: Start the Webhook Server

Run the Flask server locally:
`python webhook_server.py`

#### Step 2: Expose the Server with ngrok

Start ngrok to expose the local server to the internet:
`ngrok http 5000`

Copy the https:// forwarding URL (e.g., https://<ngrok-subdomain>.ngrok-free.app).

#### Step 3: Update GitHub Webhook

1. Go to your GitHub repository > Settings > Webhooks > Add webhook.
2. Set the Payload URL to the ngrok forwarding URL with /webhook appended (e.g., https://<your-ngrok-subdomain>.ngrok-free.app/webhook).
3. Set the Content type to application/json.
4. Enter the Secret that was set in the repos webhook in the .env file.
5. Select the Issues events and save.

#### Step 4: Run the Discord Bot

Start the bot:
`py main.py`

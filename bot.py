import os

from dotenv import load_dotenv

load_dotenv()

from chatto import YouTubeBot
from chatto.events import MessageCreatedEvent

scam_links = ["dank3", "dank4", "dank5"]

bot = YouTubeBot(
    # Your project's API key.
    os.environ.get("API_KEY"),
    # The ID of the channel whose stream you want to connect to.
    os.environ.get("CHANNEL_ID"),
    # Your OAuth client ID secrets file.
    secrets_file="secrets.json",
)


# Listen for MessageCreatedEvents, and run this awaitable whenever a
# new message is received.
@bot.listen(MessageCreatedEvent)
async def on_message_created(event):
    # Ignore messages sent by the broadcaster.
    # if event.message.channel.is_owner:
    #     return

    # Respond to messages starting with "!hello".
    if event.message.content.startswith("!hello"):
        await bot.send_message(f"Hi {event.message.channel.name}!")

    if event.message.content in scam_links:
        await bot.send_message("sheesh")


if __name__ == "__main__":
    # This is blocking, so should be the last thing you call.
    bot.run(with_stream_id=os.environ.get("STREAM_ID"))

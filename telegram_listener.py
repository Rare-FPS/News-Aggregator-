from telethon import TelegramClient, events
from rich import print
from rich.panel import Panel
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_CHANNELS

async def start_telegram_listener():
    client = TelegramClient('news_session', TELEGRAM_API_ID, TELEGRAM_API_HASH)
    
    @client.on(events.NewMessage(chats=TELEGRAM_CHANNELS))
    async def handler(event):
        chat = await event.get_chat()
        text = event.raw_text
        link = f"https://t.me/{chat.username}/{event.id}" if chat.username else "Private Channel"
        
        content = f"{text[:300]}...\n\n[bold green]Link:[/bold green] [link={link}]{link}[/link]"
        print(Panel(content, title=f"[bold cyan]Telegram: @{chat.username}[/bold cyan]", expand=False))
        
    await client.start()
    print("[bold green]✔ Telegram real-time listener active and waiting for news...[/bold green]\n")
    await client.run_until_disconnected()
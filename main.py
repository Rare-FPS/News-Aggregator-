import asyncio
from rich import print
from rss_fetcher import fetch_rss_news
from telegram_listener import start_telegram_listener

async def periodic_rss_fetcher():
    """Fetches RSS feeds initially, then every 10 minutes."""
    while True:
        print("\n[bold magenta]=== Fetching Latest RSS News Outlets ===[/bold magenta]")
        
        # Print RSS updates
        for panel in fetch_rss_news():
            print(panel)
            
        print("\n[italic green]Next RSS refresh in 10 minutes... (Telegram is listening live)[/italic green]\n")
        await asyncio.sleep(600)  # 600 seconds = 10 minutes

async def main():
    print("[bold yellow]Starting Terminal News & Telegram Aggregator...[/bold yellow]")
    
    # Run the periodic RSS fetcher and the real-time Telegram stream concurrently
    await asyncio.gather(
        periodic_rss_fetcher(),
        start_telegram_listener()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[bold red]Aggregator shut down safely. Goodbye![/bold red]")
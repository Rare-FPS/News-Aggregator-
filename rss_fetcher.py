import feedparser
from rich.panel import Panel
from config import RSS_FEEDS

def fetch_rss_news():
    panels = []
    
    for url in RSS_FEEDS:
        try:
            feed = feedparser.parse(url)
            
            # Check if feed empty or bozo flag set (parsing error)
            if not feed.entries:
                print(f"[bold yellow]⚠ Warning: No entries found for {url}[/bold yellow]")
                continue
                
            source_title = feed.feed.get('title', 'News Source')
            
            # Grab top 2 articles from this feed
            for entry in feed.entries[:2]:
                title = entry.get('title', 'No Title')
                link = entry.get('link', '')
                published = entry.get('published', 'Recently')
                
                content = (
                    f"[bold white]{title}[/bold white]\n\n"
                    f"[cyan]Link:[/cyan] [link={link}]{link}[/link]\n"
                    f"[dim]Published: {published}[/dim]"
                )
                
                panels.append(
                    Panel(
                        content, 
                        title=f"[bold yellow]RSS: {source_title}[/bold yellow]", 
                        expand=False
                    )
                )
        except Exception as e:
            print(f"[bold red]❌ Failed to fetch feed {url}: {e}[/bold red]")
            
    return panels
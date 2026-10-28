import os
from dotenv import load_dotenv

load_dotenv()

# Telegram Configuration
TELEGRAM_API_ID = int(os.getenv("TELEGRAM_API_ID", 0))
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH", "")
TELEGRAM_CHANNELS = [
    #Global News Channels
    "bbcnews", "reuters","nytimes", "TheGuardian", "trtworld", "aljazeeraenglish", "disclosetv", 
    #Local News Channels
    "bdnews24", "prothomalo", "jamunatvbd", "somoynews", "bdtech"]

# RSS Feed URLs
RSS_FEEDS = [
    # Global News Sources
    "http://feeds.bbci.co.uk/news/world/rss.xml",
    "https://openrss.org/feed/www.allsides.com/unbiased-balanced-news",
    "https://globalnews.ca/feed/",

    #Bd News Sources
    "https://www.prothomalo.com/feed",
    "https://www.banglatribune.com/feed/",
    "https://globalvoices.org/-/world/south-asia/bangladesh/feed/",

]
import json
import pandas as pd
from twitter_scraper_selenium import scrape_profile
from twitter_scraper_selenium import get_profile_details


def scrape_twt_posts_json(username):
    user = scrape_profile(twitter_username='microsoft', output_format="json", browser="firefox", tweets_count=10, headless=False)
    # profile = json.loads(s=user)
    # df = pd.json_normalize(profile['user']['result'])
    return user


def scrape_twt_profile_details(username):
    profile = get_profile_details(twitter_username=username)
    profile = json.loads(s=profile)
    df = pd.json_normalize(profile['user']['result'])
    return df








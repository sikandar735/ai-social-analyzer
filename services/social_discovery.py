# backend/services/discovery.py
import requests

# Directly define your SerpAPI Key here
SERPAPI_KEY = "9fa823d557c9566f3e0541cf2337bb5128cf6ed0bc981638a6b58c3462e165a2"  # <-- Replace with your actual key

def search_social_links(company_name):
    """
    Uses SerpAPI to search for company social media profiles.
    """
    platforms = ["facebook", "instagram", "linkedin"]
    found_links = {}

    for platform in platforms:
        params = {
            "engine": "google",
            "q": f"site:{platform}.com {company_name}",
            "api_key": SERPAPI_KEY,
            "num": 1  # Only get top result
        }

        response = requests.get("https://serpapi.com/search", params=params)
        data = response.json()

        if "organic_results" in data and data["organic_results"]:
            top_result = data["organic_results"][0]
            found_links[platform] = top_result.get("link", "")

    return found_links

def detect_accounts(domain):
    """
    Uses SerpAPI to detect social media accounts linked to a domain.
    """
    params = {
        "engine": "google",
        "q": f"site:{domain} facebook OR instagram OR linkedin",
        "api_key": SERPAPI_KEY,
        "num": 5
    }

    response = requests.get("https://serpapi.com/search", params=params)
    data = response.json()

    platforms_found = []
    if "organic_results" in data:
        for result in data["organic_results"]:
            url = result.get("link", "")
            if "facebook.com" in url:
                platforms_found.append("facebook")
            if "instagram.com" in url:
                platforms_found.append("instagram")
            if "linkedin.com" in url:
                platforms_found.append("linkedin")

    return list(set(platforms_found))
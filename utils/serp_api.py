import os
import requests

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")

def search_social_links(domain: str):
    if not SERP_API_KEY:
        raise ValueError("SerpAPI key is missing. Please set SERPAPI_API_KEY in your environment.")

    query = f"site:{domain}"
    platforms = ["facebook.com", "linkedin.com", "instagram.com", "twitter.com", "tiktok.com", "youtube.com"]
    results = {}

    for platform in platforms:
        url = "https://serpapi.com/search"
        params = {
            "q": f"{query} site:{platform}",
            "api_key": SERP_API_KEY,
            "engine": "google"
        }

        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            link = data['organic_results'][0]['link']
            results[platform.split('.')[0]] = link
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] SerpAPI request failed for {platform}: {e}")
        except (KeyError, IndexError):
            print(f"[INFO] No result found for {platform}")
        except Exception as e:
            print(f"[ERROR] Unexpected error for {platform}: {e}")

    return results

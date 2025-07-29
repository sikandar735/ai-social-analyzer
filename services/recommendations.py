# backend/services/recommendations.py

RECOMMENDED_PLATFORMS = {
    "fashion": ["facebook", "instagram", "pinterest", "tiktok"],
    "tech": ["linkedin", "twitter", "youtube"],
    "food": ["facebook", "instagram", "youtube"],
    "education": ["linkedin", "youtube", "twitter"],
    "health": ["facebook", "linkedin", "instagram"],
    "default": ["facebook", "linkedin"]
}

def recommend_missing_platforms(category, found_platforms_dict):
    """
    Recommends missing platforms based on category.
    Args:
        category (str): Company category (e.g., fashion, tech)
        found_platforms_dict (dict): Dictionary of found social media links {platform: url}
    Returns:
        list: Platforms that are missing
    """
    found_platforms = found_platforms_dict.keys()

    recommended = RECOMMENDED_PLATFORMS.get(category.lower(), RECOMMENDED_PLATFORMS["default"])

    missing = []
    for platform in recommended:
        if platform not in found_platforms:
            missing.append(platform)

    return missing

def suggest_platforms(scope, category):
    """
    Suggest platforms based on business scope and category.
    Args:
        scope (str): Local / National / Global
        category (str): Business category
    Returns:
        list: Suggested platforms for strategy
    """
    scope = scope.lower()
    category = category.lower()

    suggestions = set()

    # Scope Influence
    if scope == "global":
        suggestions.update(["linkedin", "youtube"])
    elif scope == "national":
        suggestions.update(["facebook", "instagram"])
    elif scope == "local":
        suggestions.update(["facebook", "whatsapp"])

    # Category-based platforms
    category_platforms = RECOMMENDED_PLATFORMS.get(category, RECOMMENDED_PLATFORMS["default"])
    suggestions.update(category_platforms)

    return list(suggestions)
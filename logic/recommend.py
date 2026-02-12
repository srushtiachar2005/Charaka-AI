import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERB_PATH = os.path.join(BASE_DIR, "data", "herb.json")

with open(HERB_PATH, "r", encoding="utf-8") as f:
    herbs = json.load(f)

def recommend_herbs(prakriti: str, limit: int = 5):
    """
    Recommend herbs that pacify the given prakriti (dosha).
    
    Args:
        prakriti: The dominant dosha (e.g., "Vata", "Pitta", "Kapha")
        limit: Maximum number of herbs to return
        
    Returns:
        List of herb dictionaries containing name, benefits, and link
    """
    recommended = []
    
    for herb in herbs:
        # Check if this herb pacifies the given prakriti
        if prakriti in herb["pacify"] or "tridosha" in herb["pacify"]:
            recommended.append({
                "name": herb["name"],
                "benefits": herb["preview"],
                "link": herb["link"]
            })
    
    return recommended[:limit]

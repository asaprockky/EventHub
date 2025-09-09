import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyBxINPZM50gQvUPL4GeKD6jaKGKDNG9eT0"


# Configure Gemini with API key (store API key in Django settings for safety!)
genai.configure(api_key=GEMINI_API_KEY)

# Choose the model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_bio(interests: str, name: str = "", age: int = None, location: str = "") -> str:
    """
    Generate a professional/interesting user bio based on their interests and profile info.
    """
    prompt = f"""
    Create a friendly and engaging bio for a user.
    Name: {name if name else "User"}
    Age: {age if age else "Unknown"}
    Location: {location if location else "Not specified"}
    Interests: {interests if interests else "Not shared"}

    The bio should sound natural, warm, and personal, in 2–3 sentences.
    """
    response = model.generate_content(prompt)
    print("Generated bio:", response.text.strip())
    return response.text.strip()



def generate_short_description(profile) -> str:
    """
    Generate a very short one-line description of a user (for event pages).
    Example: "Tech enthusiast from Tashkent who loves football."
    """
    prompt = f"""
    Write a short, single-sentence description about this user:

    Name: {profile.name or "User"}
    Age: {profile.age or "Unknown"}
    Location: {profile.location or "Not specified"}
    Interests: {profile.interests or "Not shared"}
    """

    response = model.generate_content(prompt)
    return response.text.strip()

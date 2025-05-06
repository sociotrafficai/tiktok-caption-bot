import random

# Static data source
captions = {
    "funny": [
        "POV: I'm still figuring out life 🤡",
        "If overthinking burned calories, I'd be ripped 😂",
        "This video was sponsored by zero plans and vibes only.",
        "Why be moody when you can shake that booty? 🍑",
        "Current mood: buffering..."
    ],
    "motivational": [
        "Chase dreams, not people 💯",
        "You didn't come this far to stop now 🚀",
        "From 0 to 100 – watch me go 📈",
        "Small wins > No wins 🔥",
        "Manifest it, grind it, repeat."
    ],
    "trendy": [
        "This sound is about to blow up 🔥",
        "Don't blink or you'll miss it 👀",
        "Using this trend before it’s mainstream 😎",
        "Caught the trend train just in time 🚂",
        "Trend + me = viral combo"
    ]
}

def generate_caption(category="funny"):
    if category not in captions:
        print("Category not found. Choose from: funny, motivational, trendy.")
        return
    caption = random.choice(captions[category])
    print(f"📝 Your TikTok caption ({category}):\n{caption}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python caption_bot.py <category>")
        print("Example: python caption_bot.py funny")
    else:
        generate_caption(sys.argv[1])

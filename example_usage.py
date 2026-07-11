"""
example_usage.py -- Demonstrates CompetitorAdCreativeParserClient
"""
from client import CompetitorAdCreativeParserClient

def main():
    client = CompetitorAdCreativeParserClient()
    result = client.parse_ad(
        ad_copy_sample="Get the cheapest moisturizers on the market right now!",
        ad_platform="Meta"
    )
    print("[Competitor Ad Parser Result]")
    print(f"Hook: {result['pitch_hook']}")
    print(f"Counter Suggestion: {result['counter_copy']}")

if __name__ == "__main__":
    main()

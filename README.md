# genpark-competitor-ad-creative-parser-skill

> **GenPark AI Agent Skill** -- Rival ad analyzer and counter-copy compiler.

## Quick Start

```python
from client import CompetitorAdCreativeParserClient
client = CompetitorAdCreativeParserClient()
res = client.parse_ad("Free delivery this week", "Google")
print(res["pitch_hook"])
```

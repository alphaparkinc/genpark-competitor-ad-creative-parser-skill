"""
genpark-competitor-ad-creative-parser-skill: Client SDK
Parses competitor ad messaging to suggest counter-objections and marketing copy.
"""
from __future__ import annotations
from typing import Optional


class CompetitorAdCreativeParserClient:
    """
    SDK for ad positioning audit.
    """

    def parse_ad(
        self,
        ad_copy_sample: str,
        ad_platform: str,
    ) -> dict:
        copy = ad_copy_sample.lower()
        platform = ad_platform.lower()

        if "cheap" in copy or "price" in copy or "sale" in copy:
            hook = "Discount & Pricing Focus"
            counter = "Stand out by emphasizing premium ingredients, verified reviews, and lifetime value over short-term discounts."
        elif "fast" in copy or "delivery" in copy:
            hook = "Logistics/Speed Focus"
            counter = "Counter with our careful craftsmanship, quality assurance guarantees, and eco-friendly packing."
        else:
            hook = "Generic Brand Awareness"
            counter = "Introduce direct-response copy that addresses specific user pain points."

        return {
            "pitch_hook": hook,
            "counter_copy": counter
        }

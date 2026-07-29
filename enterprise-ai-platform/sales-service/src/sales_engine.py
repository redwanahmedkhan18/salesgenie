"""
AI Sales Engine & Decision Nodes
Lead qualification scoring (BANT framework), product recommendation algorithms, and coupon distribution rules.
"""

from typing import List, Dict, Any
from .models import Lead, ProductCatalog, ProductRecommendationDTO, Coupon


def calculate_lead_qualification_score(
    budget_usd: float | None,
    has_authority: bool,
    need_urgency: str,  # 'immediate', 'this_quarter', 'exploring'
    timeline_months: int | None,
) -> int:
    """
    Computes BANT (Budget, Authority, Need, Timeline) lead score from 0 to 100.
    Scores >= 70 qualify as High Intent Leads.
    """
    score = 0
    
    # Budget Scoring (Max 35 pts)
    if budget_usd:
        if budget_usd >= 50000:
            score += 35
        elif budget_usd >= 10000:
            score += 25
        elif budget_usd >= 2500:
            score += 15

    # Authority Scoring (Max 25 pts)
    if has_authority:
        score += 25

    # Need Urgency Scoring (Max 25 pts)
    if need_urgency == "immediate":
        score += 25
    elif need_urgency == "this_quarter":
        score += 18
    elif need_urgency == "exploring":
        score += 10

    # Timeline Scoring (Max 15 pts)
    if timeline_months is not None:
        if timeline_months <= 1:
            score += 15
        elif timeline_months <= 3:
            score += 10
        elif timeline_months <= 6:
            score += 5

    return min(score, 100)


def generate_product_recommendations(
    user_interest_category: str,
    products: List[ProductCatalog],
) -> List[ProductRecommendationDTO]:
    """Generates personalized product recommendations and cross-sell/upsell suggestions."""
    recommendations = []
    for prod in products:
        if prod.category.lower() == user_interest_category.lower():
            reason = f"Top-rated match in {prod.category} category based on user inquiry preferences."
            discount_offer = "Use coupon 'SAVE15' for 15% discount today!"
            recommendations.append(
                ProductRecommendationDTO(
                    product_id=prod.id,
                    sku=prod.sku,
                    name=prod.name,
                    category=prod.category,
                    price_usd=prod.price_usd,
                    recommendation_reason=reason,
                    upsell_discount_offer=discount_offer,
                )
            )
    return recommendations

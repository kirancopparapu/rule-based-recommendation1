import streamlit as st

# Hardcoded business rule
RULES = {
    "Jeans": ["Shoes"]
}

# Recommender logic
def recommend_products(purchased_items):
    recommendations = []
    for item in purchased_items:
        if item in RULES:
            recommendations.extend(RULES[item])
    return list(set(recommendations))

# UI
st.title("Rule-Based Recommender")

st.write("If a user purchases **Jeans**, we recommend **Shoes**.")

products = ["Jeans", "Shoes", "Shirt", "T-shirt"]
purchased = st.multiselect("Select items the user purchased:", products)

if st.button("Get Recommendations"):
    recs = recommend_products(purchased)
    if recs:
        st.success(f"Recommended Products: {', '.join(recs)}")
    else:
        st.info("No recommendations for the selected items.")

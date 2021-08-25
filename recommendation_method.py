def get_recommendation_based_purchase_history(customer_id):
    purchase_history = get_customer_purchase_history(customer_id)
    categories_percentages = calc_categories_percentages(purchase_history)
    recommended_products = get_top_selling_products(categories_percentages)
    return recommended_products

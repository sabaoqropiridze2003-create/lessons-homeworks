import requests
import streamlit as st

st.title("Fake Store")

with st.spinner("Loading products..."):
    try:
        response = requests.get("https://fakestoreapi.com/products")
        if response.status_code == 200:
            products = response.json()
        else:
            products = None
    except:
        products = None

if products is None:
    st.error("Failed to load products")
else:
    st.sidebar.title("filters")

    categories = ["All"] + \
        sorted(list(set(item["category"] for item in products)))
    selected_category = st.sidebar.selectbox("Category", categories)

    max_price_in_data = float(max(item["price"] for item in products))
    max_price = st.sidebar.slider(
        "Maximum Price", 0.0, max_price_in_data, max_price_in_data
    )

    search_query = st.sidebar.text_input("Search", "").lower()

    filtered_products = []
    for product in products:
        if (
            selected_category != "All"
            and product["category"] != selected_category
        ):
            continue

        if product["price"] > max_price:
            continue

        if search_query and (
            search_query not in product["title"].lower()
            and search_query not in product["description"].lower()
        ):
            continue

        filtered_products.append(product)

    st.write(f"**products found:** {len(filtered_products)}")
    st.divider()

    for product in filtered_products:
        col1, col2 = st.columns([1, 3])

        with col1:
            st.image(product["image"], width=150)

        with col2:
            st.subheader(product["title"])
            st.write(f"**ID:** {product['id']}")
            st.write(f"**Price:** ${product['price']}")
            st.write(f"**Category:** {product['category']}")
            st.write(
                f"**Rating:**  {product['rating']['rate']} ({product['rating']['count']} reviews)"
            )

            with st.expander("View details"):
                st.write(product["description"])

        st.divider()

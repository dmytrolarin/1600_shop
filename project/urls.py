import shop

shop.shop.add_url_rule(
    rule="/",
    view_func=shop.render_catalog
)
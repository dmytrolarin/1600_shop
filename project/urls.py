import shop


shop.shop.add_url_rule(
    rule="/",
    view_func=shop.render_catalog,
    methods= ['GET', 'POST']
)

shop.shop.add_url_rule(
   rule='/create-payment/',
   view_func=shop.create_payment,
)
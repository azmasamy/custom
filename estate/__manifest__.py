{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "Hamza Taher",
    'category': 'Sales',
    'description': """
    A realestate advertisement application
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/inherited_res_users.xml',
        'views/estate_property_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
}

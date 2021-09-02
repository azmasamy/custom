{
    'name': "Recpmmendation System",
    'version': '1.0',
    'depends': ['base',
                'sale',
                ],
    'author': "Hamza Taher",
    'category': 'Sales',
    'description': """
    A realestate advertisement application
    """,
    ''
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/inherited_product_template.xml',
        'views/inherited_res_partner.xml',
        'views/customer_categories_views.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
    'application': False,
}

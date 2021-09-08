{
    'name': "Estate Account",
    'version': '1.0',
    'depends': ['base',
                'estate',
                'account'],
    'author': "Hamza Taher",
    'category': 'Sales',
    'description': """
    A link between estate and account modules to create estate invoices
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [],
}

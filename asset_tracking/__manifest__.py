# -*- coding: utf-8 -*-
{
    'name': "Asset Tracking",
    'summary': """
       This module help to tracking asset record""",
    'description': """
       This module help to tracking asset record
    """,
    'author': "Boraq-Group",
    'website': "https://boraq-group.com",
    'category': 'Asset',
    'version': '14.0',
    'images': ['static/description/banner.png'],
    'price': 40,
    "currency":  "EUR",
    'depends': ['account_asset','hr','account'],
    'data': [
        'security/security_view.xml',
        'security/ir.model.access.csv',
        'views/account_asset_view.xml',
        ],
}

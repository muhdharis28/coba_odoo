{
    'name': 'Academic Degree',
    'summary': """
        Modul Name
         Modul Summary""",
    'version': '0.0.1',
    'category': 'Category',
    "author": "Muhammad Haris",
    'description': """
        Belajar Python
    """,
    'depends': [
        'base','web','mail'
    ],
    'data': [
    	'views/degree.xml','security/ir_model_access.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True    
}
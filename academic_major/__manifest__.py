{
    'name': 'Academic Major',
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
        'base','web','mail','academic_degree'
    ],
    'data': [
    	'views/major.xml','security/ir_model_access.xml','views/degree.xml'
    ],
    'installable': True,
    'auto_install': False,
    'application': True    
}
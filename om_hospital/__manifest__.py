{
    "name": "Hospital Management System",
    "author": "Jeff Nyalik",
    "website": "www.jeffnyalik.com",
    "summary": "Odoo module development",
    "description": """ 
         Hospital Management System (HMS) is an integrated software solution designed to manage the administrative, financial, and clinical aspects of a hospital. 
         It aims to streamline operations, enhance patient care, and improve the overall efficiency of hospital workflows. Here are the key features and functionalities of a comprehensive Hospital Management System:
     """,
    "version": "1.0.0",
    "depends": ["base", "sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/xml/menu.xml",
        "views/xml/form_view.xml",
        "views/xml/tree_view.xml",
        "views/xml/patient.xml",
        "views/xml/sale.xml"
    ]
}

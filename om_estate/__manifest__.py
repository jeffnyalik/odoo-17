{
    "name": "Real estate",
    "author": "Jeff Nyalik",

    "depends": ["base", "mail", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/xml/estate_menu.xml",
        "views/xml/estate_tags_menu.xml",
        "views/xml/estate_tags_actions.xml",
        "views/xml/estate_actions.xml",
        "views/xml/estate_form_view.xml",
        "views/xml/estate_tree_view.xml",
        "views/xml/estate_search_view.xml",
        "views/xml/estate_tree_view.xml",
        "views/xml/estate_kanban_view.xml",

        "views/xml/estate_type_actions.xml",
        "views/xml/estate_types_menu.xml",
        "views/xml/estate_property_type_tree.xml",
        "views/xml/estate_prop_type_view.xml",
        "views/xml/users_inherit.xml",
        "data/data.xml" ## sequential value

    ],
    "application": True,
    "installable": True,
    "autoinstall": False
}
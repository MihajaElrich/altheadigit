{
	"name" : "Order Validation Management",
	"version" : "1.0",
	"summary" : "Order Validation Management",
	"sequence" : 4,
	"license" : "LGPL-3",
	"author" : "Muriel Rémi Cyr",
	"description" : """
		Order Validation Management
		===========================
		This module has as main objective to handle which user can or not validate an order
	""",
	"depends" : ['sale_management'],
	"data" : [
		"views/users.xml"
	],
	"application" : True,
	"installable" : True,
	"auto_install" : False
}
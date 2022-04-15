{
	"name" : "Sales Dashboard",
	"version" : "1.0",
	"summary" : "Sales Dashboard",
	"sequence" : 4,
	"license" : "LGPL-3",
	"author" : "Muriel Rémi Cyr",
	"description" : """
		Sales Dashboard
		===============
		This module adds graph view for the sale dashboard
	""",
	"depends" : ['sale_management'],
	"data" : [
		"views/sale.xml",
	],
	"application" : True,
	"installable" : True,
	"auto_install" : False
}
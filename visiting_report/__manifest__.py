{
	"name" : "Visiting Report",
	"version" : "1.0",
	"summary" : "Visiting Report",
	"sequence" : 200,
	"license" : "LGPL-3",
	"author" : "Muriel Rémi Cyr",
	"description" : """
		Visiting Report
		===============
		This module adds a tab in sale.order for visiting report
	""",
	"depends" : ["sale"],
	"data" : [
		"views/sale.xml",
		"views/website.xml",
	],
	"application" : True,
	"installable" : True,
	"auto_install" : False
}
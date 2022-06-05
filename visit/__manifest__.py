{
	"name" : "Visit",
	"version" : "1.0",
	"summary" : "Visit",
	"sequence" : 4,
	"license" : "LGPL-3",
	"author" : "Muriel Rémi Cyr",
	"description" : """
		Visit
		=====
		This module adds new model called visit
	""",
	"depends" : ['sale_management'],
	"data" : [
		"security/ir.model.access.csv",
		"views/visit.xml",
		"views/website.xml",
		"views/sale.xml",
	],
	"application" : True,
	"installable" : True,
	"auto_install" : False
}
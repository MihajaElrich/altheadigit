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
		"security/ir.model.access.csv",
		"views/dashboard.xml",
		"views/dashboard_parameter.xml",
		"views/users.xml",
		# "data/dashboard_parameter_data.xml"
	],
	"application" : True,
	"installable" : True,
	"auto_install" : False,
}
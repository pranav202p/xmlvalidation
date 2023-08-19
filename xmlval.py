import xmlschema as xml


XML_SCHEMA = xml.XMLSchema(r"C:\Users\prana\OneDrive\Documents\xml\emp_schema.xsd")

if XML_SCHEMA.is_valid(r"C:\Users\prana\OneDrive\Documents\xml\employees.xml"):
    print("The xml is vaild")
else:
    print("Sorry, xml is not well formed or valid")
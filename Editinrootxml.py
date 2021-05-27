import xml.etree.ElementTree as ET

tree = ET.parse("testedit.xml")
root = tree.getroot()                                                

for AAA in root.findall('AAA'):
    if AAA.find('CCC'):
        BBB = AAA.find('CCC').find('BBB')
        BBB.text = '33333' + BBB.text

tree.write('/home/kornbotdev/Automaticsoftware/output.xml')

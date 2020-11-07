import xml.etree.ElementTree as ET
from parse.definition import ParsedDoc

def getFile(filename):
    # f = open(filename,encoding='utf-8')
    context = ET.iterparse(filename, events=('end',))
    document = ParsedDoc(filename)
    document.triples_text(context)
    document.output(filename)


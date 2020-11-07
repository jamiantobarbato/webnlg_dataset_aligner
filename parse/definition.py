import os

class ParsedDoc:
    def __init__(self, filename):
        self.name = filename
        self.rdf = []
        self.txt = []

    def triples_text(self,context):
        for event, elem in context:
            if elem.tag == 'modifiedtripleset':
                title = elem.find('mtriple').text
                title_ = title.split(' | ')
                _title_ = '  '.join(title_)
                self.rdf.append(_title_)

            if elem.tag == 'entry':
                lexicalisation = elem.findall('lex')
                strLex = []
                for lex in lexicalisation:
                    strLex.append(lex.text)

                string = '//'.join(strLex)
                self.txt.append(string)

    # Print output files
    def output(self, output):
        try:
            os.mkdir('data/' + output)
        except OSError:
            print("Creation of the directory %s failed" % output)
        else:
            print("Successfully created the directory %s " % output)

        for index, s in enumerate(self.txt):
            sep = s.split('//')

            for chunk in sep:
                with open('data/'+output+'/'+output+'_rdf.txt', 'a') as f:
                    f.write(self.rdf[index]+'\n')
                with open('data/'+output+'/'+output+'_text.txt', 'a') as f:
                    if chunk.endswith('\n'):
                        f.write(chunk)
                    else:
                        f.write(chunk + '\n')
# webnlg_dataset_aligner
Use `main.py -i <inputfile>` from cmd to load the script. A new directory with the file's name will be created inside the **/data** folder, containing two files, respectively **filename_rdf.txt** and **filename_text.txt**. 

> :warning: Since it uses UTF-8 encoding/decoding, some characters might not be recognized; this can cause tools like OpenNMT to throw errors when parsing such lines in the .txt files. It is suggested to manually remove undesidered lines to prevent further errors. 

This script can be used to create an aligned dataset to be fed into NLG, NMT and many other tools. By now, it only works on datasets, like the [WebNLG 2017](https://gitlab.com/shimorina/webnlg-dataset/-/blob/master/README.md) or the WebNLG 2019 ones, that are represented by the following XML structure:

```XML
  <entry category="Artist" eid="Id2" shape="(X (X (X)))" shape_type="chain" size="2">
      <originaltripleset>
        <otriple>Aaron_Bertram | associatedActs | Suburban_Legends</otriple>
        <otriple>Suburban_Legends | genre | Ska</otriple>
      </originaltripleset>
      <originaltripleset>
        <otriple>Aaron_Bertram | associatedMusicalArtist | Suburban_Legends</otriple>
        <otriple>Suburban_Legends | genre | Ska</otriple>
      </originaltripleset>
      <modifiedtripleset>
        <mtriple>Aaron_Bertram | associatedBand/associatedMusicalArtist | Suburban_Legends</mtriple>
        <mtriple>Suburban_Legends | genre | Ska</mtriple>
      </modifiedtripleset>
      <lex comment="good" lid="Id1">Aaron Bertram plays for the Suburban Legends band and their genre is Ska.</lex>
      <lex comment="good" lid="Id2">Aaron Bertram plays for the Suburban Legends band which play Ska music.</lex>
      <lex comment="good" lid="Id3">Aaron Bertram plays for the Suburban Legends band who perform Ska music.</lex>
    </entry>
```

The resulting files will contain a line of text for each triple extracted from the `<mtriple>` tag, like the following:
```
Aaron_Bertram  associatedBand/associatedMusicalArtist  Suburban_Legends 
```
```
Aaron Bertram plays for the Suburban Legends band and their genre is Ska.
```

You can find some extracted data in the **data/examples** folder.

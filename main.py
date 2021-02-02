from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation

record = SeqIO.read("Genome.gb", "genbank")

gd_diagram = GenomeDiagram.Diagram("Tomato Curly Stunt Virus")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()

for feature in record.features:
    if feature.type != "gene":
        #Exclude this feature
        continue
    if len(gd_feature_set) % 5 == 0:
        color = colors.blue
    elif len(gd_feature_set) % 5 == 1:
        color = colors.green
    elif len(gd_feature_set) % 5 == 2:
        color = colors.red
    elif len(gd_feature_set) % 5 == 3:
        color = colors.purple  
    else:
        color = colors.pink
    gd_feature_set.add_feature(feature, sigil="ARROW",
                               color=color, label=True,
                               label_size = 14, label_angle=0)

    #Including features such as EcoRi regonition sites                       
for site, name, color in [("GAATTC","EcoRI",colors.green),
                          ("CCCGGG","SmaI",colors.orange),
                          ("AAGCTT","HindIII",colors.red),
                          ("GGATCC","BamHI",colors.purple)]:
    index = 0
    while True:
        index  = record.seq.find(site, start=index)
        if index == -1 : break
        feature = SeqFeature(FeatureLocation(index, index+len(site)))
        gd_feature_set.add_feature(feature, color=color, name=name,
                                   label=True, label_size = 10,
                                   label_color=color)
        index += len(site)

    gd_diagram.draw(format="circular", circular=True, pagesize=(20*cm,20*cm),
                start=0, end=len(record), circle_core=0.6)
gd_diagram.write("tomato_curly_stuny_virus_cg.png", "PNG")

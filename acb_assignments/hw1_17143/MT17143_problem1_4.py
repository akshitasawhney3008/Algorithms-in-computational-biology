#outfile=open('gccontent.','w')
from Bio import SeqIO
gbk_filename = "mtb.gb"
faa_filename = "mtbc.faa"
input_handle  = open(gbk_filename, "r")
output_handle = open(faa_filename, "w")
with open("mtb.gb", "r") as input,\
open("mtb1.fasta", "w") as output:
    sequences = SeqIO.parse(input, "genbank")
    for rec in sequences:
        ver=rec.id
        #print(type(ver))//
        count = 0
        for iterator in rec.features:
           # print(type(count))//
            if iterator.type=='CDS':
                location=iterator.location
                start = iterator.location.start.position
                stop = iterator.location.end.position
                locus=iterator.qualifiers['locus_tag']
                mylocus = ''.join(locus)
                str=rec.seq[start:stop]
                char_list = list(str)
                countg = 0
                countc = 0
                for c in char_list:
                    if c == 'G':
                        countg += 1
                    elif c == 'C':
                        countc += 1
                print((countg + countc)/(len(char_list)))







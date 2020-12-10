import time
import re
start_time1 = time.time()
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
                print(type(str))
                if 'gene' in iterator.qualifiers.keys():
                    gene = iterator.qualifiers['gene']
                    mystring = ''.join(gene)
                else:
                    gene=None
                my_new_list = list(str)
                my_new_list_2 = []

                #str1=[]
                #print(str)
                idx = 0
                for c in my_new_list:
                    if idx % 60 != 0:
                        my_new_list_2.append(c)
                        #print(c, end='')
                    else:
                        my_new_list_2.append('\n')
                        my_new_list_2.append(c)
                        #print(c, end='')
                    idx += 1

                #for i in range (int(len(str)/60)):
                #    print(i)

                #    str1[i]=str[i*60:(i+1)*60]
                count = count + 1
                if 'gene' in iterator.qualifiers.keys():
                    print(type(ver))
                    print(type(count))
                    print(type(mystring))
                    print(type(mylocus))
                    print(type(start))
                    print(type(stop))


                    output_handle.write(">lcl|%s_gene_%d [gene=%s] [locus_tag=%s] [location=%d..%d]\n%s\n" % (ver,count,mystring,mylocus,start,stop,
                       "".join(my_new_list_2)))
                else:
                    output_handle.write(">lcl|%s_gene_%d  [locus_tag=%s] [location=%d..%d]\n%s\n" % (ver, count, mylocus, start, stop,"".join(my_new_list_2)))
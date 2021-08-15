from requests import get

from panel_worker import load_panel


BASE_URL = "https://api.genome.ucsc.edu/getData/sequence?genome=hg19;"

panel = load_panel("../assignment/IAD143293_241_Designed.bed")
with open("target_seqs.fasta", "w") as f:
    for target in panel:
        dna_address = f"chrom={target.chromosome};start={target.start-1};end={target.end}"
        url = BASE_URL + dna_address
        seq = get(url).json()["dna"]

        f.write(f">ID={target.tid},{target.chromosome}:{target.start}-{target.end}\n")
        f.write(seq + "\n")
        print(seq)

from typing import List, Tuple, Optional


class Target:
    def __init__(self, tid, chromosome, start, end, gene_name=None, exon_number=None):
        self.tid = tid
        self.chromosome = chromosome
        self.start = start
        self.end = end
        self.gene_name = gene_name
        self.exon_number = exon_number

    def __str__(self):
        return f"{self.tid} {self.chromosome} {self.start} {self.end} {self.gene_name} {self.exon_number}"

    def __repr__(self):
        return f"Target({self.tid},{self.chromosome},{self.start},{self.end},{self.gene_name},{self.exon_number})"


def annotate_gene_name(panel: List[Target], gene_info: List[str]) -> Optional[int]:
    name, chrom, s, e = gene_info[0], gene_info[1], int(gene_info[3]), int(gene_info[4])
    for i, target in enumerate(panel):
        if chrom == target.chromosome:
            if (s <= target.start <= e) and (s <= target.end <= e):
                target.gene_name = name
                return i


def annotate_exon_number(target: Target, ):
    pass


panel: List[Target] = []
with open("IAD143293_241_Designed.bed", "r") as f:
    f.readline()
    for i, line in enumerate(f):
        chrom, s, e = line.split()[:3]
        panel.append(Target(i, chrom, int(s), int(e)))


with open("genes.txt", "r") as g:
    g.readline()
    for line in g:
        gene_info = line.split()
        annotated = annotate_gene_name(panel, gene_info)
        if annotated:
            starts = list(map(int, gene_info[8].rstrip(",").split(",")))
            ends = list(map(int, gene_info[9].rstrip(",").split(",")))
            print(panel[annotated], starts, ends)
            annotate_exon_number(panel[annotated], starts, ends)


print(panel)

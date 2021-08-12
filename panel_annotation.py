from typing import List, Optional


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


def annotate_gene_name(panel: List[Target], gene_info: List[str]) -> List[int]:
    name, chrom, s, e = gene_info[0], gene_info[1], int(gene_info[3]), int(gene_info[4])
    annotated = []
    for i, target in enumerate(panel):
        if chrom == target.chromosome:
            if (s <= target.start <= e) and (s <= target.end <= e):
                if target.gene_name and target.exon_number:
                    print(f"Warning! Double annotation of target {target.tid} by name {name}")
                    continue
                target.gene_name = name
                annotated.append(i)
    return annotated


def annotate_exon_number(target: Target, ex_starts: List[int], ex_ends: List[int]):
    ex_counter = 1
    for ex_start, ex_end in zip(ex_starts, ex_ends):
        if (ex_start <= target.end) and (target.start <= ex_end):
            target.exon_number = ex_counter
            return
        ex_counter += 1
    print(f"Warning! target {target.tid} was not annotated by exon number")


panel: List[Target] = []
with open("IAD143293_241_Designed.bed", "r") as f:
    f.readline()
    for i, line in enumerate(f):
        chrom, s, e = line.split()[:3]
        panel.append(Target(i, chrom, int(s), int(e)))


print(panel)


with open("genes.txt", "r") as g:
    g.readline()
    for line in g:
        gene_info = line.split()
        annotated = annotate_gene_name(panel, gene_info)
        for ann in annotated:
            starts = list(map(int, gene_info[8].rstrip(",").split(",")))
            ends = list(map(int, gene_info[9].rstrip(",").split(",")))
            # print(panel[annotated], starts, ends)
            annotate_exon_number(panel[ann], starts, ends)


print(panel)

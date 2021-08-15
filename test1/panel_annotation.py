from typing import List

from panel_worker import Target, load_panel, add_info_to_panel_file


def annotate_gene_name(panel: List[Target], gene_info: List[str]) -> List[int]:
    name, chrom, s, e = gene_info[12], gene_info[2], int(gene_info[4]), int(gene_info[5])
    annotated = []
    for i, target in enumerate(panel):
        if chrom == target.chromosome:
            if s <= target.end and target.start <= e:
                if target.gene_name and target.exon_number:
                    print(f"Warning! Double annotation of target {target.tid} by name {name}")
                    continue
                target.gene_name = name
                annotated.append(i)
    return annotated


def annotate_by_exon_number(target: Target, ex_starts: List[int], ex_ends: List[int]):
    ex_counter = 1
    for ex_start, ex_end in zip(ex_starts, ex_ends):
        if (ex_start <= target.end) and (target.start <= ex_end):
            target.exon_number = ex_counter
            return
        ex_counter += 1
    print(f"Warning! target {target.tid} was not annotated by exon number")


panel = load_panel("../assignment/IAD143293_241_Designed.bed")


with open("NCBI_ref_genes.txt", "r") as g:
    g.readline()
    for line in g:
        gene_info = line.split()
        annotated = annotate_gene_name(panel, gene_info)
        for ann in annotated:
            starts = list(map(int, gene_info[9].rstrip(",").split(",")))
            ends = list(map(int, gene_info[10].rstrip(",").split(",")))
            annotate_by_exon_number(panel[ann], starts, ends)


print(panel)

add_info_to_panel_file("../assignment/IAD143293_241_Designed.bed", panel)

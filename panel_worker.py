from os import path
from typing import List


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


class PanelFileNotCorrespondError(Exception):
    pass


def load_panel(filename: str) -> List[Target]:
    panel: List[Target] = []
    with open(filename, "r") as f:
        f.readline()
        for i, line in enumerate(f):
            chrom, s, e = line.split()[:3]
            panel.append(Target(i, chrom, int(s), int(e)))

    print(panel)
    return panel


def add_info_to_panel_file(filename: str, panel: List[Target]):
    with open(filename, "r") as r, open(path.basename(filename).split(".")[0] + "_mod.txt", "w") as w:
        w.write(r.readline())
        for i, line in enumerate(r):
            row = line.split()
            if row[0] == panel[i].chromosome and int(row[1]) == panel[i].start and int(row[2]) == panel[i].end:
                row[5] = row[5] + f";gene_name={panel[i].gene_name};exon_number={panel[i].exon_number}"
                w.write("\t".join(row) + "\n")
            else:
                raise PanelFileNotCorrespondError

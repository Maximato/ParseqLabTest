import pandas as pd
import io


genes = set()
with open("IAD143293_241_Designed_mod.txt", "r") as f:
    f.readline()
    for line in f:
        genes.add(line.split()[5].split(";")[2][10:])

print(genes)
print(f"count of genes: {len(genes)}")


panel_diseases = io.StringIO()
with open("curated_gene_disease_associations.tsv", "r") as f:
    panel_diseases.write(f.readline())
    for line in f:
        if line.split()[1] in genes:
            panel_diseases.write(line)


panel_diseases.seek(0)
df = pd.read_csv(panel_diseases, sep="\t")

panel_diseases_counts = df.groupby("diseaseName").size().reset_index(name='counts')\
    .sort_values("counts", ascending=False).reset_index(drop=True)

with open("panel_diseases_counts.csv", "w") as f:
    f.write(panel_diseases_counts.to_csv(sep=";", line_terminator="\n"))

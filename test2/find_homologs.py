with open("h37_blast_hits.csv", "r") as f:
    for line in f:
        row = line.rstrip().split(",")
        ts, te = row[1].split(":")[1].split("-")
        hs, he = row[9], row[10]

        target_length = abs(int(te) - int(ts))
        hit_length = abs(int(he) - int(hs))

        if float(row[3]) == 100 and target_length == hit_length and (ts != hs or te != he) and row[2].startswith("NC"):
            print(row[0] + ",", f"target={row[1]},", f"not_target={row[2]}:{row[9]}-{row[10]}", f"identity={row[3]}")

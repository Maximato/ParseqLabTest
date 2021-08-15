## Задание № 1

### Аннотация панели

Данные по известным генам и позициям экзонов 
для референсной ДНК последовательности человека hg19 
были загружены с ресурса [UCSC](http://genome.ucsc.edu/) 
в разделе `TableBrowser`.

![Alt text](pics/ref_genes_load.png?raw=true)

Позиции генов и экзонов из файла `NCBI_ref_genes.txt` использовались 
для аннотации исходного файла панели. 

Написанный скрипт `panel_annotation.py` считывает 
исходный файл панели, для каждого участка добавляет 
в последний столбец дополнительную информацию 
(название гена и номер экзона), записывает данные
в новый файл панели `IAD143293_241_Designed_mod.txt`.

### Диагностика заболеваний

Данные об ассоциированных с генами заболеваниях были загружены с ресурса 
[DisGeNET](https://www.disgenet.org/home/) - файл `curated_gene_disease_associations.tsv`.

Чтобы сделать предположение о заболеваниях, для которых предназначена данная панель,
был написан скрипт `disease_counter.py`. Данный скрипт
считывает файл проаннотированной панели, собирает набор всех генов панели,
собирает информацию о заболеваниях для набора генов панели (из
файла `curated_gene_disease_associations.tsv`), подсчитывает
сколько раз каждое из заболеваний встречается в итоговой таблице и
записывает результат в `panel_diseases_counts.csv`.
Исходя из полученных данных, можно предположить, что панель предназначена 
для диагностики различных типов диабета. 


## Задание № 2

Для сбора последовательностей регионов панели был написан 
скрипт `seq_collector.py`, использующий REST API ресурса [UCSC](http://genome.ucsc.edu/).
Полученные последовательности `target_seqs.fasta` были 
загружены в [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) для 
поиска гомологичных регионов.

![Alt text](pics/blast_load.png?raw=true)

Результаты BLAST выгружены в виде таблицы (Hit Table(csv) - `h37_blast_hits.csv`)

![Alt text](pics/blast_results.png?raw=true)

Написан скрипт `find_homologs.py`, выполняющий поиск нецелевых
регионов по таблице `h37_blast_hits.csv`. Нецелевым регионом
считается тот, который имеет 100% гомологичность и несовпадающие
с целевым координаты.

Таким образом, для региона панели chr9:135944485-135944807 
(AMPL7166072478;gene_name=CEL;exon_number=9) был обнаружен
нецелевой участок chr9:135960269-135960591 в гене CELP.
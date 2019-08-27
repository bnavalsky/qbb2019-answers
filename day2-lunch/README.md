$head -n 40000 SRR072893.fastq > ../day2-lunch/SRR072893.10k.fastq #to get first 40k lines in order to get first 10k reads
$ fastqc SRR072893.10k.fastq 
$ open SRR072893.10k_fastqc.html #look at quality report
$ hisat2 -p 4 -x ~/qbb2019-answers/genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893.10k.sam
$ samtools sort SRR072893.10k.sam > SRR072893.10k.bam
$ samtools index SRR072893.10k.bam
$ stringtie SRR072893.10k.bam -G ~/qbb2019-answers/genomes/BDGP6.Ensembl.81.gtf -o SRR072893.10k.gtf -p 4 -B -e

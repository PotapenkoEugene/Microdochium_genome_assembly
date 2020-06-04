# De novo assembly and annotation of the *Microdochium sp.* genome
Microdochium is a genus of ascomycete fungi. Our goal is to assemble and annotate 3 isolates of *Microdochium sp.* 
Previousy genome of *M. bolleyi* was assembled and annotated [1].

## Goal
- To assemble and annotate Microdochium sp. genome

## Objectives
- Quality control
- Pre-processing of raw data
- Decontamination
- Assembly
- Quality control
- Structure annotation
- Functional annotation

## Data
Microdochium is a genus of ascomycete fungi. Genomes of 3 isolates of plant pathogen *Microdochium sp.* were sequenced in Kazan Scientific Center of RAS. Reads in FASTQ format were obtained using Illumina MiSeq.

## Methods
Quality check was done with FASTQC (v0.11.5) [2]. Illumina adapters were trimmed by AfterQC (v0.9.6) [3]. Reads were assembled using SPAdes (v3.14.0) genome assembler [4]. Assemblies were evaluated by the QUAST tool. We checked contigs for contaminations with KAIJU(web server) [5]/SIDR(alpha version) [6]/Blobtools2(v2.2.0) [7]. Contaminated reads were filtered out by aligning (bwa-mem v0.7.17-r1188) [8] them to trusted contigs. PE and SE reads were taken from alignments with Samtools fastq (v1.9) [9] and assembled with SPAdes. After comparing assemblies, we found out that decontamination using Blobtools2 was more effective. The assembly quality was evaluated with QUAST(v5.0.2) [10]. Quantitative assessment of genome assembly completeness was done with BUSCO [11]. We selected the best assembly for further annotation. To mask repetitions we used the RepeatModeler tool (v2.0.1. Combined Dhttps://github.com/blobtoolkit/blobtools2atabase: Dfam_3.0, RepBase-20170127) [12]. Structural annotation was performed with AUGUSTUS (v3.2.3) [13]. A genomic annotation of a close related species (*Microdochium bolleyi*) was used for AUGUSTUS training. Then KEGG [14] orthology-based functional annotation was done.

## Code
You can found files with code in this repository in **Scripts** folder.
## Results
Size of the assembled genomes were 36.7/36.8/37.2 mb. Genomes consisted of  1360/817/272 scaffolds. 10 304 predicted genes were found. Median gene length is 1,454 bp and median protein length is 426 amino acids. The estimated percent of genome repeat is 4.59%. Functional annotation was done.
We are planning to reassemble the genome with Nanopore reads and use RNA-seq reads for more precise annotation.

## References
[1]: David, Aaron S., et al. "Draft genome sequence of Microdochium bolleyi, a dark septate fungal endophyte of beach grass." Genome Announc. 4.2 (2016): e00270-16.

[2]: Andrews S. (2010). FastQC: a quality control tool for high throughput sequence data. Available online at: http://www.bioinformatics.babraham.ac.uk/projects/fastqc

[3]: Shifu Chen, Tanxiao Huang, Yanqing Zhou, Yue Han, Mingyan Xu and Jia Gu. AfterQC: automatic filtering, trimming, error removing and quality control for fastq data. BMC Bioinformatics 2017 18(Suppl 3):80

[4]: Nurk S. et al. (2013) Assembling Genomes and Mini-metagenomes from Highly Chimeric Reads. In: Deng M., Jiang R., Sun F., Zhang X. (eds) Research in Computational Molecular Biology. RECOMB 2013. Lecture Notes in Computer Science, vol 7821. Springer, Berlin, Heidelberg

[5]:Menzel, P., Ng, K. & Krogh, A. Fast and sensitive taxonomic classification for metagenomics with Kaiju. Nat Commun 7, 11257 (2016). https://doi.org/10.1038/ncomms11257

[6]: link to a web page: https://github.com/damurdock/SIDR

[7]: link to a web page:: https://github.com/blobtoolkit/blobtools2 

[8]: Li H. (2013) Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM. arXiv:1303.3997v1 [q-bio.GN].

[9]: link to a web page: https://github.com/samtools/samtools

[10]: Alla Mikheenko, Andrey Prjibelski, Vladislav Saveliev, Dmitry Antipov, Alexey Gurevich,
Versatile genome assembly evaluation with QUAST-LG,
Bioinformatics (2018) 34 (13): i142-i150. doi: 10.1093/bioinformatics/bty266

[11]: Seppey M., Manni M., Zdobnov E.M. (2019) BUSCO: Assessing Genome Assembly and Annotation Completeness. In: Kollmar M. (eds) Gene Prediction. Methods in Molecular Biology, vol 1962. Humana, New York, NY. 2019 doi.org/10.1007/978-1-4939-9173-0_14

[12]: Flynn, Jullien M., et al. "RepeatModeler2 for automated genomic discovery of transposable element families." Proceedings of the National Academy of Sciences 117.17 (2020): 9451-9457.

[13]: Mario Stanke, Rasmus Steinkamp, Stephan Waack and Burkhard Morgenstern (2004)
"AUGUSTUS: a web server for gene finding in eukaryotes"
Nucleic Acids Research, Vol. 32, W309-W312 

[14]: Kanehisa, M. and Goto, S.; KEGG: Kyoto Encyclopedia of Genes and Genomes. Nucleic Acids Res. 28, 27-30 (2000). 


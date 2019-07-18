#!/usr/bin/env bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --job-name=velveth
#SBATCH --output=velveth.out
#SBATCH --error=velveth.err
#SBATCH --time=0-00:30:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=3

conda deactivate
conda deactivate
conda deactivate
conda activate bgmp_py3

/usr/bin/time -v velveth /home/pberry/bgmp/Bi621/PS6/31 31 -fastq -short /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched -shortPaired -separate /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1 /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2

/usr/bin/time -v velveth /home/pberry/bgmp/Bi621/PS6/41 41 -fastq -short /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched -shortPaired -separate /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1 /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2

/usr/bin/time -v velveth /home/pberry/bgmp/Bi621/PS6/49 49 -fastq -short /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched -shortPaired -separate /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1 /projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2

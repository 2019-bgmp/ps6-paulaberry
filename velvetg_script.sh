#!/usr/bin/env bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --job-name=velvetg
#SBATCH --output=velvetg.out
#SBATCH --error=velvetg.err
#SBATCH --time=0-00:30:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=5

conda deactivate
conda deactivate
conda deactivate
conda activate bgmp_py3

/usr/bin/time -v velvetg /home/pberry/bgmp/Bi621/PS6/31

/usr/bin/time -v velvetg /home/pberry/bgmp/Bi621/PS6/41

/usr/bin/time -v velvetg /home/pberry/bgmp/Bi621/PS6/49

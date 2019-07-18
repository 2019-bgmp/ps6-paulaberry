#!/usr/bin/env python3

#A script to return information about read lengths from a fastq file.

import math

f1 = open("hpc:/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched", "r")
f2 = open("hpc:/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1", "r")
f3 = open("hpc:/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2", "r")


def readcounter(file):
	"""A function to return the number of reads in a fastq file."""
	counter = 0
	read_counter = 0
	for line in file:
		counter = counter + 1
		if counter % 4 == 2:
			read_counter = read_counter + 1
	return read_counter

def total_read_length(file):
	"""A function to return the total length of all sequences in a fastq file."""
	counter = 0
	for line in file:
		seq = ""
		counter = counter + 1
		if counter % 4 == 2:
			line = line.strip()
			seq = str(seq) + str(line)

		return len(seq)

print("Unmatched file is " + str(total_read_length(f1)) + "nucleotides long.")
print("Unmatched file has an average read length of " + str(total_read_length(f1) / readcounter(f1)) " nucleotides.")
print()

print("fq_1 file is " + str(total_read_length(f2)) + " nucleotides long.")
print("Unmatched file has an average read length of " + str(total_read_length(f2) / readcounter(f2)) " nucleotides.")
print()

print("fq_2 file is " + str(total_read_length(f3)) + " nucleotides long.")
print("Unmatched file has an average read length of " + str(total_read_length(f3) / readcounter(f3)) " nucleotides.")

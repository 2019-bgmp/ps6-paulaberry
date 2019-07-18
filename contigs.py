#!/usr/bin/env python3
#A script to return information about a fasta file containing contigs.

import re
import math

kmer_len = 49 # set kmer length value

def header_values(line):
	"""A function that returns the values of Ck (kmerized length of contig) and coverage for an individual read"""
	fasta_id = str(line)
	id_array = re.split(r"_", str(line))
	Ck = id_array[3]
	coverage = id_array[5]
	return Ck, coverage

def read_lengths(Ck, kmer_len):
	"""A function that returns the physical length of a read from the Ck read"""
	read_length = int(Ck) + int(kmer_len) - 1
	#print(read_length)
	return read_length

def list_mean(any_list):
	"""A function to return the mean value of a list"""
	list_sum = sum(any_list)
	mean = list_sum / len(any_list)
	return mean

def list_median(any_list):
	"""A function to return the median value of any list"""
	any_list.sort()
	if len(any_list) % 2 == 0:
		med_low = len(any_list) // 2
		med_high = med_low + 1
		median = (any_list[med_low] + any_list[med_high]) / 2

	else:
		med = (len(any_list) // 2) + 1
		median = any_list[med]

	return median

def N50_calc(any_list):
	"""A function to return the N50 value of any list of contig lengths"""
	any_list.sort(reverse = True) # sort largest to smallest value
	threshhold = sum(any_list) / 2 # calculate threshhold for N50 value
	running_sum = 0
	element_counter = 0
	for i in any_list:
		running_sum = running_sum + i
		if running_sum >= threshhold:
			return any_list[element_counter]
		else:
			element_counter = element_counter + 1

def histogram_dictionary(any_list, bucket, dictionary):
	"""A function to populate a dictionary of histogram values"""
	any_list.sort()
	max_range = (max(any_list) // bucket) * 100
	for i in range(0, max_range, bucket):
		dictionary[i] = 0
		#print(histogram)
	for i in any_list:
		if ((int(i) // int(bucket)) * int(bucket)) in histogram:
			dictionary[((int(i) // int(bucket)) * int(bucket))] = dictionary[((int(i) // int(bucket)) * int(bucket))] + 1
		else:
			dictionary[((int(i) // int(bucket)) * int(bucket))] = 1

f = open("contigs.fa", "r")
Ck_list = []
coverage_list = []
read_length_list = []
histogram = {}
read_counter = 0

for line in f:
	line = line.strip()
	if re.search(r">NODE_[0-9]+_length_[0-9]+_cov_[0-9]+.[0-9]",line) != None:
		read_counter = read_counter + 1
		Ck, coverage = header_values(line)
		read_length = read_lengths(Ck, kmer_len)
		Ck_list.append(Ck)
		coverage_list.append(float(coverage))
		read_length_list.append(int(read_length))

f.close()



print("Total number of contigs: " + str(read_counter))
print("Maximum contig length: " + str(max(read_length_list)))
print("Mean contig length: " + str(list_mean(read_length_list)))
print("Total length of genome assembly: " + str(sum(read_length_list)))
print("Mean depth of coverage: " + str(list_mean(coverage_list)))
print("N50: " + str(N50_calc(read_length_list)))

histogram_dictionary(read_length_list, 100, histogram)
print("# Contig length	Number of Contigs in this category")
for i in histogram:
	print(str(i) + "	" + str(histogram[i]))

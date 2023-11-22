import os
import pandas as pd

fasta_file = r"C:\Users\FishmanVS\Downloads\splice_test_1.fa"

with open(fasta_file) as fin:
	l = fin.readline().split()[1][6:]
	chrm = l.split(":")[0]
	start = int(l.split(":")[1].split("-")[0])
	end = int(l.split(":")[1].split("-")[1])

# print (chrm, start)

webservice_out_folder = r"C:\Users\FishmanVS\Downloads\request_2023-11-22_59333_archive"
webservice_out_folder = webservice_out_folder.replace("\\","/")

with open(os.path.join(webservice_out_folder,"roi.converted.bed"), "w") as fout:
	fout.write("\t".join([chrm, str(start), str(end), "ROI"]))

files = os.listdir(webservice_out_folder)
for file in files:
	file = os.path.join(webservice_out_folder,file)
	if file.endswith(".bed") and not file.endswith(".converted.bed"):
		data = pd.read_csv(file,skiprows=1,
							header=None, sep="\s", engine='python')
		data.iloc[:,0] = [chrm]*len(data)
		data.iloc[:,1] = data.iloc[:,1] + start
		data.iloc[:,2] = data.iloc[:,2] + start
		data.to_csv(file+".converted.bed",header=False, index=False, sep="\t")
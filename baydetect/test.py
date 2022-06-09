import os
import fnmatch

img_dir_input = "C:\BayDetect\example\image_data\Example_Forest\Raw_Photos"
org_img_dir_input = str(img_dir_input.replace("\\", "/")) + "/"

common_dirname_input = "Session*"
second_common_dirname = "100CU*"

# Lists for all
org_img_dirpath = []
pattern1_list = []
pattern2_list = []

img_paths = []
dataset_station = []
station = []
session = []

dataset = str


for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
    for dirname_p1 in fnmatch.filter(dirs, common_dirname_input):
        pattern1_list.append(os.path.join(path, dirname_p1).replace("\\", "/"))

for path, dirs, files in os.walk(os.path.abspath(org_img_dir_input)):
    for dirname_p2 in fnmatch.filter(dirs, second_common_dirname):
        pattern2_list.append(dirname_p2)

for ip1, ip2 in zip(pattern1_list, pattern2_list):
    org_img_dirpath.append(os.path.join(ip1, ip2).replace("\\", "/"))

print("\nSAMPLE PATH WHERE IMAGES ARE STORED IN: \n" + org_img_dirpath[0].split()[-1] + "/" + "\n")


for idirpaths in org_img_dirpath:
    for dirpath, dirnames, files in os.walk(idirpaths):
        if files:
            img_paths.append(''.join(idirpaths.split()[-1]))
            session.append(''.join(idirpaths.split('/')[-2]))
            dataset_station.append(''.join(idirpaths.split('/')[-3]))
        if not files:
            pass

print("\nList of Paths to Folders Contain Images: ")
print(img_paths)

print("\nList of Dataset Stations: ")
print(dataset_station)

for name in dataset_station:
    dataset = ''.join(name.split('_')[0])
    station.append('_'.join(name.split('_')[1:]))

print("\nDataset Name: " + dataset)

print("\nList of Stations: ")
print(station)

print("\nList of Sessions: ")
print(session)

input_MD_json_dir = "C:\BayDetect\example\metadata\Example_Forest\EF_JSON\EF_MegaDetected"
input_csv_dir = "C:\BayDetect\example\metadata\Example_Forest\EF_CSV"
input_txtcmds_dir = "C:\BayDetect\example\metadata\Example_Forest\EF_batch_commands\pf3_mdJSONtoCSV"

MD_json_dir_input = input_MD_json_dir.replace("\\", "/") + "/"
csv_dir_input = input_csv_dir.replace("\\", "/") + "/"
txtcmds_dir_input = input_txtcmds_dir.replace("\\", "/") + "/"

md_json_fullnames = []
md_json_withMD = []
csv_woMeta = []

for (dirpath, dirnames, filenames) in os.walk(MD_json_dir_input):
    for ifilenames in filenames:
        md_json_fullnames.append(os.path.join(dirpath, ifilenames))
        json_names, extension = os.path.splitext(ifilenames)
        md_json_withMD.append(json_names)

for iname in md_json_withMD:
    icsv_names = '_'.join(iname.split('_')[0:5])
    csv_woMeta.append(icsv_names)

print("\nIMAGE FOLDER PATHS: ")
print(org_img_dirpath)

print("\nPaths to MegaDetected JSON files: ")
print(md_json_fullnames)

print("\nMegaDetected JSON filenames WITHOUT `.json`: ")
print(md_json_withMD)

print("\nFirst part of CSV filenames: ")
print(csv_woMeta)

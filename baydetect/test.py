import os

org_img_dirpath =
mdJSONDir =
csvDir =
txtOutputDir =

md_json_paths = []
md_json_names = []
csv_woMeta = []

for (dirpath, dirnames, filenames) in os.walk(mdJSONDir):
    for ifilenames in filenames:
        md_json_paths.append(os.path.join(dirpath, ifilenames))

    for ifilenames in range(len(filenames)):
        fullnames = filenames[ifilenames]
        json_names, extension = os.path.splitext(fullnames)
        md_json_names.append(json_names)

    print(md_json_names)

for iname in md_json_names:
    icsv_names = '_'.join(iname.split('_')[0:5])
    csv_woMeta.append(icsv_names)

print("\nSelected IMAGE FOLDERS: ")
print(org_img_dirpath)

print("\nSelected JSON files: ")
print(md_json_paths)

print("\nSelected CSV files: ")
print(csv_woMeta)

for ista, isess, iorg_dirpath, imd_json_paths, icsv_woMeta in zip(self.station, self.session,
                                                                  self.org_img_dirpath,
                                                                  md_json_paths, csv_woMeta):
    create = open(f"{txtOutputDir}pf3_mdJSONToCSV_{self.dataset}_{ista}_{isess}.txt", "a")
    create.write(f"1\n"
                 f"2\n"
                 f"{iorg_dirpath}/\n"
                 f"{imd_json_paths}\n"
                 f"{csvDir}{icsv_woMeta}_Meta.csv\n")
    create.close()
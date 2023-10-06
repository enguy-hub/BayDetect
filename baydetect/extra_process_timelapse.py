import os
import ffmpeg

# Define the input and output folders
input_folder = "./Plotwatcher/KW_003/Session_1_27112018/"

# Iterate through each .tlv file in the input folder
for (root,dirs,files) in os.walk(input_folder):
    for filename in files:
        # print(filename)

        if filename.endswith(".TLV"):

            inputfile_fullpath = os.path.join(root, filename).replace("\\", "/")
            print(inputfile_fullpath)

            filename_without_ext = filename.split('.')[0]
            print(filename_without_ext) 

            parentfolder_path = os.path.dirname(inputfile_fullpath)
            print(parentfolder_path)

            output_dir = os.path.join(parentfolder_path, filename_without_ext).replace("\\", "/") + "_images/"
            print(output_dir)

            # Create the output folder if it does not exist
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)

            outputfile_fullpath = os.path.join(output_dir, filename_without_ext) + "_%04d.jpg"
            print(outputfile_fullpath)

            # Convert the .tlv file to an .avi file using tlvlib
            (
                ffmpeg
                .input(inputfile_fullpath)
                .output(outputfile_fullpath, start_number=0)
                .overwrite_output()
                .run(quiet=True)
            )

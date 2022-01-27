"""This module contains processing functions used for PRE and POST MegaDetector batch processing."""

import os
import json
import shutil
import PIL.Image
import pandas as pd

from PIL.ExifTags import TAGS
from PIL.ExifTags import GPSTAGS

""" Brief description of what each processing function does """
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/----- PRE Processing Functions -----/
##pf1 | md_json_creator(): creates a JSON file contains all image paths inside a given a directory, use for 
MegaDetection batch processing.

/----- POST Processing Functions -----/
#pf2 | md_csv_converter(): converts the output JSON file from MegaDetection batch processing into a CSV file with 
six columns "Image Name", "Flash", "Location", "Station", "Session", "Predicted Category", and "Image Path".

#pf2_supp | get_exif(): supporting function for md_csv_converter().

#pf3_0 | sort_images_csv(): sorts the MegaDetected image into four categories of folders "Empty", "Animal" 
(for value 0), "Person" (for value 1), "Vehicle" (for value 2).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


# ID: pf1 || md_json_creator()
def md_json_creator():
    """
    This function create JSON file contains the paths to all the ".JPG" image of a directory given by the user.

    For LWF, this JSON that will primarily be use as input JSON file for MegaDetector batch processing
    ("run_tf_detector_batch")

    When execute the function, it will first prompt the user to enter the absolute path of the directory which
    contains all subdirectories and image that the user would like to run MegaDetector on. Then it will ask the
    user to give a name and a path for the new output json file.

    Parameters:
        usr_input_dir (str): the absolute path of the directory which contains all subdirectories and image, that
        the user would like to run MegaDetector on

        usr_input_name (str): the path and name of where the output json file will be saved (end with '.json'), if no
        path is given, the json file will be saved at the same directory as where this script is stored.

    Returns: None

    Output:
        JSON file will be saved at where user defined in the "usr_output_json" prompt

    """

    usr_input_dir = input("Enter the absolute path of the directory containing the images that you would like to "
                          "execute `run_tf_detector_batch.py` on (end with `/`): ")

    usr_input_name = input("Give a name and absolute path of where the `batch-input` JSON file will be saved at "
                           "(end with '*_BatchInput.json'): ")

    ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

    files = []
    # p = path, d = dirs, f = files
    for p, d, f in os.walk(usr_input_dir):
        for name in f:
            if name.endswith(ext):
                files.append(os.path.join(p, name))

    with open(usr_input_name, 'w') as f:
        print(json.dump(files, f, indent=4))

    return print('Done!')


# ID: pf2_supp || Supporting function for md_csv_converter()
def get_exif(source_images_path):
    """
    This function takes the original images as input and returns the exif cameratrap_data of the corresponding images.

    Parameters:
        source_images_path (str): the path of the images folder

    Returns:
        df_exif: A dataframe containing the exif cameratrap_data of the images in the given folder

    """
    lst_dict = []
    ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

    for image_name in os.listdir(source_images_path):
        if image_name.endswith(ext):
            image = PIL.Image.open(os.path.join(source_images_path, image_name))
            exif = image._getexif()
            if exif is None:
                return
            exif_data = {}
            exif_data['Image Name'] = image_name
            for tag_id, value in exif.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    gps_data = {}
                    for t in value:
                        gps_tag = GPSTAGS.get(t, t)
                        gps_data[gps_tag] = value[t]
                    exif_data[tag] = gps_data
                else:
                    exif_data[tag] = value
            lst_dict.append(exif_data)

    df_exif = pd.DataFrame.from_dict(lst_dict)

    return df_exif


# ID: pf2 || md_csv_converter()
def md_csv_converter():
    """
     This function converts the output JSON file from MegaDetector batch processing" into a CSV classified_metadata file
     . The CSV classified_metadata file will contains the image in the following seven columns "Image Name",
     "Flash", "Location", "Station", "Session", "Predicted Category", "Image Path", and "DateTime". It combines the
     dataframe created from get_exif() and the dataframe created from the output JSON file from MegaDetector batch
     processing.

     ** The conversion is done primarily based on the name and the location path of each image in the output JSON file
     from MegaDetector batch processing".

     Parameters:
         usr_input_dir(str): the absolute path to the image folder that you ran MegaDetector batch processing on

         usr_input_json(str): the absolute path to the '*_MegaDetected.json' file resulted from MegaDetector
         batch processing (end with .json)

         usr_output_csv(str): the absolute path and name (end with '.csv') of where the output csv file will be saved,
         if no path is given, the json file will be saved at the same directory as where this script is stored.

     Returns: None

     Output:
         CSV classified_metadata file saved at where user defined in the "usr_output_csv" prompt

     """
    usr_input_dir = input("Enter the absolute path of the image directory that you just created a `*_MegaDetected.json`"
                          " file for and would like to perform a CSV metadata conversion on (end with `/`): ")

    usr_input_json = input("Enter the absolute path to the `*_MegaDetected.json` file that you would like to perform "
                           "the CSV metadata conversion on (end with '*_MegaDetected.json'): ")

    usr_output_csv = input("Give a name and absolute path to where the CSV metadata file will be saved at "
                           "(end with '*_Meta.csv'): ")

    input_json = open(usr_input_json, 'r')
    json_info = json.load(input_json)

    df_exif = get_exif(usr_input_dir)
    df_json = pd.DataFrame()

    for i in range(len(list(json_info['images']))):

        imageName = list(json_info['images'][i].values())[0].split('/')[11]
        session = list(json_info['images'][i].values())[0].split('/')[9]
        station = list(json_info['images'][i].values())[0].split('/')[8]

        imagePath = list(json_info['images'][i].values())[0]

        trigger = imageName[2:7]

        detection_box = list(json_info['images'][i].values())[2]
        bb_numbers = len(detection_box)

        pred_category, confidence, bb_locations, y_lower = [], [], [], []

        if bb_numbers != 0:
            for b in range(bb_numbers):
                pred_category.append(list(detection_box[b].values())[0])
                confidence.append(list(detection_box[b].values())[1])
                bb_locations.append(list(detection_box[b].values())[2])
        else:
            pred_category.append('0')

        for _ in bb_locations:
            y_lower.append(max([loc[3] for loc in bb_locations]))

        y_lower = list(set(y_lower))

        data = imageName, trigger, station, session, str(
            bb_numbers), pred_category, confidence, bb_locations, y_lower, imagePath
        data = [list(data)]

        df_single = pd.DataFrame(data, columns=['Image Name', 'Trigger', 'Station', 'Session', 'Number of BBs',
                                                'Predicted Category', 'Confidence', 'Location of BBs', 'Y Lower',
                                                'Image Path'])

        df_json = pd.concat([df_json, df_single])

        df_final = pd.merge(df_exif[['Image Name', 'DateTime']], df_json, on='Image Name')

        df_final.to_csv(usr_output_csv, index=False)

    return print('Done!')


# ID: pf3 || sort_images_csv()
def sort_images_csv():  # input_path, csv_input
    """
    This function takes the user inputs of two things: the absolute path of the image folder that user wish to sort by
    categories and the absolute path to the CSV classified_metadata file of that image folder. It will then sort the
    image in that folder into their according folders based on their "Predicted Category" values in the CSV file.
    The four categories folders are "Empty", "Animal" (for value 0), "Person" (for value 1), "Vehicle" (for value 2)

    When execute the function, it will first prompt the user to enter the absolute path of the image folder that user
    wish to sort by categories. Then it will ask the user to enter the absolute path of the CSV classified_metadata file
    of that image folder.

    Parameters:
        usr_input_dir (str): the absolute path of the image folder that user wish to sort by categories

        usr_input_csv (str): the absolute path of the CSV classified_metadata file of that image folder.

    Returns: None

    Result:
        Images in the directory defined in "usr_input_dir" variable will be sorted (by copying) into their according
        categorical folders.

    """

    usr_input_dir = input("Enter the absolute path of the directory that you want to sort the images by `classified "
                          "classes` (end with `/`): ")

    usr_input_csv = input("Enter the absolute path of the '*_Meta.csv' file of the above directory (end with '.csv'): ")

    sorted_input = input("Would you like the sorted images to be saved in a separate `*_Sorted` directory, located at "
                         "the same level as the original images' directory (answer with 'Y' or 'N')? ")

    old_path = []  # Old - full original paths of where the image files are currently stored
    parent_path = []  # First half of the o_path (parent path) without the image name
    parent_path_sorted = []

    ext = ('rgb', 'gif', 'jpeg', 'jpg', 'png', 'JPG')

    for root, dirs, files in os.walk(usr_input_dir):
        for fname in files:
            if fname.endswith(ext):
                org_path = os.path.join(root, fname)
                org_path = os.path.normpath(org_path)
                old_path.append(org_path)

                p_path = os.path.split(org_path)[0]
                p_path = os.path.normpath(p_path)
                parent_path.append(p_path)

    csv_file = pd.read_csv(usr_input_csv)
    df_csv = pd.DataFrame(csv_file)

    classified_folder = []  # Classified categories of each image

    list_numbbs = df_csv['Number of BBs'].tolist()
    list_predcategory = df_csv['Predicted Category'].tolist()

    for num_bbs, category in zip(list_numbbs, list_predcategory):
        if num_bbs > 1:
            checking = all(element == category[0] for element in category)
            if (checking):
                print("Same category for all bounding boxes")
            else:
                predclass = 'Assitant Required'
        else:
            if '0' in category:
                predclass = 'Empty'
            elif '1' in category:
                predclass = 'Animal'
            elif '2' in category:
                predclass = 'Person'
            elif '3' in category:
                predclass = 'Vehicle'
            else:
                predclass = None
        classified_folder.append(predclass)

    new_path = []  # New - new path where the image files will be move to
    new_path_sorted = []

    for i in parent_path:
        new_parent_path = i + '_Sorted'
        parent_path_sorted.append(new_parent_path)

    if sorted_input == 'Y':
        for ps, ss in zip(parent_path_sorted, classified_folder):
            new_img_path_sorted = os.path.join(ps, ss)
            new_img_path_sorted = os.path.normpath(new_img_path_sorted)
            os.makedirs(new_img_path_sorted, exist_ok=True) if not os.path.exists(new_img_path_sorted) else None
            new_path_sorted.append(new_img_path_sorted)

        # Make copy of the image and sorted them in categories
        for o, ns in zip(old_path, new_path_sorted):
            shutil.copy(o, ns)

    elif sorted_input == 'N':
        for p, s in zip(parent_path, classified_folder):
            new_img_path = os.path.join(p, s)
            new_img_path = os.path.normpath(new_img_path)
            os.makedirs(new_img_path, exist_ok=True) if not os.path.exists(new_img_path) else None
            new_path.append(new_img_path)

        # Make copy of the image and sorted them in categories
        for o, n in zip(old_path, new_path):
            shutil.copy(o, n)

    else:
        print("\nWrong choice, please re-run the script and follow the instructions !!!"
              "\n")

    return print('Done!')


# if __name__ == '__main__':

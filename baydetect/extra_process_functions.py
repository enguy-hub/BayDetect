"""Extra function(s), not being used atm, but could be further develop and implemented"""
import cv2
import json
import numpy as np
import pandas as pd
import pathlib as Path

from ast import literal_eval


# ID: pf_extra_1 || md_json_converter()
def md_json_converter():
    '''
    This function converts the output JSON file from MegaDetector batch processing to a new JSON file. This new JSON
    file sorts each image JSON objects into their according "Location", "Station", "Session", and "Predicted Category".
    The sorting is done primarily based on the storing location path of each image in the output JSON file from
    MegaDetector batch processing".

    When execute the function, it will first prompt the user to enter the absolute path of the output JSON file from
    MegaDetector batch processing. Then it will ask the user to give a name and an absolute path for the new JSON file.

    Parameters:
        usr_input_json (str): the absolute path of the output JSON file from MegaDetector batch processing
        (end with '.json')

        usr_output_json (str): the absolute path (end with .json) of where the new JSON file will be saved, if
        no path is given, the new JSON file will be saved at the same directory as where this script is stored.

    Returns:

    Output:
        JSON file saved at where user defined in the "usr_output_json" prompt
    '''

    usr_input_json = input("Enter the absolute path of the '*_MegaDetected.json' (end with '.json'): ")

    usr_output_json = input("Give a name and absolute path of where the new '*_MegaDetected_Organized.json' file will "
                            "be saved (end with '.json'): ")

    with open(usr_input_json, 'r') as file:
        json_info = json.load(file)

    final_dict = {}
    results = []

    for i in range(len(list(json_info['image']))):
        json_dict = {'Path': list(json_info['image'][i].values())[0],
                     'Location': list(json_info['image'][i].values())[0].split('/')[6],
                     'Station': list(json_info['image'][i].values())[0].split('/')[8],
                     'Session': list(json_info['image'][i].values())[0].split('/')[9]}

        detection_box = list(json_info['image'][i].values())[2]
        bb_numbers = len(detection_box)

        if bb_numbers != 0:
            json_dict['Predicted Category'] = list(detection_box[0].values())[0]
        else:
            json_dict['Predicted Category'] = 'Empty'

        print(json_dict)

        results.append(json_dict)
        print(results)

    final_dict['ImageFiles'] = results

    with open(usr_output_json, 'w') as file:
        json.dump(final_dict, file, indent=2)

    return None


# ID: pf_extra_2_supp || Supporting function for cropper_json_extractor()
def cropper_json_extractor(json_path):
    '''
    This function takes the output JSON file from the MegaDetector batch process as input and creates a dataframe
    based on the information provided in the JSON file.

    Parameters:
        json_path (str): the path of the json file

    Returns:
        df_json: a dataframe containing the information provided in the json file
    '''

    with open(json_path) as f:
        json_info = json.load(f)
    df_json = pd.DataFrame()

    for i in range(len(list(json_info['images']))):
        x = list(json_info['images'][i].values())[2]
        bb_numbers = len(x)
        image_name = list(json_info['images'][i].values())[0].split('/')[11]
        #        actual_category = list(json_info['images'][i].values())[0].split('\\')[0].split('/')[2]
        pred_category, confidence, bb_locations = None, None, None

        if bb_numbers != 0:
            pred_category, confidence, bb_locations = [], [], []
            for j in range(bb_numbers):
                pred_category.append(list(x[j].values())[0])
                confidence.append(list(x[j].values())[1])
                bb_locations.append(list(x[j].values())[2])

        data = image_name, str(bb_numbers), pred_category, confidence, bb_locations
        data = [list(data)]
        df_single = pd.DataFrame(data, columns=['Image Name', 'Number of BBs', 'Predicted Categories',
                                                'Confidence', 'Location of BBs'])
        df_json = pd.concat([df_json, df_single])

    return df_json


# ID: pf_extra_2 || cropper_metadata_creator()
def cropper_metadata_creator():
    '''
    This function takes the directories to the original image and the MegaDetector output JSON file as input, and
    creates a dataframe by calling json_extractor() and update the "Image Path" column with the rightful paths for the
    image. The updated dataframe will then be saved in a CSV classified_metadata file (usr_output_csv)

    Parameters:
        usr_input_orgdir (str): the path of the image folder
        usr_input_json (str): the path of the JSON file
        usr_output_csv (str): the path and name of the CSV classified_metadata file

    Returns:
        df_json: a dataframe containing the information provided in the JSON file

    '''

    usr_input_orgdir = input("Enter the absolute path of the directory which contains the images that you would like to"
                             " perform the cropping on (end with '/'): ")

    usr_input_json = input("Enter the absolute path of where the '*_MegaDetected.json' of the above directory is stored"
                           " (end with '.json'): ")

    usr_output_csv = input("Give a name and absolute path of where the '*_MetaCropping.csv' file will be saved at "
                           "(end with '.csv'): ")

    save_output = False

    df = cropper_json_extractor(usr_input_json)
    df["Image Path"] = np.nan
    # To save the path to each image, I added a new column called 'Image Path' to this merged dataframe.

    for i in df.index:
        image_path = usr_input_orgdir + df['Image Name'][i]

    df['Image Path'] = image_path

    if save_output:
        df.to_csv(usr_output_csv)

    return df, print('Done!')


# ID: pf_extra_3 || cropper()
def cropper():
    """
    This function takes the megadetected image (e.g., original_images) and its CSV classified_metadata file as input.
    The cropping of the image are based on the bounding box information provided in the CSV classified_metadata file.
    The user can save the cropped image on the disk.

    Parameters:
        usr_input_path(str): The path of megadetected image.
        usr_output_path(str): The path for saving the cropped image.
        save_image(bool): Should the cropped image be saved on the disk? => True
        usr_input_csv(str): The path of the CSV classified_metadata file

    Returns:
        List of NumPy arrays representing the cropped image.
        The cropped image can be saved on disk in the output_path.
    """

    usr_input_path = input("Enter the absolute path of the image that you would like to perform the cropping on "
                           "(end with '/'): ")

    usr_output_path = input("Enter the absolute path of where you would like the cropped image to be saved "
                            "(end with '/'): ")

    usr_input_csv = input("Enter the absolute path of where the '*_MetaCropped.csv' file is located in "
                          "(end with '.csv'): ")

    save_image = True

    df = pd.read_csv(usr_input_csv)
    cropped_list = []

    for i, j in enumerate(df['Image Name']):
        if df['Number of BBs'][i] != 0:
            image_path = usr_input_path + j
            category = df["Predicted Categories"][i]
            bb_numbers = df['Number of BBs'][i]
            bb_locations = df['Location of BBs'][i]
            image_name = j.split(".")[0]
            img = cv2.imread(image_path)
            x_scale, y_scale = img.shape[0], img.shape[1]

            if save_image:
                Path(usr_output_path).mkdir(parents=True, exist_ok=True)
            # k = 0

            for k in range(bb_numbers):
                location = literal_eval(bb_locations)[k]
                pred_category = literal_eval(category)[k]
                y = int(y_scale * location[0])
                x = int(x_scale * location[1])
                h = int(y_scale * location[2])
                w = int(x_scale * location[3])
                crop_img = img[x:x + w, y:y + h]
                cropped_list.append(crop_img)

                if save_image:
                    cv2.imwrite(usr_output_path + pred_category + image_name + str(k + 1) + '.jpg', crop_img)
                cv2.waitKey(30)

    return cropped_list


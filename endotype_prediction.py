import numpy as np
import pandas as pd
import pickle
import argparse
import logging
from time import sleep


parser = argparse.ArgumentParser()
parser.add_argument('-f', "--file",
                    default='data/example_df.csv', 
                    type=str,
                    help='csv file including 77 variables for endotype prediction')
parser.add_argument('-o', "--output",
                    default='output/output.csv', 
                    type=str,
                    help='csv file including 77 variables for endotype prediction')
args = parser.parse_args()
column_name = [
        'Gender, 0: male 1: female', 
        'Hypertension, 0: no 1: yes', 
        'Diabetes, 0: no 1: yes', 
        'smoke, 0: nenver or ex 1: current', 
        'Age, yrs',
        'SBP, mmHg', 'DBP, mmHg', 
        'BMI, kg/m2', 'Waist-hip ratio', 
        'Hb, dg/L', 
        'Total_cholesterol mmol/L','LDL Cholesterol, mmol/L', 'HDL Cholesterol, mmol/L', 'Triglycerides, mmol/L',
        'Glucose, mmol/L', 'C reactive Protein, mg/L', 
        'eGFR',
        'AGRP', 
        'CCL3','CD40L', 'CHI3L1', 'CSTB', 'CTSD', 'CTSL1', 'CXCL1', 'CXCL16', 
        'Dkk1',
        'FABP4', 'FAS', 'FGF23', 'FS', 
        'GDF15', 'GH', 'Gal3',
        'HBEGF', 'HSP27',
        'IL16', 'IL18', 'IL1ra', 'IL27A', 'IL6', 'IL6RA', 
        'KLK6',
        'LEP', 'LOX1', 
        'MB', 'MCP1', 'MMP12', 'MMP3', 'MMP7', 'MPO', 
        'NTproBNP', 
        'OPG', 
        'PAPPA', 'PAR1', 'PDGFSubunitB', 'PECAM1', 'PSGL1', 'PTX3', 'PGF',
        'RAGE', 'REN', 'RETN', 
        'SCF', 'SELE', 'SPON1', 'SRC','ST2', 
        'TF', 'TIE2', 'TM', 'TNFR1', 'TNFR2', 'tPA', 'TRAILR2', 
        'UPAR',
        'VEGFD'
       ]

if __name__ == "__main__":


    logging.basicConfig(format='%(asctime)s | %(levelname)s: %(message)s', level=logging.NOTSET)
    logging.info("You are using ASCVD endotype prediction tool, the program will start within 3 s")
    
    sleep(3)
    file_sr = pd.Series(args.file)
    logging.info("Reading input file from " + file_sr.to_string())
    Model = pickle.load(open('model_list/endotype_prediction_model.sav', 'rb'))
    check_csv = file_sr.str.contains(pat = '.csv')

    
    logging.info("Checking input data set format, require csv file with sep of comma")
    if not check_csv.bool():
        logging.error("Your input is not csv file, please format the input as csv file and use the programme again")
        exit()
    
    pred_df = pd.read_csv(args.file)
    print(pred_df)
    
    for index, var_name in enumerate(column_name):
        logging.info(str(index+1)+": required "+var_name +" "*10+ "[" + pred_df.columns[index] + "] is your input variable")
    logging.info("Please check the order and unit of variables list")
    confirrm_col_order = input("confirm (Input yes to continue, others to quit the programme): ")
    if confirrm_col_order=="yes":
            print(pred_df)
            logging.info("Confirm the value of your input dataset, the program will start within 5s, crtl + c to quit")
            sleep(5)
            logging.info("Starting endotype prediction")
            pred_endotype_list = Model.predict(pred_df.to_numpy())
            pred_df['pred_endotyoe'] = pred_endotype_list + 1
            pred_df.to_csv(args.output,index=False)
            
            endotype_array, count_array = np.unique(pred_df['pred_endotyoe'],return_counts=True)
            print("*"*20+"Frequency Table"+"*"*20)
            print("Endotype",":","count")
            for endotype_ind, count in zip(endotype_array,count_array):
                print(endotype_ind,":",count)
            logging.info("Endotype prediction finished, please check the " + args.output)
    else:
        logging.error("Stop endotype prediction by user(s)")
        exit()

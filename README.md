# Subclinical_athero_endotype
Subclinical atherosclerosis endotype prediction
The predicition model will be released and public avaliable for the academic purpose.

## Conda installation and enviroment set-up
Please check the following link for conda installation> https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

After conda installation, please search the "endotype_pred.yml" in the folder of env for enviroment set/up, with the following script in terminal>
```
conda create env --file env/endotype_pred.yml
```

## data preparation for endotype prediction in your cohort
Please organize your data with the following order (by columns):
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
(Unfinished)
Save the dataset as csv file, with sep of ",".

## endotype prediction


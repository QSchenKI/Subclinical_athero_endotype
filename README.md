# Atherosclerosis Subclinical Endotype Prediction (ASep)

## Background

This is the software for subclinical carotid atherosclerosis endotype prediction.

## Before using

We much appreciate it if you could cite the paper when using the tool.

Please note that the Endotype Prediction Tool is exclusively intended for academic purposes and is publicly available for non-profit educational, research, and academic use. Any commercial usage or inquiries regarding commercial licensing should be directed to Bruna Gigante (bruna.gigante@ki.se) and Qiaosen Chen (chen.qiaosen@ki.se). 

For any questions or bug reports during usage, please contact chen.qiaosen@ki.se.

The prediction tool was developed by Qiao Sen, Chen and tested by Otto Bergman. The development and testing environment is Linux but theoretically, it also applies to MacOS or Windows.

## Before set-up
./ refers to the current directory (Subclinical_athero_endotype/).

./path refers to the sub-directory within the Subclinical_athero_endotype/
The author suggests to set-up a virtual environment for endotype prediction so that your regular working environment won't be impacted by the dependency package.

In this README file of text, ./ will be intentionally presented to specify the directory. For sure you can take it away when you are using the model.

The model has no requirement of the nomenclature for variables in the current version, but the model will ask the user to check whether the variables input match what it expects.

## Conda installation and enviroment set-up
Please check the following link to install conda https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

After conda installation, please search the "endotype_pred.yml" in the folder of ./env for environment set-up, with the following script in the terminal:
```
conda create env --file ./env/endotype_pred.yml
```

## Data preparation for endotype prediction in your cohort
Please organize your data in the following order (by columns):

| Variable                | Description                             |
|:------------------------|:----------------------------------------|
| Gender                  | 0: male, 1: female                      |
| Hypertension            | 0: no, 1: yes                           |
| Diabetes                | 0: no, 1: yes                           |
| Smoke                   | 0: never or ex, 1: current              |
| Age                     | years                                   |
| SBP                     | mmHg                                    |
| DBP                     | mmHg                                    |
| BMI                     | kg/m²                                   |
| Waist-hip ratio         |                                         |                                                                |
| Hb                      | dg/L                                    |
| Total Cholesterol       | mmol/L                                  |
| LDL Cholesterol         | mmol/L                                  |
| HDL Cholesterol         | mmol/L                                  |
| Triglycerides           | mmol/L                                  |
| Glucose                 | mmol/L                                  |
| C-reactive Protein      | mg/L                                    |
| estimated glomerular filtration rate| cockcroft and gault formula |
| AGRP                    |                                         |
| CCL3                    |                                         |
| CD40L                   |                                         |
| CHI3L1                  |                                         |
| CSTB                    |                                         |
| CTSD                    |                                         |
| CTSL1                   |                                         |
| CXCL1                   |                                         |
| CXCL16                  |                                         |
| Dkk1                    |                                         |
| FABP4                   |                                         |
| FAS                     |                                         |
| FGF23                   |                                         |
| FS                      |                                         |
| GDF15                   |                                         |
| GH                      |                                         |
| Gal3                    |                                         |
| HBEGF                   |                                         |
| HSP27                   |                                         |
| IL16                    |                                         |
| IL18                    |                                         |
| IL1ra                   |                                         |
| IL27A                   |                                         |
| IL6                     |                                         |
| IL6RA                   |                                         |
| KLK6                    |                                         |
| LEP                     |                                         |
| LOX1                    |                                         |
| MB                      |                                         |
| MCP1                    |                                         |
| MMP12                   |                                         |
| MMP3                    |                                         |
| MMP7                    |                                         |
| MPO                     |                                         |
| NTproBNP                |                                         |
| OPG                     |                                         |
| PAPPA                   |                                         |
| PAR1                    |                                         |
| PDGFSubunitB            |                                         |
| PECAM1                  |                                         |
| PSGL1                   |                                         |
| PTX3                    |                                         |
| PGF                     |                                         |
| RAGE                    |                                         |
| REN                     |                                         |
| RETN                    |                                         |
| SCF                     |                                         |
| SELE                    |                                         |
| SPON1                   |                                         |
| SRC                     |                                         |
| ST2                     |                                         |
| TF                      |                                         |
| TIE2                    |                                         |
| TM                      |                                         |
| TNFR1                   |                                         |
| TNFR2                   |                                         |
| tPA                     |                                         |
| TRAILR2                 |                                         |
| UPAR                    |                                         |
| VEGFD                   |                                         |

For the OLINK protein, please use the Z-scores in your own cohort.
Save the dataset as csv file, with sep of ",".
## Activate endotype_pred environment
```
conda activate endotype_pred
```
After running this command, you will expect that (endotype_pred) shown in your terminal if everything goes well.

## Endotype prediction
Supposed we save the data for prediction in the folder of ./data, then the endotype can be predicted as follow
```
python endotype_pred.py --file ./data/exmaple_data.csv --output ./output.csv
```
After running this command, the file output.csv will include a new column of pred_endotype indicating the predicted endotype in your cohort.
You can specify the directory of the input file by --file or -f, and specify the output file directory and name by --output or -o

## Deactivate endotype_pred environment
```
conda deactivate
```
The command brings you back to your original base environment and now you can proceed with your other projects without influence by the endotype_pred environment.


# Subclinical carotid atheroclerosis endotype prediction
The predicition model will be released and public avaliable for the academic purpose.

The model was tested in Linux environments only but theoretically, it also applies to MacOS or Windows.

## Conda installation and enviroment set-up
Please check the following link to install conda https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html

After conda installation, please search the "endotype_pred.yml" in the folder of env for environment set/up, with the following script in the terminal:
```
conda create env --file env/endotype_pred.yml
```

## data preparation for endotype prediction in your cohort
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
| Waist-hip ratio         |     78                                                                                                  |
| Hb                      | dg/L                                    |
| Total Cholesterol       | mmol/L                                  |
| LDL Cholesterol         | mmol/L                                  |
| HDL Cholesterol         | mmol/L                                  |
| Triglycerides           | mmol/L                                  |
| Glucose                 | mmol/L                                  |
| C-reactive Protein      | mg/L                                    |
| eGFR                    |                                         |
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
Supposed we save the data for prediction in the folder of data, then the endotype can be predicted as follow
```
python endotype_pred.py --file data/exmaple_data.csv --output output.csv
```
After running this command, the file output.csv will include a new column of pred_endotype indicating the predicted endotype in your cohort.
You can specify the directory of the input file by --file or -f, and specify the output file directory and name by --output or -o

## Deactivate endotype_pred environment
```
conda deactivate
```
The command brings you back to your original base environment and now you can proceed with your other projects without influence by the endotype_pred environment.


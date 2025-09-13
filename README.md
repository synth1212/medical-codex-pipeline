<h1 align="center">
    HHA 507 Data Science Health Informatics<br>
    Fall 2025<br>
    </h1>
<!-- h1 = Heading 1; br = line break while keep alignment-->

## Purpose
This assignment simulates actual work data engineer or data scientist perform in healthcare technology. Companies like Epic, Cerner, or health insurance providers maintain exactly these types of data pipelines to ensure their systems have current medical coding standards.

The skills developed:

* Healthcare data domain knowledge
* ETL pipeline development
* Data quality validation
* File format optimization
* Production-ready code practices

## Instructions
Create Python scripts that can process each medical codex listed below into standardized CSV format. Each pipeline should handle data cleaning, validation, and format conversion for production use.
    <p style="margin-left:40px">
        1. **SNOMED CT (US)** - Clinical terminology<br>
        2. **ICD-10-CM (US)** - Diagnosis codes<br>
        3. **ICD-10 (WHO)** - International diagnosis codes<br>
        4. **HCPCS (US)** - Healthcare procedure codes<br>
        5. **LOINC (US)** - Laboratory test codes<br>
        6. **RxNorm (US)** - Medication codes<br>
        7. **NPI (US)** - Healthcare provider identifiers<br>
        </p>


## Medical Codexes Raw File Download Links
* Snowmed (US)
    - https://www.nlm.nih.gov/healthit/snomedct/archive.html
* ICD-10-CM (US)
    -  https://www.cms.gov/medicare/coding-billing/icd-10-codes 
* ICD-10 (WHO)
    - https://icdcdn.who.int/icd10/index.html 
* HCPCS (US)
    - https://www.cms.gov/medicare/coding-billing/healthcare-common-procedure-system/quarterly-update 
* LOINC (US)
    - https://loinc.org/downloads/ 
* RxNorm (US)
    - https://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html 
* NPI (US) 
    - https://download.cms.gov/nppes/NPI_Files.html 

## Repository Setup
1. Create a **public** GitHub repository named `medical-codex-pipeline`
2. Structure:
   ```
   medical-codex-pipeline/
   ├── input/
   ├── scripts/
   │   ├── snomed_processor.py
   │   ├── icd10cm_processor.py
   │   ├── icd10who_processor.py
   │   ├── hcpcs_processor.py
   │   ├── loinc_processor.py
   │   ├── rxnorm_processor.py
   │   └── npi_processor.py
   ├── output/
   │   ├── csv/
   ├── utils/
   │   └── common_functions.py
   ├── requirements.txt
   └── README.md
   ```

3. **Important**: Create `.gitignore` to exclude raw data files:
    ```gitignore
    # Raw data files (exclude from repo)
    inputs/
    *.txt
    *.xml
    *.zip
    raw_downloads/

    # Processed files are OK to commit
    # output/ - keep these

    # Python
    __pycache__/
    *.pyc
    .env
    venv/

    # IDE
    .vscode/
    .idea/

    # ignore any import dataset under any scripts/folder
    **/inputs/**/*.csv
    **/inputs/**/*.xlsx
    **/inputs/**/*.xml
    **/inputs/**/*.txt
    **/inputs/**/*.zip

    # but keep small outputs you generate
    !**/outputs/*.csv
    ```
    **<h4>Understanding .gitignore**</h4>
        <p>The ```.gitignore``` file is essential for this assignment beuase it tells Git which files to ignore and when uploading into GitHub. This is important when it comes to:
            <ul style="margin-left:20px">
                <li>Working with Large Data Sets</li>
                <li>Licensing/Contracting Concerns</li>
                <li>Overall Performance Level of the Repository</li>
            </ul>
        </p>
4. Create `requirement` text file to list all of the Python packages use in this assignment
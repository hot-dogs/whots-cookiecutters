# Installation

1. Create a virtual environment using `conda` and Install all packages
   if you haven't installed it yet. Otherwise, skip to the next section:
   ```bash
   conda create --prefix ./.env python=3.10 sphinx-book-theme=0.2.0 sphinx-design=0.0.13 sphinx-autodoc-typehints=1.12.0 sphinx=4.4.0 sphinx-autobuild=2021.3.14 sphinxcontrib-bibtex=2.5.0 myst-parser=0.17.0 ipython=8.1.1 nbsphinx=0.8.8 cookiecutter=2.1.1 -c conda-forge
   ```

# How to create a new WHOTS Data Report template? `FOR STAFF ONLY`

## 1. Use `tropac` or install `miniconda+git` on your own account

1. Connect to `helu` as `tropac`

## 2. Activate Conda Environment

1. Navigate to:

   ```shell
   cd /home/helu/science/WHOTS/whots-mono-reports/
   ```

2. Start a `bash` terminal

   ```shell
   bash
   ```

3. Activate `whots-data-report` Environment

   ```shell
   conda activate whots-data-report

   #you should now see:
   #(whots-data-report) helu>
   ```

## 3. Create a report template by using whots-cookiecutter:

1. On your terminal, type:

   ```shell
   cookiecutter /home/helu/github/whots-cookiecutters/projects/whots-annual-report/
   ```

   - Then, follow shell instructions (`without the supporting links`):

     ```shell
     # THIS IS AN EXAMPLE FOR WHOTS-16:

     current_whots_deployment_number [xx]: 16
     current_whots_deployment_date [DD Month YYYY]: 06 October 2019
     current_whots_deployment_time [HH:MM]: 02:12
     current_whots_recovery_date [DD Month YYYY]: 28 August 2021
     current_whots_recovery_time [HH:MM]: 17:52
     current_whots_deployment_station [Station #]: 52
     current_whots_deployment_anchor_position_latitude [xx xx.xx'N]: 22 40.096'N
     current_whots_deployment_anchor_position_longitude [xxx xx.xx'W]: 157 56.788'W
     current_whots_deployment_anchor_water_depth [xxxx]: 4753
     current_whots_cruise_start_date [DD Month YYYY]: 04 October 2019
     current_whots_cruise_end_date [DD Month YYYY]: 12 October 2019
     Select current_whots_ship:
     1 - Kilo-Moana
     2 - Oscar Elton Settle
     Choose from 1, 2 [1]: 2
     Select current_whots_chief_scientist:
     1 - Albert J Plueddemann
     Choose from 1 [1]: 1
     previous_whots_deployment [15]:
     previous_whots_recovery_date [DD Month YYYY]: 08 October 2019
     previous_whots_deployment_station [Station # ]: 50
     next_whots_deployment [17]:
     next_whots_deployment_date [DD Month YYYY]: 26 August 2021
     next_whots_deployment_time [HH:MM]: 03:13
     next_whots_recovery_date [DD Month YYYY]: 25 July 2022
     next_whots_recovery_time [HH:MM]: 18:03
     next_whots_deployment_station [Station # ]: 50
     next_whots_deployment_anchor_position_latitude [xx xx.xx'N]: 26 46.042'N
     next_whots_deployment_anchor_position_longitude [xxx xx.xx'W]: 157 53.796'W
     next_whots_cruise_start_date [DD Month YYYY]: 24 August 2021
     next_whots_cruise_end_date [DD Month YYYY]: 01 September 2021
     creator [Your Name]: Fernando Carvalho Pacheco
     created_on [2022-11-09]:
     ```

## 4. Build a sphinx project for the new whots data report

1. Navigate to:

   ```shell
   cd /home/helu/science/whots/whots-mono-reports/whots{{cookiecutter.current_whots_deployment_number}}-data-report/docs
   ```

2. Run the following:

   ```shell
   sphinx-autobuild -b html ../docs/source/ build/html
   ```

3. Check/Open the new WHOTS Data Report :
   - If you are using `tropac` on helu, do the following:
     1. Open a new terminal (shell)
     2. Connect to `helu` as `tropac`
     3. Type the following command on the terminal
        ```shell
        xdg-open http://127.0.0.1:8000
        ```
   - If you are on your own machine with your own terminal, just open the
     link:
     ```shell
     http://127.0.0.1:8000
     ```

## 5. Create a GitHub repository

1. Open your browser and navigate to:

   [hot-dogs](https://github.com/organizations/hot-dogs/repositories/new)

2. Under `Repository name`, type the whots{{cookiecutter.current_whots_deployment_number}}-data-report).
3. Under `Description (optional)`, type WHOTS-{{cookiecutter.current_whots_deployment_number}} Data Report.
4. Select `Public`, so anyone on the internet can see this repository.
5. DON'T check `[] Add a README file`,`[] Add .gitignore` , `[] Choose a license`.
6. Click on `Create repository`.

## 6. Push your local project to your new GitHub repository

1. On `helu` (local machine), navigate to:

   ```shell
   cd /home/helu/science/whots/whots-mono-reports/whots{{cookiecutter.current_whots_deployment_number}}-data-report/docs
   ```

2. `Start` git, add folders/files and commit changes:

   ```shell
   git init
   git add --all
   git commit -S -am 'started whots-{{cookiecutter.current_whots_deployment_number}} repo'
   ```

3. Tell your `local repository` to follow the new GitHub repository:

   ```shell
   git remote add origin git@github.com:hot-dogs/whots{{cookiecutter.current_whots_deployment_number}}-data-report.git
   ```

4. `Push` your local repo to GitHub:

   ```shell
   git push -u origin main
   ```

## 7. Import your WHOTS Data Report to Readthedocs website.

1. On your browser, navigate to:

   [readthedocs](https://readthedocs.org/dashboard/import/?)

2. Sign in using GitHub (`hotdata` account)
3. Click on `hotdata` (top right of the page), then on `Import a Project`.
4. Refresh the list of repositories.
5. Select the `hot-dogs/whots{{cookiecutter.current_whots_deployment_number}}-data-report`.
6. Under `Project Details`, the default details are ok!, just click `Next`.
7. Finally, click on `Build Version`. --> This will take some time to finish.

# Zenodo

Zenodo is a research data repository that allows users to share and archive
their scientific and academic work, including datasets, software, and
publications. Zenodo provides a public API that allows developers to interact
with the platform programmatically. The API is based on the RESTful
architecture and uses standard HTTP methods to access and manipulate resources.

1. **Register for a Zenodo account:**

Before you can use the Zenodo API, you'll need to sign up for a Zenodo account
if you haven't already. Go to the Zenodo website (https://zenodo.org/) and
click on the "Sign In" or "Register" button.

2. **Create a personal access token:**
   To interact with the Zenodo API, you'll need an access token that will
   authenticate your requests. After logging into your Zenodo account, go to the
   "Applications" section in your account settings and create a new personal
   access token. Make sure to keep this token secure, as it grants access to your
   Zenodo account.

3. **API Endpoints and Documentation:**
   Zenodo's API documentation provides information about the available endpoints
   and how to use them. The official API documentation can be found at:
   [https://developers.zenodo.org/]

4. **Authorization:**
   To use the Zenodo API, you'll need to include your access token in the request
   headers. Typically, you'll add an `Authorization` header with the value `Bearer
YOUR_ACCESS_TOKEN` to your API requests.

5. **API Requests:**
   The Zenodo API allows you to perform various actions, such as uploading files,
   creating new depositions (projects), publishing records, and more. Here's an
   example of how you can upload a file using the Zenodo API in Python using the
   `requests` library:

```bash
conda install requests
```

```python
import requests

# Your personal access token
access_token = "YOUR_ACCESS_TOKEN"

# Endpoint URL for creating a new deposition (project)
deposition_url = "https://zenodo.org/api/deposit/depositions"

headers = {
    "Authorization": f"Bearer {access_token}"
}

# Create a new deposition (project)
response = requests.post(deposition_url, headers=headers)

if response.status_code == 201:
    # The deposition was successfully created
    deposition_data = response.json()
    deposition_id = deposition_data["id"]
    print(f"Deposition ID: {deposition_id}")

    # Upload a file to the deposition
    file_url = f"https://zenodo.org/api/deposit/depositions/{deposition_id}/files"
    files = {"file": open("path/to/your/file.pdf", "rb")}
    response = requests.post(file_url, headers=headers, files=files)

    if response.status_code == 201:
        print("File uploaded successfully.")
    else:
        print("File upload failed.")
else:
    print("Failed to create a new deposition.")
```

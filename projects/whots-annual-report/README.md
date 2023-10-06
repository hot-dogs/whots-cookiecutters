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

import json
from datetime import datetime

import requests


# Function to get the current date in "yyyy-mm-dd" format
def get_formatted_date():
    current_date_time = datetime.now()
    return current_date_time.strftime("%Y-%m-%d")


# Function to create an empty upload and obtain the deposition_id
def create_empty_upload():
    deposition_url = "https://sandbox.zenodo.org/api/deposit/depositions"
    headers = {"Content-Type": "application/json"}

    params = {"access_token": ACCESS_TOKEN, "prereserve_doi": "true"}

    r = requests.post(deposition_url, params=params, json={}, headers=headers)

    deposition_id = r.json()["id"]
    doi = r.json()["metadata"]["prereserve_doi"]["doi"]
    bucket_url = r.json()["links"]["bucket"]

    return deposition_id, doi, bucket_url


# ADD metadata
def add_metadata(deposition_id, doi, formatted_date):
    headers = {"Content-Type": "application/json"}

    data = {
        "metadata": {
            "title": "Hydrographic Observations at the Woods Hole Oceanographic Institution Hawaii Ocean Time-Series Site (WHOTS):  2021 - 2022, Data Report #17",
            "In 2003, Robert Weller (Woods Hole Oceanographic Institution [WHOI]), Albert Plueddemann (WHOI),and Roger Lukas (the University of Hawaii [UH]) proposed to establish a long-term surface mooring at the Hawaii             Ocean Time-series (HOT) Station ALOHA (22°45’N, 158°W) to provide             sustained, high-quality air-sea fluxes and the associated upper             ocean response as a coordinated part of the HOT program, and as an             element of the global array of ocean reference stations supported             by the National Oceanic and Atmospheric Administration’s (NOAA)             Office of Climate Observation.               The WHOTS-17 mooring was deployed on August 26, 2021 (WHOTS-17 cruise) and was recovered on July 25, 2022 (WHOTS-18 cruise). The cruises were             aboard the R/V Oscar Elton Settle. The WHOTS-18 mooring was             deployed on July 24, 2022, during the WHOTS-18 cruise and was             recovered on June 19, 2023, during the WHOTS-19 cruise.              This report documents and describes the oceanographic observations made on the WHOTS-17 mooring for nearly eleven months and from shipboard measurements during the two cruises when the mooring was deployed and recovered. Sections II and III include a detailed description of the cruises and the mooring, respectively. Sampling and processing procedures of the hydrographic casts, thermosalinograph, and shipboard ADCP data collected during these cruises are described in Section IV. Section V includes the processing procedures for the data collected by the moored instruments: SeaCATs, MicroCATs, Moored ADCPs and VMCM. Plots of the resulting data and preliminary analysis are presented in Section VI.",
            "upload_type": "publication",
            "publication_type": "softwaredocumentation",
            "publication_date": formatted_date,
            "access_right": "open",
            "license": "CC-BY-4.0",
            "language": "eng",
            "keywords": [
                "WHOTS",
                "HOT",
                "Hawaii Ocean Time-series",
                "OceanSITES",
                "WHOTS Mooring",
                "WHOTS-17 Data Report",
                "Oceanography",
                "timeseries",
                "physical oceanography",
            ],
            "version": "0.0.1",
            "notes": "This publication is based upon observations from the WHOI-Hawaii Ocean Time-series Site (WHOTS) mooring, which is supported in part by the National Oceanic and Atmospheric Administration (NOAA) Global Ocean Monitoring and Observing (GOMO) Program through the Cooperative Institute for the North Atlantic Region (CINAR) under Cooperative Agreement NA14OAR4320158. NOAA CPO FundRef number 100007298 to the Woods Hole Oceanographic Institution, and by National Science Foundation grants OCE-0327513,OCE-0752606, OCE-0926766, OCE-1260164 and OCE-1756517 to the University of Hawaii for the Hawaii Ocean Time-series. This is SOEST contribution number xxxxxxxxx",
            "communities": [{"identifier": "hot"}],
            "grants": [
                {"id": "10.13039/100000001::0327513"},
                {"id": "10.13039/100000001::0752606"},
                {"id": "10.13039/100000001::0926766"},
                {"id": "10.13039/100000001::1260164"},
                {"id": "10.13039/100000001::1756517"},
            ],
            "locations": [
                {
                    "lat": "22.767367",
                    "place": "WHOTS-17",
                    "lon": "-157.896583",
                    "description": "Set: 26 August 2021 from R/V Oscar Elton Settle; Recovered: 25 July 2022, from R/V Oscar Elton Settle; Water depth: 4699m",
                }
            ],
            "related_identifiers": [
                {
                    "scheme": "url",
                    "identifier": "http://whots17-data-report.readthedocs.io/",
                    "relation": "isDocumentedBy",
                    "resource_type": "publication-softwaredocumentation",
                },
                {
                    "scheme": "url",
                    "identifier": "http://tds0.ifremer.fr/thredds/catalog/CORIOLIS-OCEANSITES-GDAC-OBS/DATA/WHOTS/catalog.html",
                    "relation": "isSupplementedBy",
                    "resource_type": "dataset",
                },
                {
                    "scheme": "url",
                    "identifier": "ftp://mananui.soest.hawaii.edu/pub/hot/whots/wh17",
                    "relation": "isSupplementedBy",
                    "resource_type": "dataset",
                },
                {
                    "scheme": "url",
                    "identifier": "ftp://mananui.soest.hawaii.edu/pub/hot/whots/whots_cruises/wh17_cruise",
                    "relation": "isSupplementedBy",
                    "resource_type": "dataset",
                },
                {
                    "scheme": "url",
                    "identifier": "ftp://mananui.soest.hawaii.edu/pub/hot/whots/whots_cruises/wh18_cruise",
                    "relation": "isSupplementedBy",
                    "resource_type": "dataset",
                },
                {
                    "scheme": "url",
                    "identifier": "https://whots17-data-report.readthedocs.io/_/downloads/en/latest/pdf/",
                    "relation": "isIdenticalTo",
                    "resource_type": "publication-report",
                },
                {
                    "scheme": "url",
                    "identifier": "http://www.soest.hawaii.edu/whots/WHOTS-17_datareport.pdf",
                    "relation": "isIdenticalTo",
                    "resource_type": "publication-report",
                },
            ],
            "creators": [
                {
                    "name": "Carvalho Pacheco, Fernando",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                    "orcid": "https://orcid.org/0000-0002-0376-5338",
                },
                {
                    "name": "Santiago-Mandujano, Fernando",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "name": "Potemra, James T.",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                    "orcid": "https://orcid.org/0000-0002-2515-6402",
                },
                {
                    "name": "Plueddemann, Albert J.",
                    "affiliation": " Woods Hole Oceanographic Institution - Woods Hole, MA",
                    "orcid": "https://orcid.org/0000-0003-0228-9795",
                },
                {
                    "name": "Weller, Robert A.",
                    "affiliation": " Woods Hole Oceanographic Institution - Woods Hole, MA",
                    "orcid": "https://orcid.org/0000-0001-8001-6886",
                },
                {
                    "name": "Fitzgerald, Daniel",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "name": "Galbraith, Nancy R.",
                    "affiliation": " Woods Hole Oceanographic Institution - Woods Hole, MA",
                },
            ],
            "contributors": [
                {
                    "type": "ProjectLeader",
                    "name": "Potemra, James T.",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                    "orcid": "https://orcid.org/0000-0002-2515-6402",
                },
                {
                    "type": "ProjectLeader",
                    "name": "Plueddemann, Albert J.",
                    "affiliation": " Woods Hole Oceanographic Institution - Woods Hole, MA",
                    "orcid": "https://orcid.org/0000-0003-0228-9795",
                },
                {
                    "type": "ProjectLeader",
                    "name": "Weller, Robert A.",
                    "affiliation": " Woods Hole Oceanographic Institution - Woods Hole, MA",
                    "orcid": "https://orcid.org/0000-0001-8001-6886",
                },
                {
                    "type": "DataManager",
                    "name": "Santiago-Mandujano, Fernando",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "type": "Editor",
                    "name": "Santiago-Mandujano, Fernando",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "type": "Researcher",
                    "name": "Hasbrouck, Emerson",
                    "affiliation": "Woods Hole Oceanographic Institution - Woods Hole, MA",
                },
                {
                    "type": "Researcher",
                    "name": "Maloney, Kelsey",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "type": "Other",
                    "name": "Harris, James",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "type": "Other",
                    "name": "Jackson, Caroline",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "type": "ResearchGroup",
                    "name": "Upper Ocean Processes Group (UOP)",
                    "affiliation": " Woods Hole Oceanographic Institution - Woods Hole, MA",
                },
                {
                    "type": "ResearchGroup",
                    "name": "Hawaii Ocean Time-series (HOT)",
                    "affiliation": " University of Hawaiʻi at Mānoa - UH Manoa",
                },
                {
                    "type": "HostingInstitution",
                    "name": " University of Hawaiʻi at Mānoa",
                },
                {
                    "type": "HostingInstitution",
                    "name": " Woods Hole Oceanographic Institution",
                },
                {
                    "type": "Sponsor",
                    "name": " Ocean Observing and Monitoring Division, Climate Program Office",
                },
                {
                    "type": "Sponsor",
                    "name": " National Oceanic and Atmospheric Administration",
                },
                {"type": "Sponsor", "name": " U.S. Department of Commerce"},
                {"type": "Sponsor", "name": " National Science Foundation"},
            ],
            "references": [
                "Plueddemann, A. J., Weller, R. A., Lukas, R., Lord, J., Bouchard,P. R., & M. Alexander Walsh. (2006). WHOI hawaii ocean timeseries station (WHOTS) : WHOTS-2 mooring turnaround cruise report. Woods Hole Oceanographic Institution. https://doi.org/10.1575/1912/1074",
                "Whelan, S. P., Weller, R. A., Lukas, R., Bradley, F., Lord, J., Smith, J. C., Bahr, F. B., Lethaby, P., & Snyder, J. (2007). WHOI hawaii ocean timeseries station (WHOTS) : WHOTS-3 mooring turnaround cruise report (p. 103). Woods Hole Oceanographic Institution. https://doi.org/10.1575/1912/1825",
                "Whelan, S. P., Plueddemann, A. J., Lukas, R., Lord, J., Lethaby, P., Smith, J. C., Bahr, F. B., Galbraith, N. R., & Sabine, C. L. (2008). WHOI hawaii ocean timeseries station (WHOTS): WHOTS-4 2007 mooring turnaround cruise report. Woods Hole Oceanographic Institution. https://doi.org/https://doi.org/10.1575/1912/2504",
                "Whelan, S. P., Santiago-Mandujano, F., Bradley, F., Plueddemann, A. J., Ludovic Barista, Ryder, J. R., Lukas, R., Lethaby, P., Snyder, J., Sabine, C. L., Stanitski, D., Rapp, A. D., Fairall, C. W., Pezoa, S., Galbraith, N. R., Lord, J., & Bahr, F. B. (2010). WHOI hawaii ocean timeseries station (WHOTS): WHOTS-6 2009 mooring turnaround cruise report. Woods Hole Oceanographic Institution. https://doi.org/https://doi.org/10.1575/1912/3458",
                "Santiago-Mandujano, F., Snyder, J., Natarov, S., Maloney, K., Howins, N., Hebert, G., & Lukas, R. (2019). UH contributions to WHOTS-15 cruise report. School of Ocean and Earth Science and Technology; University of Hawaii. http://www.soest.hawaii.edu/whots/proc_reports/WHOTS-15_CruiseRpt.pdf",
                "Hasbrouck, E., Weller, R., Santiago-Mandujano, F., Blomquist, B., Maloney, K., Snyder, J., Clabaugh, A., Adams, S., Rosburg, K., King, A., Natarov, S., Howins, N., Hebert, G., & Lukas, R. (2019). WHOI hawaii ocean timeseries station (WHOTS) : WHOTS-14 2017 mooring turnaround cruise report (p. 112). Woods Hole Oceanographic Institution. https://doi.org/10.1575/1912/25262",
                "Santiago-Mandujano, F., Fitzgerald, D., Maloney, K., Rohrer, T., Howins, N., Tabata, R., & Potemra, J. (2021). UH contributions to WHOTS-16 cruise report. School of Ocean and Earth Science and Technology, University of Hawaii. https://www.soest.hawaii.edu/whots/proc_reports/UH_Contributions_to_WHOTS16_Cruise_Report.pdf",
                "Santiago-Mandujano, F., Fitzgerald, D., Maloney, K., Rohrer, T., Howins, N., Tabata, R., & Potemra, J. (2022). UH contributions to WHOTS-17 cruise report. School of Ocean and Earth Science and Technology, University of Hawaii. http://www.soest.hawaii.edu/whots/proc_reports/UH%20Contributions%20to%20WHOTS17_Cruise_Report.pdf",
                "Santiago-Mandujano, F., Carvalho Pacheco, F., Fitzgerald, D., Maloney, K., Rohrer, T., Harris III, J., Howins, N., & Potemra, J. (2022). UH Contributions to WHOTS-18 Cruise Report. http://www.soest.hawaii.edu/whots/proc_reports/WHOTS18_Cruise_Report.pdf",
                "Hosom, D. S., Weller, R. A., Payne, R. E., & Prada, K. E. (1995). The IMET (improved meteorology) ship and buoy systems. Journal of Atmospheric and Oceanic Technology, 12(3), 527–540. https://doi.org/2.0.co;2>10.1175/1520-0426(1995)012<0527:timsab>2.0.co;2",
                "Keir Colbo, & Weller, R. A. (2009). Accuracy of the IMET sensor package in the subtropics. Journal of Atmospheric and Oceanic Technology, 26(9), 1867–1890. https://doi.org/10.1175/2009JTECHO667.1",
                "A. Birol Kara, Rochford, P. A., & Hurlburt, H. E. (2000). Mixed layer depth variability and barrier layer formation over the North Pacific Ocean. Journal of Geophysical Research: Oceans, 105(C7), 16783–16801. https://doi.org/10.1029/2000jc900071",
                "Santiago-Mandujano, F., Lethaby, P., Lukas, R., Snyder, J., Weller, R. A., Plueddemann, A. J., Lord, J., Whelan, S., Bouchard, P., & Galbraith, N. (2007). Hydrographic observations at the woods hole oceanographic institution (WHOI) hawaii ocean timeseries (HOT) site (WHOTS): 2004-2006. School of Ocean and Earth Science and Technology, University of Hawaii. http://uop.whoi.edu/currentprojects/WHOTS/docs/UH_Whots_data_report_1.pdf",
                "Tupas, L., Santiago-Mandujano, F., Hebel, D., Lukas, R., Karl, D., & Firing, E. (1993). Hawaii ocean time-series data report 4, 1992. In SOEST Technical Report 93-14 (p. 248). School of Ocean and Earth Science and Technology, University of Hawaii. https://hahana.soest.hawaii.edu/hot/reports/rep_y4.pdf",
                "Fukieki, L., Santiago-Mandujano, F., Pacheco, F. C., Potemra, J., & White, A. (2023). Hawaii Ocean Time-series Data Report 32: 2020. https://hahana.soest.hawaii.edu/hot/reports/rep_y32.pdf",
                "W. Brechner Owens, & Millard, R. C. (1985). A new algorithm for CTD oxygen calibration. Journal of Physical Oceanography, 15, 621–631. https://doi.org/2.0.CO;2>10.1175/1520-0485(1985)015<0621:ANAFCO>2.0.CO;2",
                "Tupas, L., Santiago-Mandujando, F., Hebel, D., Nosse, C., Fujieki, L., Firing, E., Lukas, R., Karl, D., Win, C., Bidigare, R., Landry, M., & Lopez, M. (1996). Hawaii ocean time-series data report 8, 1996 (pp. 1–286). School of Ocean and Earth Science and Technology, University of Hawaii. https://hahana.soest.hawaii.edu/hot/reports/rep_y8.pdf",
                "Howard Paul Freitag, McCarty, M. E., Nosse, C., Lukas, R., McPhaden, M. J., & Cronin, M. F. (1999). COARE Seacat data: Calibrations and quality control procedures. NOAA Technical Memorandum ERL PMEL-115. https://repository.library.noaa.gov/view/noaa/10999",
                "Firing, E. (1991). Acoustic Doppler current profiling measurements and navigation. WOCE Hydrographic Operations and Methods. WOCE Operations Manual, WHP Office Report WHPO 91-1, WOCE Report No. 68/91; WOCE Hydrographic Programme. https://www.nodc.noaa.gov/archive/arc0013/0001873/1.1/data/1-data/publications/WOCE/ADCP.pdf",
                "Teledyne RD Instruments. (2011). Acoustic doppler current profiler principles of operation a practical primer. In P/N 951-6069-00 (pp. 1–62). http://www.teledynemarine.com/Documents/Brand%20Support/RD%20INSTRUMENTS/Technical%20Resources/Manuals%20and%20Guides/General%20Interest/BBPRIME.pdf",
                "Lukas, R., Santiago-Mandujano, F., Bingham, F., & Mantyla, A. (2001). Cold bottom water events observed in the Hawaii Ocean Time-series: implications for vertical mixing. Deep Sea Research Part I: Oceanographic Research Papers, 48(4), 995–1021. https://doi.org/https://doi.org/10.1016/S0967-0637(00)00078-9",
                "Howe, b. m., lukas, r., duennebier, f., & karl, d. (2011). aloha cabled observatory installation. 1–11. https://doi.org/10.23919/oceans.2011.6107301",
            ],
        }
    }

    # r = requests.put(
    #     "https://sandbox.zenodo.org/api/deposit/depositions/%s" % deposition_id,
    #     params={"access_token": ACCESS_TOKEN},
    #     data=json.dumps(data),
    #     headers=headers,
    # )
    #
    # r.status_code

    url = f"https://sandbox.zenodo.org/api/deposit/depositions/{deposition_id}"
    r = requests.put(
        url,
        params={"access_token": ACCESS_TOKEN},
        data=json.dumps(data),
        headers=headers,
    )

    return r.status_code


# Function to upload a file to the bucket


def upload_file_to_bucket(bucket_url, filename, params):
    path = f"/Users/fcp/Pictures/{filename}"

    with open(path, "rb") as fp:
        r = requests.put(
            f"{bucket_url}/{filename}",
            data=fp,
            params=params,
        )
    return r.status_code


# # PUBLISH:
# r = requests.post(
#     "https://sandbox.zenodo.org/api/deposit/depositions/%s/actions/publish"
#     % deposition_id,
#     params={"access_token": ACCESS_TOKEN},
# )
# r.status_code
# # 202


if __name__ == "__main__":
    ACCESS_TOKEN = "change_your_access_token_here"
    params = {"access_token": ACCESS_TOKEN}

    formatted_date = get_formatted_date()
    deposition_id, doi, bucket_url = create_empty_upload()
    status_code = add_metadata(deposition_id, doi, formatted_date)

    # Uncomment the line below to upload a file to the bucket
    # file_upload_status_code = upload_file_to_bucket(
    #     bucket_url, "addfilehereifnecessary.jpg", params)

    # Uncomment the line below to publish the deposition
    # publish_status_code = publish_deposition(deposition_id)

    print("prereserve_doi =", doi)
    print("Metadata status code:", status_code)
```

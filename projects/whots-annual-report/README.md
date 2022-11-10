# Installation 

1. Create a virtual environment using `conda` and Install all packages 
if you haven't installed it yet. Otherwise, skip to the next section:
   ```bash
   conda create --prefix ./.env python=3.10 sphinx-book-theme=0.2.0 sphinx-design=0.0.13 sphinx-autodoc-typehints=1.12.0 sphinx=4.4.0 sphinx-autobuild=2021.3.14 sphinxcontrib-bibtex=2.5.0 myst-parser=0.17.0 ipython=8.1.1 nbsphinx=0.8.8 cookiecutter=2.1.1 -c conda-forge 
   ```

#  How to create a new WHOTS Data Report template? `FOR STAFF ONLY`
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
   + Then, follow shell instructions:

      ```shell
      # This is an example for WHOTS-16:
      whots_deployment_number [20]: 16
      whots_previous_deployment [15]:
      whots_next_deployment [17]:
      Select whots_ship:
      1 - Kilo-Moana
      2 - Oscar Elton Settle
      Choose from 1, 2 [1]: 2
      Select whots_chief_scientist:
      1 - Albert J Plueddemann
      Choose from 1 [1]: 1
      whots_deployment_date [DD Month YYYY ]: 06 October 2019
      whots_recovery_date [DD Month YYYY]: 28 August 2021
      creator [Your Name]: Fernando Carvalho Pacheco
      created_on [2022-04-02]:
      ```

## 4. Build a sphinx project for the new whots data report

1. Navigate to:

    ```shell
    cd /Users/fcp/workspace/1.git/5.whots/whots-mono-reports/whots-16/docs
    ```

2. Run the following:

    ```shell
    sphinx-autobuild ../docs/source build/html
    ```

## 5. Create a GitHub repository

1. Open your browser and navigate to:

   [hot-dogs](https://github.com/organizations/hot-dogs/repositories/new)

2. Under `Repository name`, type the whotsxx-data-report, where xx is the whots deployment number (*eg*:
3. whots16-data-report).
4. Under `Description (optional)`, type WHOTS-XX Data Report.
5. Select `Public`, so anyone on the internet can see this repository.
6. DON'T check `[] Add a README file`,`[] Add .gitignore`, `[] Choose a license`.
7. Click on `Create repository`.

## 6. Push your local project to your new GitHub repository

1. On your local computer, navigate to:

   ```shell
   cd /Users/fcp/workspace/1.git/5.whots/whots-mono-reports/whots-16
   ```

2. Start git, add folders/files and commit changes:

   ```shell
   git init
   git add --all
   git commit -S -am 'started whots-16 repo'
   ```

3. Tell your local repository to follow the new GitHub repository:

   ```shell
   git remote add origin git@github.com:hot-dogs/whots16-data-report.git
   ```

4. Push your local repo to github:

   ```shell
   git push -u origin main
   ```

## 7. Import your WHOTS data report to readthedocs.

1. On your browser, navigate to:

   [readthedocs](https://readthedocs.org/dashboard/import/?)

2. Click on your projects, then on `Import a Project`.
3. Refresh the list of repositories.
4. Select the whotsxx-data-report.
5. Under `Project Details`, the default details are ok!, just click `Next`.
6. Finally, click on `Build Version`. --> This will take some time to finish.


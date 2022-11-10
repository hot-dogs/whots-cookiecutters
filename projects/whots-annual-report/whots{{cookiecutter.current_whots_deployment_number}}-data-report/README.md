#  Woods Hole - Hawaii Ocean Time-series Site
[<img src="https://github.com/hot-dogs/whots{{cookiecutter.current_whots_deployment_number}}-data-report/blob/main/docs/source/_static/_images/new_logo_HOT.png" height="200" />](https://hahana.soest.hawaii.edu/hot/)


[![Documentation Status](https://readthedocs.org/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/badge/?version=latest)](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/?badge=latest)
[![DOI](https://zenodo.org/badge/doi/xx.xxxx/zenodo.xxxxxx.svg)](https://doi.org/xx.xxxx/zenodo.xxxxxx)
[![CITATION.cff](https://github.com/hot-dogs/whots{{cookiecutter.current_whots_deployment_number}}-data-report/actions/workflows/cff-validator.yml/badge.svg?branch=main)](https://github.com/hot-dogs/whots{{cookiecutter.current_whots_deployment_number}}-data-report/actions/workflows/cff-validator.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](http://creativecommons.org/licenses/by/4.0/)


## Documentation 
[*Hydrographic observations at the Woods Hole Oceanographic Institution Hawaii
Ocean Time-Series Site (WHOTS): {{ (cookiecutter.current_whots_deployment_date|string)[-4:]}} - {{ (cookiecutter.current_whots_recovery_date|string)[-4:]}}, Data Report #{{cookiecutter.current_whots_deployment_number}}*](http://whots{{cookiecutter.current_whots_deployment_number}}-data-report.readthedocs.io/)

## Abstract

In 2003, [Robert Weller](https://www.whoi.edu/profile/rweller/) ([Woods Hole
Oceanographic Institution [WHOI]](https://www.whoi.edu))
, [Albert Plueddemann](https://www.whoi.edu/profile/aplueddemann/) 
([WHOI](https://www.whoi.edu)), and
[Roger Lukas](http://www.soest.hawaii.edu/oceanography/faculty/rlukas/)
([The University of Hawaii [UH]](https://manoa.hawaii.edu)) proposed to establish 
a [long-term surface mooring at the Hawaii Ocean Time-series (HOT)](http://www.soest.hawaii.edu/whots/)
[Station ALOHA (22°45’N, 158°W)](https://hahana.soest.hawaii.edu/stationaloha/)
to provide sustained, high-quality air-sea fluxes and the associated upper
ocean response as a coordinated part of the HOT program, and as an element of
the global array of ocean reference stations supported by the National Oceanic
and Atmospheric Administration’s (NOAA) Office of Climate Observation. 

The WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring was deployed on 
{{ (cookiecutter.current_whots_deployment_date|string)[3:-5]}} {{ (cookiecutter.current_whots_deployment_date|string)[1:2]}}, {{ (cookiecutter.current_whots_deployment_date|string)[-4:]}}
 ([WHOTS-{{cookiecutter.current_whots_deployment_number}} cruise](http://www.soest.hawaii.edu/whots/wh{{cookiecutter.current_whots_deployment_number}}_dep.html)) 
and was recovered on {{ (cookiecutter.current_whots_recovery_date|string)[3:-5]}} { (cookiecutter.current_whots_recovery_date|string)[1:2]}},  {{ (cookiecutter.current_whots_recovery_date|string)[-4:]}} 
([WHOTS-{{cookiecutter.next_whots_deployment}} cruise](http://www.soest.hawaii.edu/whots/wh{{cookiecutter.next_whots_deployment}}_dep.html)). 
The cruises were aboard the R/V {{cookiecutter.current_whots_ship}}. The WHOTS-{{cookiecutter.next_whots_deployment}} mooring was 
deployed on {{ (cookiecutter.next_whots_deployment_date|string)[3:-5]}}  {{ (cookiecutter.next_whots_deployment_date|string)[1:2]}}, {{ (cookiecutter.next_whots_deployment_date|string)[-4:]}}, during the 
[WHOTS-{{cookiecutter.next_whots_deployment}} cruise](http://www.soest.hawaii.edu/whots/wh{{cookiecutter.next_whots_deployment}}_dep.html) and was 
recovered on {{ (cookiecutter.next_whots_recovery_date|string)[3:-5]}} {{ (cookiecutter.next_whots_recovery_date|string)[1:2]}}, {{ (cookiecutter.next_whots_recovery_date|string)[-4:]}}. 

This report documents and describes the oceanographic observations made on the 
WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring for nearly one year and ten months and from shipboard measurements
during the two cruises when the mooring was deployed and recovered. 
[Sections II](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/2_section.html) 
and [III](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/3_section.html) 
include a detailed description of the cruises and the mooring, respectively. 
Sampling and processing procedures of the hydrographic casts, thermosalinograph, 
and shipboard ADCP data collected during these cruises are described in
[Section IV](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/4_section.html). 
[Section V](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/5_section.html) 
includes the processing procedures for the data collected by the moored 
instruments: SeaCATs, MicroCATs, Moored ADCPs and VMCM. Plots of the resulting 
data and preliminary analysis ar presented in [Section VI](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/6_section.html).


## Citing

- `APA`
```
Carvalho Pacheco, F., Santiago-Mandujano, F., Potemra, J. T., Plueddemann, A. J., Weller, R. A., Fitzgerald, D., & Galbraith, N. R. ({{ (cookiecutter.created_on|string)[:4]}}). Hydrographic Observations at the Woods Hole Oceanographic Institution Hawaii Ocean Time-Series Site (WHOTS): {{ (cookiecutter.current_whots_deployment_date|string)[-4:]}} - {{ (cookiecutter.current_whots_recovery_date|string)[-4:]}}, Data Report #{{cookiecutter.current_whots_deployment_number}}. School of Ocean and Earth Science and Technology (SOEST), Department of Oceanography, University of Hawai‘i at Mānoa, Honolulu, HI. https://doi.org/xx.xxx/zenodo.xxxxx
```

- `Bibtex`

```bibtex
@techreport{Carvalho_Pacheco_Hydrographic_Observations_at_2022,
  author = {Carvalho Pacheco, Fernando and Santiago-Mandujano, Fernando and Potemra, James T. and Plueddemann, Albert J. and Weller, Robert A. and Fitzgerald, Daniel and Galbraith, Nancy R.},
  doi = {10.xxxx/zenodo.xxxxxxxx},
  institution = {School of Ocean and Earth Science and Technology (SOEST), Department of Oceanography, University of Hawai‘i at Mānoa, Honolulu, HI},
  title = { {Hydrographic Observations at the Woods Hole Oceanographic Institution Hawaii Ocean Time-Series Site (WHOTS): {{ (cookiecutter.current_whots_deployment_date|string)[-4:]}} - {{ (cookiecutter.current_whots_recovery_date|string)[-4:]}}, Data Report #{{cookiecutter.current_whots_deployment_number}}} },
  url = {http://whots{{cookiecutter.current_whots_deployment_number}}-data-report.readthedocs.io/},
  year = { {{ (cookiecutter.created_on|string)[:4]}} },
  note = { This publication is based upon observations from the WHOI-Hawaii
  Ocean Time-series Site (WHOTS) mooring, which is supported in part by the
  National Oceanic and Atmospheric Administration (NOAA) Global Ocean
  Monitoring and Observing (GOMO) Program through the Cooperative Institute
  for the North Atlantic Region (CINAR) under Cooperative Agreement
  NA14OAR4320158. NOAA CPO FundRef number 100007298 to the Woods Hole
  Oceanographic Institution, and by National Science Foundation grants 
  OCE-0327513,OCE-0752606, OCE-0926766, OCE-1260164 and OCE-1756517 to the 
  University of Hawaii for the Hawaii Ocean Time-series. 
  This is SOEST contribution number xXxXxX.}

}
```

## Acknowledgements

- Many people participated in the WHOTS mooring deployment/recovery cruises
  See [Table 2.1](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/2_section.html#table-1)
  and [Table 2.4](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/2_section.html#table-4)

- Thanks are due to all the personnel of the
  [Upper Ocean Processes Group (UOP)](http://uop.whoi.edu) at WHOI who prepared
  the WHOTS buoy’s instrumentation and mooring;

- To [Kelsey Maloney](https://www.linkedin.com/in/kelsey-maloney-4a18291a4),
  [Tully Rohrer](https://hahana.soest.hawaii.edu/hot/staff1.html),
  [Noah Howins](https://www.soest.hawaii.edu/oceanography/profile/Howins-Noah/),
  [Ryan Tabata](https://www.linkedin.com/in/ryan-tabata-69215486/), and
  [James Harris](https://www.linkedin.com/in/james-harris-661170174/)
  for their technical assistance with the moored and shipboard instrumentation;

- We gratefully acknowledge the support from the colleagues at
  [Sea-Bird](https://www.seabird.com) to maintain the quality of the CTD data.

- We would also like to thank the captains and crew of the
  [Ship Oscar Sette](https://www.omao.noaa.gov/learn/marine-operations/ships/oscar-elton-sette/about),
  and the [University of Hawaii (UH) Marine Center](https://www.soest.hawaii.edu/UMC/cms/)
  staff for their efforts.

- This publication is based upon observations from the WHOI-Hawaii Ocean
  Time-series Site (WHOTS) mooring, which is supported in part by the National
  Oceanic and Atmospheric Administration ([NOAA](https://www.noaa.gov/)) Global
  Ocean Monitoring and Observing ([GOMO](https://globalocean.noaa.gov/)) Program
  through the Cooperative Institute for the North Atlantic
  Region ([CINAR](https://website.whoi.edu/cinar/)) under Cooperative Agreement
  NA14OAR4320158. NOAA CPO FundRef number 100007298 to the Woods Hole
  Oceanographic Institution, and by National Science Foundation grants
  [OCE-0327513](https://www.nsf.gov/awardsearch/showAward?AWD_ID=0327513),
  [OCE-0752606](https://www.nsf.gov/awardsearch/showAward?AWD_ID=0752606&HistoricalAwards=false)
  ,
  [OCE-0926766](https://www.nsf.gov/awardsearch/showAward?AWD_ID=0926766&HistoricalAwards=false)
  ,
  [OCE-1260164](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1260164&HistoricalAwards=false)
  and
  [OCE-1756517](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1756517&HistoricalAwards=false)
  to the University of Hawaii for the Hawaii Ocean Time-series.

- This is SOEST contribution number xxxxx.

## Contact 
- You can contact us by emailing <hotdata@hawaii.edu>
- Or open a new issue [here](https://github.com/hot-dogs/whots{{cookiecutter.current_whots_deployment_number}}-data-report/issues)

## References
[Check here](https://whots-annual-report.readthedocs.io/projects/whots{{cookiecutter.current_whots_deployment_number}}-data-report/en/latest/references.html)

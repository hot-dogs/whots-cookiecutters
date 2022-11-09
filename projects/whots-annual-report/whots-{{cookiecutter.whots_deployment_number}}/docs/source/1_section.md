# Introduction

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

With support from the NOAA and the National Science Foundation (NSF), the WHOI
HOT Site (WHOTS) surface mooring has been maintained at Station ALOHA since
August 2004. This project aims to record long-term, high-quality air-sea fluxes
as a coordinated part of the HOT program and contribute to the goals of
observing heat, freshwater, and chemical fluxes at a site representative of the
oligotrophic North Pacific Ocean. The approach is to maintain a surface mooring
outfitted for meteorological and oceanographic measurements at a site near
Station ALOHA by successive mooring turnarounds. These observations will be
used to investigate air-sea interaction processes related to climate
variability

The original mooring system is described in the mooring deployment/recovery
cruise reports {cite}`Plueddemann2006, Whelan2007, Whelan2008,Whelan2008,Whelan2010,Santiago-Mandujano2019,Hasbrouck2019,Santiago-Mandujano2021,Santiago-Mandujano2022`.
Briefly, a Surlyn foam surface buoy is equipped with meteorological
instrumentation, including two complete Air-Sea Interaction Meteorological 
(ASIMET) systems, measuring air and sea surface temperatures, relative humidity,
barometric pressure, wind speed and direction, incoming shortwave and longwave
radiation, and precipitation {cite}`Hosom1995, Colbo2009`. Complete surface
meteorological measurements are recorded every minute, as required to compute
air-sea fluxes of heat, freshwater, and momentum. Each ASIMET system also
transmits hourly averages of the surface meteorological variables via the Argos
satellite system. The mooring line is instrumented to collect time series of
upper ocean temperatures, velocities, and salinities coincident with the
surface forcing record. This mooring includes conductivity, salinity and
temperature recorders, two Vector Measuring Current Meters (VMCMs), and two
Acoustic Doppler current profilers (ADCPs). See the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring diagram in
the {numref}`diagram`.

The subsurface instrumentation is located to resolve the temporal variations of
shear and stratification in the upper pycnocline to support the study of mixed
layer entrainment. Experience with moored profiler measurements near Hawaii
suggests that Richardson number estimates over 10 m scales are adequate.
Salinity is essential to the stratification, as salt-stratified barrier layers
are observed at HOT and in the region {cite}`Kara2000`. Hence, we use Sea-Bird
SeaCATs and MicroCATs with vertical separation ranging from 5 to 20 m to
measure temperature and salinity. We use two ADCPs made by Teledyne RD
Instruments to obtain current profiles across the entrainment zone and in the
mixed layer zone. Both ADCPs are in an upward-looking configuration, one is at
125 m, using 4 m bins, and the other is at 47.5 m using 2 m bins. To provide
near-surface velocity (where ADCP estimates are less reliable), we deploy two
Vector Measuring Current Meters (VMCMs). The nominal mooring design is a
balance between resolving extremes versus the typical annual cycling of the
mixed layer {cite}`Plueddemann2006, Santiago-Mandujano2007`. A pair of Sea-Bird
SeaCATs (SBE-16) or MicroCATs (SBE-37) have been included since the WHOTS-9
deployment (June 2012) to measure near-bottom temperature and salinity.

```{figure} /figures/diagram/whots{{cookiecutter.current_whots_deployment_number}}-diagram.png
:height: 1000px
:align: center
:name: diagram

WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring design
```

The WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring was deployed on 
{{ (cookiecutter.current_whots_deployment_date|string)[3:-5]}} {{ (cookiecutter.current_whots_deployment_date|string)[1:2]}}, {{ (cookiecutter.current_whots_deployment_date|string)[-4:]}}
 ([WHOTS-{{cookiecutter.current_whots_deployment_number}} cruise](http://www.soest.hawaii.edu/whots/wh{{cookiecutter.current_whots_deployment_number}}_dep.html)) 
and was recovered on {{ (cookiecutter.current_whots_recovery_date|string)[3:-5]}} { (cookiecutter.current_whots_recovery_date|string)[1:2]}},  {{ (cookiecutter.current_whots_recovery_date|string)[-4:]}} 
([WHOTS-{{cookiecutter.next_whots_deployment}} cruise](http://www.soest.hawaii.edu/whots/wh{{cookiecutter.next_whots_deployment}}_dep.html)). 
The cruises were aboard the R/V {{cookiecutter.current_whots_ship}}. The WHOTS-{{cookiecutter.next_whots_deployment}} mooring was 
deployed on {{ (cookiecutter.next_whots_deployment_date|string)[3:-5]}}  {{ (cookiecutter.next_whots_deployment_date|string)[1:2]}}, {{ (cookiecutter.next_whots_deployment_date|string)[-4:]}}, during the 
[WHOTS-{{cookiecutter.next_whots_deployment}} cruise](http://www.soest.hawaii.edu/whots/wh{{cookiecutter.next_whots_deployment}}_dep.html) and was 
recovered on {{ (cookiecutter.next_whots_recovery_date|string)[3:-5]}} {{ (cookiecutter.next_whots_recovery_date|string)[1:2]}}, {{ (cookiecutter.next_whots_recovery_date|string)[-4:]}. 


This report documents and describes the oceanographic observations made on the
WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring for nearly one year and ten months and from shipboard
measurements during the two cruises when the mooring was deployed and
recovered. Sections
{ref}`II</2_section.md#description-of-the-WHOTS-{{cookiecutter.current_whots_deployment_number}}-mooring-cruises>` and
{ref}`III</3_section.md#description-of-WHOTS-{{cookiecutter.current_whots_deployment_number}}-mooring>` include a detailed
description of the cruises and the mooring, respectively. Sampling and
processing procedures of the hydrographic casts, thermosalinograph, and
shipboard ADCP data collected during these cruises are described in Section
{ref}`IV</4_section.md#WHOTS-{{cookiecutter.current_whots_deployment_number}}-17-cruise-shipboard-observations>`. Section
{ref}`V</5_section.md#moored-instrument-observations>` includes the processing
procedures for the data collected by the moored instruments:
{ref}`SeaCATs, MicroCATs</5_section.md#microcat-data-processing-procedures>`,
{ref}`Moored ADCPs</5_section.md#acoustic-doppler-current-profiler>` and
{ref}`VMCM</5_section.md#vector-measuring-current-meter-vmcm>`. Plots of the
resulting data and preliminary analysis are presented in Section
{ref}`VI</6_section.md#results>`.

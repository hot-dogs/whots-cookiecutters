# Description of WHOTS-{{cookiecutter.current_whots_deployment_number}} Mooring

The WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring, 
deployed on {{ (cookiecutter.current_whots_deployment_date|string)[3:-5]}} {{ (cookiecutter.current_whots_deployment_date|string)[:2]}}, {{ (cookiecutter.current_whots_deployment_date|string)[-4:]}}, 
from R/V {{cookiecutter.current_whots_ship}}, was outfitted with two complete 
sets of Air-Sea Interaction Meteorological (ASIMET) sensors on the buoy and 
underneath subsurface instruments from 7 to 155 m depth, at 1875 m and near the bottom. See
{cite}`Santiago-Mandujano2021, Santiago-Mandujano2022` for a complete
description of the buoy. The mooring could not be recovered in 2020 as 
originally planned due to ship availability and restrictions related to the 
COVID-19 pandemic. The WHOTS-{{cookiecutter.current_whots_deployment_number}} 
was recovered on 
{{ (cookiecutter.current_whots_recovery_date|string)[3:-5]}} {{ (cookiecutter.current_whots_recovery_date|string)[:2]}}, {{ (cookiecutter.current_whots_recovery_date|string)[-4:]}}.

The buoy tower also contains a radar reflector, two marine lanterns, and
Iridium satellite transmission systems that provide continuous buoy position
monitoring. A Xeos Melo Global Positioning System (GPS) receiver, an SBE-39
temperature sensor adapted to measure air temperature, and a Vaisala WXT-520
multi-variable (temperature, humidity, pressure, wind, and precipitation) were
also mounted on the tower. A fourth positioning system (Xeos Kilo transmitter)
was mounted beneath the hull. Several other instruments were mounted on the
buoy. A Battelle pCO2 system, a pumped SBE-16 CTD, and a SAMI-2 pH sensor were
mounted to the buoy's underside. A Sea-Bird SBE-63 hosted a dissolved oxygen
sensor. Three down-looking radiometers were mounted on the buoy. One
hyperspectral sensor is mounted facing upward near the radiometers as a
reference for the incoming spectral irradiance. A Wetlabs ECOFLNTUS chlorophyll
fluorometer was also mounted on the buoy hull.

Four internally logging Sea-Bird SBE-56 temperature sensors were bolted to the
buoy hull's underside, measuring sea surface temperature (SST) and salinity.
The SBE-56s measured SST once every 60 sec between 80-95 cm below the surface.
Two SBE-37 MicroCATs were at 1.50m measuring at every 300s (See
{numref}`table-7`).

```{table} WHOTS-{{cookiecutter.current_whots_deployment_number}} MicroCAT and SBE-56 Temperature Sensor Information. 
:name: table-7
:widths: auto
:align: center
| **Instrument** | **SN** | **Depth (m)** | **Sample Interval (sec)** |
|:--------------:|:------:|:-------------:|:-------------------------:|
|     SBE-56     |  7212  |     0.80      |            60             |
|     SBE-56     |  7213  |     0.80      |            60             |
|     SBE-56     |  7214  |     0.95      |            60             |
|     SBE-56     |  7215  |     0.80      |            60             |
|    MicroCAT    |  1834  |     1.50      |            300            |
|    MicroCAT    |  1841  |     1.50      |            300            |
```

Instrumentation provided by UH for the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring included 20 SBE-37
Microcats, and two upward-looking RDI Workhorse ADCPs, transmitting in 300 kHz
and 600 kHz,respectively. The Microcats all measured temperature and
conductivity, with ten of them measuring pressure. All MicroCATs were deployed
with antifoulant capsules. In addition to the buoy instrumentation, WHOI
provided two Vector Measuring Current Meters (VMCMs), four deep Microcats (
SBE-37) installed at 1875 m and near the bottom of the mooring, and all 
required subsurface mooring hardware.

The {numref}`mooring_subsurface` provides a listing of the WHOTS-{{cookiecutter.current_whots_deployment_number}} subsurface
instrumentation at their nominal depths on the mooring, along with serial
numbers, sampling rates, and other pertinent information. A cold water spike
was induced to the UH MicroCATs before deployment
({numref}`mooring_subsurface`) and after recovery {numref}`table-8` by placing
an ice pack in contact with their temperature sensor to check for any drift in
their internal clock. To produce a spike in the ADCP data, each instrument’s
transducer was rubbed gently by hand for 20 seconds ({numref}`table-9` 
, and {numref}`table-10`).   

```{figure} /figures/tables/mooring_subsurface_instrument.png
:width: 1000%
:align: center
:name: mooring_subsurface

WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring subsurface instrument deployment information. All times 
are in UTC
```

```{table} WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring C-T and ADCP Instruments recovery information. All times are in UTC (mm/dd/yy hh:mm:ss). Sea-Bird 37 Serial Number (SN). 
:name: table-8
:widths: auto
:align: center
| **Depth (m)** |  **SN**   | **Time out of water** | **Time of Spike** | **Time of End Spike**  | **Time Logging Stopped** | **Samples Logged** |  **Data Quality**  |
|:-------------:|:---------:|:---------------------:|:-----------------:|:----------------------:|:------------------------:|:------------------:|:------------------:|
|       7       |   3617    |     8/29/21 3:17      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:42       |       233016       |        Good        |
|      15       |   6893    |     8/29/21 3:18      |   8/29/21 6:48    |      8/29/21 7:48      |       5/8/21 12:58       |       838859       |        Good        |
|      25       |   6894    |     8/29/21 3:22      |   8/29/21 6:48    |      8/29/21 7:48      |       5/8/21 12:58       |       838859       |        Good        |
|      35       |   6895    |     8/29/21 3:31      |   8/29/21 6:48    |      8/29/21 7:48      |       5/8/21 12:58       |       838859       |        Good        |
|      40       |   6896    |     8/29/21 3:31      |   8/29/21 6:48    |      8/29/21 7:48      |       5/8/21 12:58       |       838859       |        Good        |
|      45       |   6887    |     8/29/21 3:32      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:47       |       559239       |        Good        |
|     47.5      | ADCP 1825 |     8/29/21 2:12      |        N/A        | See {numref}`table-10` |         1/21/20          |       15823        | Failed on 01/21/20 |
|      50       |   6897    |     8/29/21 2:12      |   8/29/21 6:48    |      8/29/21 7:48      |       5/8/21 12:58       |       838859       |        Good        |
|      55       |   6898    |     8/29/21 1:55      |   8/29/21 6:48    |      8/29/21 7:48      |       5/8/21 12:58       |       838859       |        Good        |
|      65       |   6899    |     8/29/21 1:53      |   8/29/21 6:48    |      8/29/21 7:48      |       5/8/21 12:58       |       838859       |        Good        |
|      75       |   3618    |     8/29/21 1:52      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:45       |       233016       |        Good        |
|      85       |   3634    |     8/29/21 1:51      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:42       |       233016       |        Good        |
|      95       |   3670    |     8/29/21 1:50      |   8/29/21 6:48    |      8/29/21 7:48      |      3/16/21 13:52       |       190650       |        Good        |
|      105      |   6889    |     8/29/21 1:49      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:47       |       559239       |        Good        |
|      120      |   6890    |     8/29/21 1:48      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:47       |       559239       |        Good        |
|      125      | ADCP 4891 |     8/29/21 1:44      |        N/A        | See {numref}`table-10` |          7/6/21          |       92393        |        Good        |
|      135      |   6888    |     8/29/21 1:43      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:47       |       559239       |        Good        |
|      155      |   6891    |     8/29/21 1:41      |   8/29/21 6:48    |      8/29/21 7:48      |      1/31/21 10:47       |       559239       |        Good        |
|     1875      |   3639    |     8/29/21 0:52      |   8/29/21 6:48    |      8/29/21 7:48      |       7/21/21 0:19       |       190650       |        Good        |
|     1875      |   12242   |     8/29/21 0:52      |   8/29/21 6:48    |      8/29/21 7:48      |      8/31/21 19:40       |       202689       |        Good        |
|    38 mab     |   11391   |     8/28/21 21:45     |   8/29/21 6:48    |      8/29/21 7:48      |      8/31/21 17:00       |       202657       |        Good        |
|    38 mab     |   12241   |     8/28/21 21:45     |   8/29/21 6:48    |      8/29/21 7:48      |      8/31/21 16:00       |       202645       |        Good        |
```

```{table} WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring ADCP deployment and configuration information. All times are in UTC (mm/dd/yy hh:mm:ss).
:name: table-9
:widths: auto
:align: center
|            **-**            | **ADCP S/N 1825**  | **ADCP S/N 4891**  |
|:---------------------------:|:------------------:|:------------------:|
|     **Frequency (kHz)**     |        600         |        300         |
|  **Number of Depth Cells**  |         25         |         30         |
|   **Depth Cell Size (m)**   |        2 m         |        4 m         |
|   **Pings per Ensemble**    |         80         |         40         |
| **Time per Ensemble (min)** |       10 min       |       10 min       |
|   **Time per Ping (sec)**   |       2 sec        |       4 sec        |
|   **Time of First Ping**    | 10/04/19, 00:00:00 | 10/04/19, 00:00:00 |
| **Transducer 1 Spike Time** | 10/05/19, 03:30:00 | 10/05/19, 03:31:00 |
| **Transducer 2 Spike Time** | 10/05/19, 03:30:15 | 10/05/19, 03:31:15 |
| **Transducer 3 Spike Time** | 10/05/19, 03:30:30 | 10/05/19, 03:31:30 |
| **Transducer 4 Spike Time** | 10/05/19, 03:30:45 | 10/05/19, 03:31:45 |
|      **Time in Water**      | 10/05/19, 19:43:00 | 10/05/19, 20:04:00 |
|        **Depth (m)**        |       47.5 m       |       125 m        |

```

```{table} WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring ADCP recovery information. All times are in UTC (mm/dd/yy hh:mm:ss).
:name: table-10
:widths: auto
:align: center
|                             | **ADCP S/N 1825**  | **ADCP S/N 4891** |
|:---------------------------:|:------------------:|:-----------------:|
| **Transducer 1 Spike Time** |        N/A         |        N/A        |
| **Transducer 2 Spike Time** |        N/A         |        N/A        |
| **Transducer 3 Spike Time** |        N/A         |        N/A        |
| **Transducer 4 Spike Time** |        N/A         |        N/A        |
|    **Time out of Water**    | 08/29/21, 02:12:00 | 08/29/21 01:44:00 |
```

The RDI 300 kHz Workhorse Sentinel ADCP, SN 4891, was deployed at 125 m with
transducers facing upwards with an additional external battery pack. This
instrument was set to ping at 4-second intervals for 160 seconds every 10
minutes, and the burst sampling was designed to minimize aliasing by occasional
large ocean swell orbital motions. The bin size was set for 4 m. The total
number of ensemble records was 92,393. The first ensemble was on 10/04/2019 at
00:00:00Z, and the last was on 07/06/2021 at 14:39.59Z (see {numref}`table-9`,
{numref}`table-10`, and {ref}`/appendices.md#whots-{{cookiecutter.current_whots_deployment_number}}-300-khz-serial-4891` for
more configuration). This instrument also measured temperature.

The RDI 600 kHz Workhorse Sentinel ADCP, SN 1825, was deployed at 47.5 m with
transducers facing upwards with an additional external battery pack. The
instrument was set to ping at 2-second intervals for 160 seconds every 10
minutes, and the burst sampling was designed to minimize aliasing by occasional
large ocean swell orbital motions. The bin size was set for 2 m. The total
number of ensemble records was 15,823. The first ensemble was on 10/04/2019 at
00:00:00Z, and the last was on 01/21/2020 at 20:49:59Z (see {numref}`table-9`
, {numref}`table-10`, and {ref}`/appendices.md#whots-{{cookiecutter.current_whots_deployment_number}}-600-khz-serial-1825`
for more configuration). This instrument also measured temperature.

The two VMCMs, SN 2042 and 2032, were deployed at 10 m and 30 m depth,
respectively. The instruments were prepared for deployment by the WHOI/UOP
group and set to sample at 1-minute interval. These instruments also 
measured temperature.

All WHOTS-{{cookiecutter.current_whots_deployment_number}} instruments were successfully recovered; recovery information for
the C-T instruments is shown in {numref}`table-8`. Most of the instruments had
some degree of biofouling, with the most substantial fouling near the surface.
The fouling extended down to the ADCP at 125 m, although it was minor at that
level. 

All MicroCATs were in good condition after recovery, although with more
biofouling than usual given that they were in the water for nearly 2 years.
MicroCAT SN 6899 (65 m) had a barnacle partially blocking the top of its
conductivity cell. 

After recovery and before stopping recording, a bag of ice was placed in
contact with each MicroCAT temperature sensor, to produce a spike in the data
as a reference point to check the instrument’s clock. However, it was later
found that all the instruments had stopped logging data due to battery
drainage, except for the deep instruments. The data from all instruments were
downloaded on board the ship, the instruments returned data records ending as
early as January 31, 2021. {numref}`table-8` has an initial evaluation of the
data quality; more details are in
{ref}`/5_section.md#microcat-data-processing-procedures`, and
{ref}`/6_section.md#microcat-data`.

The data from the upward-looking 300 kHz ADCP at 125 m were good; the
instrument was not pinging upon recovery and the data record indicates that it
stopped recording on July 6, 2021. There appears to be no obviously
questionable data from this ADCP at this time, apart from near-surface
side-lobe interference. The 600 kHz instrument (47.5 m) was recovered with its battery
wire cut and separated from the instrument. The data record indicates that it
stopped recording on January 21, 2020.
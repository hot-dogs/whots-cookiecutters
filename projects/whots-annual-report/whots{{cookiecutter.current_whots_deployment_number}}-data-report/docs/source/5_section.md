# Moored Instrument Observations

## MicroCAT Data Processing Procedures

Each moored MicroCAT temperature, conductivity, and pressure (when installed)
was calibrated at Sea-Bird before their deployment and after their recovery on
the dates shown in {numref}`table-14`. The internally-recorded data from each
instrument were downloaded onboard the ship after the mooring recovery. The
nominally-calibrated data were plotted for a visual assessment of the data
quality. The data processing included checking the internal clock data against
external event times, pressure sensor drifts correction, temperature sensor
stability, and conductivity calibration against CTD data from casts conducted
near the mooring during HOT and WHOTS cruises. The detailed processing
procedures are described in this section.

```{table} WHOTS-{{cookiecutter.current_whots_deployment_number}} MicroCAT temperature sensor calibration dates and sensor drift during deployments; *SN = Sea-Bird Serial Number; PDC = Pre-Deployment Calibration; PRC = Post-Recovery Calibration; TSA = Temperature Sensor's Annual Drift during WHOTS-{{cookiecutter.current_whots_deployment_number}} ; N. depth = Nominal deployment depth*
:class: sd-m-auto
:align: center
:name: table-14
| **N. depth (m)** | **SN** |  **PDC**  |  **PRC**  | **TSA(mili°C)** |
|:----------------:|:------:|:---------:|:---------:|:---------------:|
|      **7**       |  3617  | 21-Nov-18 | 17-Nov-21 |      -0.31      |
|      **15**      |  6893  | 13-Dec-18 | 4-Nov-21  |      0.07       |
|      **25**      |  6894  | 13-Dec-18 | 4-Nov-21  |      0.46       |
|      **35**      |  6895  | 13-Dec-18 | 5-Nov-21  |      -0.33      |
|      **40**      |  6896  | 12-Dec-18 | 5-Nov-21  |      -1.23      |
|      **45**      |  6887  | 14-Dec-18 | 10-Nov-21 |      -0.14      |
|      **50**      |  6897  | 12-Dec-18 | 4-Nov-21  |       0.6       |
|      **55**      |  6898  | 14-Dec-18 | 4-Nov-21  |      0.02       |
|      **65**      |  6899  | 13-Dec-18 | 4-Nov-21  |      0.34       |
|      **75**      |  3618  | 18-Dec-18 | 4-Nov-21  |      0.46       |
|      **85**      |  3634  | 13-Dec-18 | 4-Nov-21  |      1.36       |
|      **95**      |  3670  | 14-Dec-18 | 10-Nov-21 |      -0.31      |
|     **105**      |  6889  | 12-Dec-18 | 10-Nov-21 |      -0.05      |
|     **120**      |  6890  | 12-Dec-18 | 10-Nov-21 |      -0.04      |
|     **135**      |  6888  | 19-Dec-18 | 10-Nov-21 |      -0.54      |
|     **155**      |  6891  | 19-Dec-18 | 10-Nov-21 |      -0.1       |
|     **1875**     |  3639  | 15-Jun-16 | 27-Feb-22 |      -0.07      |
|     **1875**     | 12242  | 25-May-14 | 25-Feb-22 |      -0.39      |
|     **4713**     | 11391  | 7-Dec-13  | 10-Mar-22 |      -0.56      |
|     **4713**     | 12241  | 23-May-14 | 25-Feb-22 |      -1.01      |
```

### Internal Clock Check and Missing Samples

Before the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring deployment and after its recovery (before the data
logging was stopped), the MicroCATs temperature sensors were placed in contact
with an ice pack to create a spike in the data, to check for any problems with
their internal clocks, and for possible missing samples ({numref}`table-8`).
However, it was found after recovery that all the instruments had stopped logging data
due to battery drainage, except for the deep instruments.
The cold spike before deployment was detected by a sudden decrease in temperature. For all the
instruments, the clock time of this event matched the time of the spike (within
the sampling interval of each instrument) correctly. No missing samples were
detected for any of the devices.

### Pressure Drift Correction and Pressure Variability

Some MicroCATs used in the moorings were outfitted with pressure sensors (
{numref}`mooring_subsurface`). Biases were detected in the pressure sensors by
comparing the on-deck pressure readings (which should be zero for standard
atmospheric pressure at sea level of 1029 mbar) before deployment and after recovery.
{numref}`table-15` shows the magnitude of the bias for each of the sensors
before and after deployment. To correct this offset, a linear fit between the
initial and final on-deck pressure offset as a function of time was obtained
and subtracted from each sensor. Only three of the deep instruments registered
on-deck pressure after recovery, all other instruments stopped recording data
before recovery due to battery drainage. For these last instruments only a  
before-deployment pressure bias correction was applied.
{numref}`figure5.1` shows the linearly
corrected pressures measured by the MicroCATs located above 200 m during the
WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment. For all these sensors, the mean difference from the
nominal instrument pressure (based on the deployed depth) was less than 1.2
dbar. The standard deviation of the pressure for the duration of the record was
less than 1 dbar for all sensors, with the deeper sensors showing a slightly
larger standard deviation. The range of variability for all sensors was about ±
3 dbar.

The causes of pressure variability can be several, including density variations
in the water column above the instrument; horizontal dynamic pressure (not only
due to the currents but also due to the motion of the mooring); mooring
position {cite}`Santiago-Mandujano2007`.

```{table} Pressure bias of MicroCATs with pressure sensors for WHOTS-{{cookiecutter.current_whots_deployment_number}}. All the instruments with a NA pressure bias ended recording before recovery. SN = Sea-bird Serial Number; BBD = Bias Before Deployment (dbar); BAR = Bias After Recovery (dbar)
:class: sd-m-auto
:align: center
:name: table-15
| **Depth (m)** | **SN** | **BBD(dbar)** | **BAR(dbar)** |
|:-------------:|:------:|:-------------:|:-------------:|
|    **45**     |  6887  |     0.07      |      NA       |
|    **95**     |  3670  |     -1.2      |      NA       |
|    **105**    |  6889  |      0.1      |      NA       |
|    **120**    |  6890  |     0.11      |      NA       |
|    **135**    |  6888  |     0.12      |      NA       |
|    **155**    |  6891  |     0.07      |      NA       |
|   **1875**    |  3639  |     -0.04     |      NA       |
|   **1875**    | 12242  |      0.1      |      0.9      |
|   **4713**    | 11391  |      0.5      |       2       |
|   **4713**    | 12241  |      0.4      |      1.5      |
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}pbias_a.png
:height: 1000px
:align: center
:name: figure5.1

Linearly corrected pressures from MicroCATs between 7 and 155 m during
WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment. The horizontal dashed line is the sensor’s nominal
pressure, based on deployed depth. The text on the left (right) side of the
figure indicates the mean (standard deviation) of the difference between each
instrument’s pressure and nominal pressure.

```

### Temperature Sensor Stability

The MicroCAT temperature sensors were calibrated at Sea-Bird before and after
each deployment, and their annual drift evaluations based on these calibrations
are shown in {numref}`table-14`. These values turned out to be insignificant (
not higher than 0.002 °C) for all sensors. Comparisons between the MicroCAT and
CTD data from casts conducted near the mooring during HOT cruises confirmed
that the rest of the moored instruments' temperature drift was insignificant. .
The two MicroCATs (SN 11391 and SN 12241) deployed near the bottom were drift
corrected. {numref}`figure5.7` (upper panel) shows the temperature differences
between both instruments before and after the correction. After the correction,
the temperature differences were in the ±0.001 °C range.

Temperature comparisons between one of the WHOTS-{{cookiecutter.current_whots_deployment_number}} near-surface MicroCAT
(SN 1834) and the four SBE-56 surface temperature sensors in the buoy hull
{numref}`table-7` are shown in {numref}`figure5.2`. All the SBE-56 instruments
returned full records, and none of them show any obvious bias compared to the
Microcat measurements.

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}tcompare_1.png
:height: 1000px
:align: center
:name: figure5.2

The temperature difference between MicroCAT SN 7212 at 1 m, and near-surface
temperature sensors SN 7212 (top panel), 7213 (second panel), 7214 (third
panel), and 7215 (bottom panel), during the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment. The light blue
line is a 24-hour running mean of the differences.
```

In addition to the Sea-Bird temperature sensors, there were additional
temperature sensors in the VMCMs (at 10 and 30 m) and in the ADCPs (at 47.5 m
and 125 m). Comparisons with the temperatures from adjacent MicroCATs were
conducted to evaluate the temperatures from those sensors.

#### Comparisons with VMCM and ADCP temperature sensors

The upper panel of {numref}`figure5.3` shows the difference between the 10-m
VMCM and the 7-m MicroCAT temperatures during WHOTS-{{cookiecutter.current_whots_deployment_number}}, after adding a 0.0259°C
offset correction to the VMCM. The offset was the mean difference between
the uncorrected VMCM and the 7-m MicroCAT data. Also shown for comparison in
the middle panel of the figure are the corrected VMCM temperature differences
from the 15 m MicroCAT. The VMCM temperatures had a 0.04 °C offset in April 2020. The lower panel shows the temperature fluctuations in the differences
between the 7 and 15-m MicroCATs, which seem to be around zero.

Temperature differences between the 30-m VMCM and the temperatures from
adjacent MicroCATs at 25 and 35-m during WHOTS-{{cookiecutter.current_whots_deployment_number}} are shown in
{numref}`figure5.4` after adding a 0.0147°C offset correction to the VMCM. The
offset was the mean difference between the uncorrected VMCM and the 25-m
MicroCAT data. For comparison, the differences between the MicroCATs
temperatures are also shown in the lower panel.

Temperature differences between the 47.5-m ADCP and the temperatures from
adjacent MicroCATs at 45 and 50-m during WHOTS-{{cookiecutter.current_whots_deployment_number}} are shown in
{numref}`figure5.5`. The ADCP failed and stopped collecting data on January
21, 2020 (see {ref}`/3_section.md#description-of-whots-{{cookiecutter.current_whots_deployment_number}}-mooring`). For
comparison, the differences between the MicroCATs temperatures are also
shown in the lower panel.

Temperature differences between the 125-m ADCP and the temperatures from
adjacent MicroCATs at 120 and 135-m during WHOTS-{{cookiecutter.current_whots_deployment_number}} are shown in
{numref}`figure5.6`. For comparison, the differences between the MicroCATs
temperatures are also shown in the lower panel. It is difficult to assess the
quality of the ADCP temperature from these comparisons. These sensors were
located at the top of the thermocline, where we expect to find substantial
temperature differences between adjacent sensors. However, an indication of the
ADCP temperatures' quality is given in the upper panel plot, which shows
temperatures fluctuating closely around zero.

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}tcompare_22.png
:height: 1000px
:align: center
:name: figure5.3

The temperature difference between the 7-m MicroCAT and the 10-m VMCM (upper
pane)l; between the 15-m MicroCAT and the 10-m VMCM (middle panel); and between
the 7-m and the 15-m MicroCATs (lower panel ) during the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment.
The light blue line is a 24-hour running mean of the differences.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}tcompare_33.png
:height: 1000px
:align: center
:name: figure5.4

The temperature difference between the 25-m MicroCAT and the 30-m VMCM (upper
panel); between the 35-m MicroCAT and the 30-m VMCM (middle panel); and between
the 25-m and the 35-m MicroCATs (lower panel) during the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment.
The light blue line is a 24-hour running mean of the differences.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}tcompare_4.png
:height: 1000px
:align: center
:name: figure5.5

The temperature difference between the 45-m MicroCAT and the 47.5-m ADCP (upper
panel). (The ADCP stopped collecting data on 2020/1/21); between the 50-m
MicroCAT and the 47.5-m ADCP (middle panel); and between the 45-m and the 50-m
MicroCATs (lower panel) during the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment. The light blue line is
a 24-hour running mean of the differences.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}tcompare_5.png
:height: 1000px
:align: center
:name: figure5.6

The temperature difference between the 120-m MicroCAT and the 125-m ADCP (upper
panel); between the 135-m MicroCAT and the 125-m ADCP (middle panel); and
between the 120-m and the 135-m MicroCATs (lower panel) during the WHOTS-{{cookiecutter.current_whots_deployment_number}}
deployment. The light blue line is a 24-hour running mean of the differences.
```

### Conductivity Calibration

The results of the Sea-Bird post-recovery conductivity calibrations indicated
that some MicroCAT conductivity sensors experienced relatively large offsets
from their pre-deployment calibration. These were qualitatively confirmed by
comparing the mooring data against CTD data from casts conducted between 200 m
and 5 km from the mooring during HOT cruises. The conductivity offsets are not
apparent, and there may have been multiple causes ( see {cite}`Freitag1999`
for a similar experience with conductivity cells during COARE). For some
instruments, the offset was negative, caused perhaps by biofouling of the
conductivity cell. In contrast, for others, the offset was positive, for
reasons still unknown. A visual
inspection of the instruments after recovery did not show any apparent signs of
biofouling. There were no cell scourings reported in the post-recovery reviews
at Sea-Bird.

Corrections of the MicroCATs conductivity data were conducted by comparing them
against CTD data from profiles and yo-yo casts conducted near the mooring
during HOT cruises and during deployment/recovery cruises. Casts led between
200 and 1000 m from the mooring were given extra weight in the correction
compared to those conducted between 1 and 5 km away. Casts more than 5 km away
from the mooring were not used. Given that the CTD casts are conducted at least
200 m from the mooring, CTD and MicroCAT data's alignment was done in density
rather than in-depth. For cases where the alignment in density was not possible
due to large conductivity offsets (causing unrealistic mooring density values),
the alignment was done in temperature space. A cubic least-squares fit (LSF) to
the CTD-MicroCAT differences against time was applied as a first approximation,
and the corresponding correction was applied.

Some sensors had large offsets and noticeable variability that could not
be explained by a cubic LSF (see below). For these sensors, a stepwise
correction was applied to match the data to the available CTD cast data and
then to use the differences between consecutive sensors to determine when the
sensor started to drift. For instance, during periods of weak stratification,
the conductivity difference between neighboring sensors A, B, and C could reach
near-zero values, in particular for instruments near the surface, which are the
ones most prone to suffer conductivity offsets. A sudden conductivity offset
observed during this period between sensors A and B, but not between sensors A
and C could indicate the beginning of an offset for sensor B.

Given that the most in-depth instruments on the mooring are less likely to be
affected by biofouling and consequent sudden conductivity drift, the deep
instruments served as an excellent reference to find any possible malfunction
in the shallower ones. Therefore, the conductivity from the deepest instruments
was corrected first, and the correction was continued sequentially upwards
toward the shallower ones.

As a quality control to the conductivity corrections, the buoyancy frequency
between neighboring instruments was calculated using finite differences. Over-
or under-corrected conductivities yielded instabilities in the water column (
negative buoyancy frequency) that were easy to detect and were not real when
lasting for several days. Based on this, the conductivity correction of the
corresponding sensors was revised.

Correction of the deep and the near-bottom MicroCATs' conductivities were done following
similar procedures than for the shallow instruments, by comparing them
against CTD data from near-bottom profiles conducted during HOT cruises
({numref}`figure5.7`, bottom panel). After correction, the salinity
differences between both instruments were in the ±0.001 range.

Another characteristic of the offsets in the conductivity sensors is that their
development is not always linear in time. Their behavior can be highly variable
{cite}`Santiago-Mandujano2007`. The corrections applied to each of the
conductivity sensors during WHOTS-{{cookiecutter.current_whots_deployment_number}} are shown in {numref}`figure5.8`
through {numref}`figure5.15`. Most of the instruments had a drift of less than
0.04 Siemens/m for the duration of the deployment (except for the near-surface
instrument SN 1834 which had a 0.08 S/m drift), corrected with a linear or
cubic least-squares fit. Many of the instruments deployed above 120 m showed a
negative drift starting a few months before the end of their record, apparently
due to the anti-foulant expiration.

```{figure} figures/microcats/plt_w{{cookiecutter.current_whots_deployment_number}}_deep_corr.png
:height: 1000px
:align: center
:name: figure5.7

Temperature differences (top panel) and salinity differences (bottom panel)
between MicroCATs #12241 and #11391 during WHOTS-{{cookiecutter.current_whots_deployment_number}}. The blue (red) lines are
the differences before (after) correcting the data following the text's
procedures.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr1.jpg
:height: 1000px
:align: center
:name: figure5.8

Conductivity sensor corrections for MicroCATs from 1 to 7 meters during
WHOTS-{{cookiecutter.current_whots_deployment_number}}.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr2.jpg
:height: 1000px
:align: center
:name: figure5.9

Conductivity sensor corrections for MicroCATs from 15 to 35 meters during
WHOTS-{{cookiecutter.current_whots_deployment_number}}
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr3.jpg
:height: 1000px
:align: center
:name: figure5.10

Conductivity sensor corrections for MicroCATs from 40 to 50 meters during
WHOTS-{{cookiecutter.current_whots_deployment_number}}
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr4.jpg
:height: 1000px
:align: center
:name: figure5.11

Conductivity sensor corrections for MicroCATs from 55 to 75 meters during
WHOTS-{{cookiecutter.current_whots_deployment_number}}.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr5.jpg
:height: 1000px
:align: center
:name: figure5.12

Conductivity sensor corrections for MicroCATs from 85 to 105 meters during
WHOTS-{{cookiecutter.current_whots_deployment_number}}.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr6.jpg
:height: 1000px
:align: center
:name: figure5.13

Conductivity sensor corrections for MicroCATs from 120 to 155 meters during
WHOTS-{{cookiecutter.current_whots_deployment_number}}
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr7.jpg
:height: 1000px
:align: center
:name: figure5.14

Conductivity sensor corrections for MicroCATs at 1875 and 4713 meters
during WHOTS-{{cookiecutter.current_whots_deployment_number}}.
```

```{figure} figures/microcats/w{{cookiecutter.current_whots_deployment_number}}mic_corr8.jpg
:height: 1000px
:align: center
:name: figure5.15

Conductivity sensor correction for MicroCAT at 4713 meters during WHOTS-{{cookiecutter.current_whots_deployment_number}}
```

## Acoustic Doppler Current Profiler

Two TRDI broadband Workhorse Sentinel ADCP’s were deployed on the WHOTS-{{cookiecutter.current_whots_deployment_number}}
mooring. A 600 kHz ADCP was deployed at 47.5 m depth in the upward-looking
configuration, and a 300 kHz ADCP was deployed at 125 m, also in the
upward-looking configuration. The instruments were installed in aluminum frames
and an external battery module to provide sufficient power for the intended
period of deployment. The four ADCP beams were angled at 20° from the vertical
line of the instrument. The 300 kHz ADCP was set to profile across 30 range
cells of 4 m with the first bin centered at 6.25m from the transducer. The 600
kHz ADCP was set to profile across 25 range cells of 4 m with the first bin
centered at 3.12m from the transducer. The specifications of the instrument are
shown in {numref}`table-16`.

```{table} Specifications of the ADCP’s used for the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring.
:class: sd-m-auto
:align: center
:name: table-16
|  **Frequency (kHz)**  |      **Instrument**       |    **Model**    |  **Serial Number**  |
|:---------------------:|:-------------------------:|:---------------:|:-------------------:|
|        **300**        |  TRDI Workhorse Sentinel  |  WHS300-I-UG86  |        4891         |
|        **600**        |  TRDI Workhorse Sentinel  |    WHS600-I     |        1825         |
```

### Compass Calibrations

#### Pre-Deployment

Before the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment, field calibration of the internal ADCP compass
was performed at the University of Hawaii’s soccer field at Manoa on September
2019, for 300 kHz and the 600 kHz instruments. Each instrument was mounted in
the deployment cage with the external battery module and was located away from
potential sources of magnetic field disturbances. The ADCP was mounted to a
turntable, aligned with the magnetic north using a surveyor’s compass. Using
the built-in RDI calibration procedure, the instrument was tilted in one
direction between 10 and 20 degrees and then rotated through 360 degrees at
less than 5° per second. The ADCP was then tilted in a different direction, and
a second rotation was made. Based on the results from the first two rotations,
calibration parameters are temporarily loaded, and the instrument, tilted in a
third direction, is rotated once more to check the calibration. Results from
each pre-deployment field calibration are shown in {numref}`table-17` and
{numref}`table-18` ({numref}`figure5.16` and {numref}`figure5.17`).

```{table} Results from the WHOTS-{{cookiecutter.current_whots_deployment_number}} pre-deployment 300 kHz ADCP compass field calibration procedure. *SCE = Single Cycle Error (°); DCE = Double Cycle Error (°); LD_SCE = Largest Double + Single Cycle Error (°); RMS_RE = RMS of 3rd Order and Higher + Random Error (°); OE = Overall Error (°); PM_STD = Pitch, Mean and St. Deviation (°); RM_STD = Roll, Mean and St. Dev. (°)*
:class: sd-m-auto
:align: center
:name: table-17
|  **(SN 4891)**  | **SCE** | **DCE** | **LD_SCE** | **RMS_RE** | **OE** |  **PM_STD**  | **RM_STD** |
|:---------------:|:-------:|:-------:|:----------:|:----------:|:------:|:------------:|:----------:|
|   **Before**    |  2.41   |  0.47   |    2.88    |    0.23    |  2.39  |  1.64 ±0.43  |  0.1±0.42  |
|    **After**    |  0.78   |  0.07   |    0.85    |    0.37    |  0.79  | -17.08 ±0.44 | -0.01±0.81 |
```

```{table} Results from the WHOTS-{{cookiecutter.current_whots_deployment_number}} pre-deployment 600 kHz ADCP compass field calibration procedure. See acronyms on [Table 5.4](table-17)
:class: sd-m-auto
:align: center
:name: table-18
| **(SN 1825)** | **SCE** | **DCE** |  **LD_SCE**  |  **RMS_RE**  |  **OE**  |   **PM_STD**   |  **RM_STD**  |
|:-------------:|:-------:|:-------:|:------------:|:------------:|:--------:|:--------------:|:------------:|
|  **Before**   |  1.44   |  0.27   |     1.71     |     0.13     |   1.52   |   1.42 ±0.35   |  0.47 ±0.34  |
|   **After**   |  0.15   |  0.27   |     0.42     |     0.21     |   0.37   |  -17.76 ±0.33  |  -0.85±0.69  |
```

#### Post-Deployment

After the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring was recovered, the ADCP compass's performance was
tested at the University of Hawai’i’s soccer field at Manoa on September 9,
2021, with an identical compass calibration procedure as during the
pre-deployment calibration. Results from the WHOTS-{{cookiecutter.current_whots_deployment_number}} post-deployment ADCP
compass field calibration procedure are listed in {numref}`table-19` and
{numref}`table-20` ({numref}`figure5.16` and {numref}`figure5.17`).

```{table} Results from the WHOTS-{{cookiecutter.current_whots_deployment_number}} post-deployment 300kHz ADCP compass field calibration procedure. See acronyms on [Table 5.4](table-17)
:class: sd-m-auto
:align: center
:name: table-19
|  **(SN 4891)**  |  **SCE**  |  **DCE**  |  **LD_SCE**  |  **RMS_RE**  |  **OE**  |  **PM_STD**   |  **RM_STD**  |
|:---------------:|:---------:|:---------:|:------------:|:------------:|:--------:|:-------------:|:------------:|
|    **After**    |   2.00    |   0.05    |     2.05     |     0.15     |   2.00   |  -0.03 ±0.40  |  0.13±0.49   |
```

```{table} Results from the WHOTS-{{cookiecutter.current_whots_deployment_number}} post-deployment 600kHz ADCP compass field calibration procedure. See acronyms on [Table 5.4](table-17)
:class: sd-m-auto
:align: center
:name: table-20
|  **(SN 1825)**  |  **SCE**  |  **DCE**  |  **LD_SCE**  |  **RMS_RE**  |  **OE**  |  **PM_STD**  |  **RM_STD**  |
|:---------------:|:---------:|:---------:|:------------:|:------------:|:--------:|:------------:|:------------:|
|    **After**    |   0.99    |   0.23    |     1.21     |     0.19     |   1.07   |  0.10 ±0.43  |  0.47±0.41   |
```

```{figure} figures/adcp_moored/adcp_whot{{cookiecutter.current_whots_deployment_number}}cmpserr_sn4891.png
:height: 600px
:align: center
:name: figure5.16

Results of the post-cruise compass calibration, conducted September 9, 2021,
on ADCP SN 4891 at the University of Hawai’i at Manoa.
```

```{figure} figures/adcp_moored/adcp_whot{{cookiecutter.current_whots_deployment_number}}cmpserr_sn1825.png
:height: 600px
:align: center
:name: figure5.17

Results of the post-cruise compass calibration, conducted September 9, 2021,
on ADCP SN 1875 at the University of Hawai’i at Manoa.
```

### ADCP Configurations

Individual configurations for the two ADCP’s on the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring are
detailed in {ref}`/appendices.md#whots-{{cookiecutter.current_whots_deployment_number}}-300-khz-serial-4891`, and
{ref}`/appendices.md#whots-{{cookiecutter.current_whots_deployment_number}}-600-khz-serial-1825`. The salient differences for
each of the ADCP’s are summarized below.

#### 300 kHz (SN/4891 - 125m)

The ADCP, set to a beam frequency of 300 kHz, was configured in a burst
sampling mode consisting of 40 pings per ensemble to resolve low-frequency wave
orbital motions. The interval between each ping was 4 seconds, so the ensemble
length was 160 seconds. The interval between ensembles was 10 minutes. Data
were recorded in earth coordinates, with a heading bias of 9.54° E due to
magnetic declination. False targets, usually fish, were screened by setting the
threshold maximum to 70 counts. Velocity data were rejected if the difference
in echo intensity among the four beams exceeded this threshold.

#### 600 kHz (SN/1825- 47.5m)

The ADCP, set to a beam frequency of 600 kHz, was configured in a burst
sampling mode consisting of 80 pings per ensemble. The interval between each
ping was 2 seconds, so the ensemble length was also 160 seconds. The interval
between ensembles was 10 minutes. Data were recorded in earth coordinates with
a heading bias of 9.54° E. The threshold maximum was also set to 70 counts.
Velocity data were rejected if the difference in echo intensity among the four
beams exceeded this threshold.

### ADCP data processing procedures

Binary files output from the ADCP were read and converted to MATLAB™ binary
files using scripts developed by
[Eric Firing’s ADCP lab](https://currents.soest.hawaii.edu). The beginning of
the raw data files was truncated to a time after the mooring anchor was
released to allow time for the anchor to reach the seabed and for the mooring
motions that follow the anchor's impact on the seafloor to dissipate. The
pitch, roll, and ADCP temperature were examined to pick reasonable times that
ensured good data quality without unnecessarily discarding too much data
({numref}`figure5.18`, {numref}`figure5.19`). Truncation at the end of the data
files was chosen to be the ensemble before the acoustic release signal was sent
to avoid contamination due to the instrument's ascent. The times of the first
ensemble from the raw data, deployments, and recovery time, along with the
truncated records of both deployments, are shown in {numref}`table-21`.

```{figure} figures/adcp_moored/300_rawt_plt.png
:height: 500px
:align: center
:name: figure5.18

Temperature record from the 300 kHz ADCP during WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring (top panel).
The bottom panel shows the beginning and end of the record, with the green
vertical line representing the in-water time during deployment and out-of-water
recovery time. The red line represents the anchor release and acoustic release
trigger for deployment and recovery, respectively.
```

```{figure} figures/adcp_moored/600_rawt_plt.png
:height: 500px
:align: center
:name: figure5.19

Same as {numref}`figure5.18`, but for the 600 kHz ADCP.
```

```{table} ADCP record times (UTC mm/dd/yyyy, hh:mm:ss) during WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment
:class: sd-m-auto
:align: center
:name: table-21
|       **Activities**       |       **300 kHz**       |       **600 kHz**       |
|:--------------------------:|:-----------------------:|:-----------------------:|
|     **Raw file start**     |  10/4/2019,  00:00:00   |  10/4/2019,  00:00:00   |
|      **Raw file end**      |   7/6/2021,  14:39:59   |  1/21/2020,  20:49:59   |
|     **ADCP In water**      |  10/5/2019,  20:04:00   |  10/5/2019,  19:43:00   |
|      **Anchor over**       |  10/06/2019,  02:12:00  |  10/06/2019,  02:12:00  |
|  **Anchor release fired**  |  08/28/2021,  17:52:00  |  08/28/2021,  17:52:00  |
|      **ADCP on deck**      |  08/29/2021,  01:44:00  |  8/29/2021,  02:12:00   |
```

#### ADCP Clock Drift

Upon recovery, a spike is normally produced in the ADCP data by gently rubbing
each instrument’s transducer by hand for 20 seconds (see {numref}`table-10`) to
compare the ADCP clocks with the ship’s time server. Unfortunately, the clock
on both ADCPs could not be evaluated because the instrument stopped working
before recovery. Past deployments of the ADCP’s suggest a 3-minute difference
is not unusual. No drift corrections were made. However, this drift may be
significant if the data are used for time-dependent analysis, such as tidal or
spectrum analysis. A drift correction needs to be applied in those cases.

#### Heading Bias

As mentioned in the ADCP configuration section, the data were recorded in the
earth coordinates. A heading bias, the angle between magnetic north and true
north, can be included in the setup to obtain output data in true-earth
coordinates. Magnetic variation was obtained from the
[National Geophysical Data Center ‘Geomag’ calculator](https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml#declination)
. A constant value is acceptable for a yearlong deployment because the change
in declination is small, approximately -0.02°{math}`year^{-1}` at the
WHOTS
location. A heading bias of 9.54° was entered in the setup of the WHOTS-{{cookiecutter.current_whots_deployment_number}}
ADCP’s.

#### Speed of sound

Due to the constant proportionality between the Doppler shift and water speed,
the speed of sound needs only be measured at the transducer head
{cite}`Firing1991`. The sound speed used by the ADCP is calculated using a
constant value of salinity (35) and the temperature recorded by the transducer
temperature sensor of the ADCP. Using CTD profiles close to the mooring during
HOT cruises, HOT-316 to 332, and from the WHOTS deployment/recovery cruises,
the mean salinity at 125 dbar was 34.95 while the mean salinity at 47.5 dbar
was 34.87. The mean ADCP temperature at 125 dbar was 21.38 °C and 25.86 °C at
47.5dbar
({numref}`figure5.18`, {numref}`figure5.19`, and {numref}`figure5.20`).The mean
sound velocity at 47.5 and 125 dbar was {math}`1537.04 ms^{-1}` and
{math}`1527.12 ms^{-1}`, respectively.

```{figure} figures/adcp_moored/wh{{cookiecutter.current_whots_deployment_number}}_CTD_sv_profile.png
:height: 800px
:align: center
:name: figure5.20

Sound speed profile (top panel) during the deployment of the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring
from 2 dbar CTD data taken during regular HOT cruises and CTD profiles taken
during the WHOTS-{{cookiecutter.current_whots_deployment_number}} and -{{cookiecutter.next_whots_deployment}}) deployment cruises (individual casts marked with a
red diamond). The bottom left panels show the sound velocity at a depth of the
ADCP’s (47.5 m and 125 m), with the mean sound velocity indicated with a
dashed black line. The lower right panels show the temperature and salinity
at each ADCP depth for the time series, with the mean temperatures
indicated with blue lines and mean salinity indicated with red lines.
```

#### Quality Control

Quality control of the ADCP data involved the thorough examination of the
velocity, instrument orientation, and diagnostic fields to develop the basis of
the QC flagging procedures. Details of the methods used can be found in the
WHOTS Data Report 1 {cite}`Santiago-Mandujano2007`. The following QC
procedures were applied to the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment of ADCP data.

1. The first bin (closest to the transducer) is sometimes corrupted due to what
   is known as ringing. A period of time is needed for the sound energy
   produced during a transducer's transmit pulse to dissipate before the ADCP
   can adequately receive the returned echoes. This “blanking interval” is used
   to prevent useless data from being recorded. If it is too short, signal
   returns can be contaminated by the lingering noise from the transducer. The
   blanking interval is expressed as a distance. The default value of 1.76 m
   was used for the 300 kHz ADCP, whereas an interval of 0.88 m was used for
   the 600 kHz ADCP. As a result, bin one was flagged and replaced with ` Not a
Number (NaN)` in the quality-controlled dataset ({numref}`figure5.21`).

   ```{figure} figures/adcp_moored/wh{{cookiecutter.current_whots_deployment_number}}_ringing.png
   :height: 600px
   :align: center
   :name: figure5.21

   Eastward velocity component for the 300 kHz (top panel) and the 600 kHz (bottom
   panel) ADCPs are showing the incoherence between depth bins 1 (red), 2 (green),
   and 3 (blue).
   ```

2. For an upward-looking ADCP with a beam angle of 20° within range of the sea
   surface, the upper 6% of the depth range is contaminated with sidelobe
   interference {cite}`Teledyne2011`. This contamination results
   from the much stronger signal reflection from the sea surface than from
   scatters, overwhelming the sidelobe suppression of the transducer. Data
   quality is quantified using echo intensity, a measure of the backscattered
   echo's strength for each depth cell. With distance from the transducer
   sensor, echo intensity is expected to decrease. Sharp increases in echo
   intensity indicate contamination from surface reflection. Most of the data
   within the upper four bins (~14% of the vertical range) were flagged. These
   top four bins range from about 15 m up to the sea surface.

3. The Janus configuration of four beams (along with instrument orientation)
   is used to resolve currents into their component earth-referenced
   velocities, providing a second estimate of the vertical velocity. The scaled
   difference between these estimates is defined as the error velocity, and it
   is useful for assessing data quality. Error velocities with an absolute
   magnitude more significant than {math}`0.15 ms^{-1}` (value comparable to
   the standard deviation of observed horizontal velocities) were flagged and
   removed.

4. An indication of data quality for each ensemble is given by the “percent
   good” data indicator, which accompanies each beam for each bin. The use of
   the percent good indicator is determined by the coordinate transformation
   mode used during the data collection. For profiles transformed into earth
   coordinates, the percent good field shows the percentage of pings that could
   be used to create the earth coordinate velocities. The percent good fields
   show the percentage of data made using 4 and 3 beam solutions in each depth
   cell within an ensemble and the percentage that was rejected due to failing
   one of the criteria set during the instrument setup (see
   {ref}`/appendices.md#whots-{{cookiecutter.current_whots_deployment_number}}-300-khz-serial-4891`). Data were flagged when
   data in each depth cell within an ensemble made from 3 or 4 beam solutions
   was 20% or less.

5. Data were rejected using correlation magnitude, which is the pulse-to-pulse
   correlation (in ping returns) for each depth cell. Correlation magnitude
   represents how the shape of the received signal corresponds to the outgoing
   signal for each ping. If at least three of the beams exhibited a correlation
   magnitude more significant than 64 counts for a given bin, the profile could
   be transformed into earth coordinates. Low correlation magnitudes may
   indicate sudden changes in particle density or sudden changes in ADCP tilt.
   More research is needed at this time into relationships between ADCP tilt
   and correlation magnitude. If any beam had a correlation magnitude of 20
   counts or less, that data point was flagged.

6. Histograms of raw vertical velocity data and partially cleaned data from the
   ADCP ({numref}`figure5.22` and {numref}`figure5.23`) and the WHOTS Data
   Report 1 {cite}`Santiago-Mandujano2007` showed vertical velocities larger
   than expected, some exceeding {math}`1 m s^{-1}`. Recall that the
   instruments’ burst sampling (4-second intervals for the 300 kHz and 2-second
   intervals for the 600 kHz, for 160 seconds every 10 minutes) was designed to
   minimize aliasing by occasional large ocean swell orbital motions
   {ref}`/3_section.md#description-of-whots-{{cookiecutter.current_whots_deployment_number}}-mooring` , and therefore are not
   the source of these speeds in the data. These significant vertical speeds
   are possibly fish swimming in the beams based on the histograms of the
   partially cleaned data; depth cells with an absolute value of vertical
   velocity greater than {math}`0.3 ms^{-1}` were flagged.

   ```{figure} figures/adcp_moored/wh{{cookiecutter.current_whots_deployment_number}}_300_vv_hist.png
   :height: 600px
   :align: center
   :name: figure5.22

   Histogram of the vertical velocity of the 300 kHz ADCP for raw data (top panel)
   and enlarged for clarity (upper middle panel), and partial quality controlled
   data (lower middle panel) and enlarged for clarity (bottom).
   ```

   ```{figure} figures/adcp_moored/wh{{cookiecutter.current_whots_deployment_number}}_600_vv_hist.png
   :height: 600px
   :align: center
   :name: figure5.23

   Same as {numref}`figure5.22`, but for 600kHz ADCP.
   ```

7. A quality control routine known as ‘edgers’ identifies outliers in surface
   bins using a five-point median differencing method. The median velocity from
   surface bins was calculated for each ensemble, and then a five-point running
   median of the surface bin median was calculated. This last median was then
   compared to individual velocity observations in the surface bins, and those
   differing by greater than {math}`0.48 ms^{-1}` were flagged.

8. A 5-pole low pass Butterworth filter with a cutoff frequency of
   {math}`0.25 \frac{cycles}{hour}` was used upon the time-series' length to
   isolate low-frequency flow for each bin independently. The low-frequency
   flow is then subtracted, giving a time series of high-frequency velocity
   component fluctuations for each bin. Data points were considered outliers
   when their values exceeded four standard deviations from the mean (for each
   bin) and were removed.

9. A median residual filter used a 7-point (70 minutes) median differencing
   method to define velocity fluctuations. A 7-point running median is
   calculated for each bin independently, and the result is subtracted out,
   giving time series of variations relative to the running median. Outliers
   higher than four standard deviations from the mean of the 7 points are
   flagged and removed for each bin.

10. Meticulous verification of all the quality control routines was performed
    through visual inspections of the quality-controlled velocity data. Two
    methods were utilized; time-series of u and v components for multiple bins
    were evaluated, and individual vertical profiles. The time-series
    methodology involved inspecting u and v components separately, five bins at
    a time, over 600 ensembles (100 hours). Any instance showing one bin
    behaving erratically from the other four bins was investigated further. If
    it seemed that there could be no reasonable rationale for the erratic
    points from the identified bin, the points were flagged. The intent of the
    inspection of vertical profiles of u and v components was to find entire
    profiles that were not aligned with neighboring profiles. Thirty u and v
    profiles were stacked at a time and were visually inspected for any
    anomalous data.

## Vector Measuring Current Meter (VMCM)

Vector measuring current meters (VMCM) were deployed on the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring at
depths of 10 m and 30 m, serial numbers SN 2042 and 2032, respectively. VMCM
data were processed by the WHOI/UOP group, and the record times are shown
in {numref}`table-22`.

```{table} Record times (UTC mm/dd/yy hh:mm) for the VMCMs at 10 m and 30 m during the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment
:class: sd-m-auto
:align: center
:name: table-22
|  **Time Over**   |  **VMCM (SN 2042)**  |  **VMCM (SN 2032)**  |
|:----------------:|:--------------------:|:--------------------:|
|  **Deployment**  |    10/5/19 19:11     |    10/5/19 18:51     |
|   **Recovery**   |     8/29/21 3:17     |     8/29/21 3:27     |
```

Daily (24 hours) moving averages of quality controlled 600 kHz ADCP data are
compared to VMCM data interpolated to the ADCP ensemble times in the top panels
of {numref}`figure5.24` through {numref}`figure5.27`, and the difference is
shown in the middle panels. The absolute value of the mean difference plus or
minus one standard deviation is shown at the top of the middle panel.
Velocities are not compared if greater than 80% of the ADCP data within a
24-hour average was flagged. The absolute value of mean differences for all
deployments and both velocity components varied between 2 and 3.5
{math}`cm s^{-1}`, with standard deviations between 1.8 and 2.7
{math}`cm s^{-1}`. The VMCM data does not appear to degrade over time for any
deployment. Propeller fouling would dampen measured VMCM velocity magnitudes,
but a decrease in VMCM velocity magnitude than ADCP velocity magnitude with
time is not observed.

```{figure} figures/ngvm_adcp/wh{{cookiecutter.current_whots_deployment_number}}_NGVM_30_U.png
:height: 1000px
:align: center
:name: figure5.24

A comparison of 30 m VMCM and ADCP U velocity for WHOTS-{{cookiecutter.current_whots_deployment_number}}. The top panel shows
24-hour moving averages of VMCM zonal (U) velocity at 30 m depth (red) and ADCP
U velocity from the nearest depth bin to 30 m (30.22 m). The middle panel shows
the U velocity difference, and the bottom panel shows the percentage of ADCP
data within the moving average not flagged by quality control methods.
```

```{figure} figures/ngvm_adcp/wh{{cookiecutter.current_whots_deployment_number}}_NGVM_30_V.png
:height: 1000px
:align: center
:name: figure5.25

Same as in {numref}`figure5.24` but for the meridional (V) velocity component.
```

```{figure} figures/ngvm_adcp/wh{{cookiecutter.current_whots_deployment_number}}_NGVM_10_U.png
:height: 1000px
:align: center
:name: figure5.26

Same as in {numref}`figure5.24` but for the 10 m VMCM.
```

```{figure} figures/ngvm_adcp/wh{{cookiecutter.current_whots_deployment_number}}_NGVM_10_V.png
:height: 1000px
:align: center
:name: figure5.27

Same as {numref}`figure5.26`, but for the meridional (V) velocity component.
```

## Global Positioning System Receiver

Xeos Global Positioning System receiver (Melo-`IMEI:300034012129060`) and
(Rover-`IMEI:300434063359170`) were attached to the buoy's tower
top during the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment
({ref}`/3_section.md#description-of-whots-{{cookiecutter.current_whots_deployment_number}}-mooring`). Data returns from the
receiver were high ({numref}`table-gps`). There was no ARGOS receiver for
WHOTS-{{cookiecutter.current_whots_deployment_number}}.

```{table} GPS record times (UTC mm/dd/yy hh:mm) during WHOTS-{{cookiecutter.current_whots_deployment_number}}
:class: sd-m-auto
:align: center
:name: table-gps
|   **Raw file**   |  **Xeos GPS (Melo)**  |  **Xeos GPS (Rover)**  |
|:----------------:|:---------------------:|:----------------------:|
|  **Start Time**  |     10/6/19 03:07     |     7/30/19 21:01      |
|   **End Time**   |     3/28/20 04:43     |     8/30/21 12:00      |
```

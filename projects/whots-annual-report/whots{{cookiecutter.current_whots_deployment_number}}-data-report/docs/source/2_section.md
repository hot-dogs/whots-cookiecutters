# Description of the WHOTS-{{cookiecutter.current_whots_deployment_number}} Mooring Cruises

## WHOTS-{{cookiecutter.current_whots_deployment_number}} Cruise: WHOTS-{{cookiecutter.current_whots_deployment_number}} Mooring Deployment


The Woods Hole Oceanographic Institution Upper Ocean Processes Group (WHOI/UOP)
, with the UH group's assistance, conducted the {{cookiecutter.current_whots_deployment_number}} deployment of the
WHOTS mooring onboard the {{cookiecutter.current_whots_ship}} during the WHOTS-{{cookiecutter.current_whots_deployment_number}} cruise between
{{ (cookiecutter.current_whots_cruise_start_date|string)[3:-5]}}  {{ (cookiecutter.current_whots_cruise_start_date|string)[:2]}} 
and {{ (cookiecutter.current_whots_cruise_end_date|string)[3:-5]}} {{ (cookiecutter.current_whots_cruise_end_date|string)[:2]}},
{{ (cookiecutter.current_whots_cruise_end_date|string)[-4:]}}. The WHOTS-{{cookiecutter.current_whots_deployment_number}} 
mooring was deployed at Station {{cookiecutter.current_whots_deployment_station}} on 
{{ (cookiecutter.current_whots_deployment_date|string)[3:-5]}} {{ (cookiecutter.current_whots_deployment_date|string)[:2]}},  {{ (cookiecutter.current_whots_deployment_date|string)[-4:]}}, 
{{cookiecutter.current_whots_deployment_time}} UTC at 
{{cookiecutter.current_whots_deployment_anchor_position_latitude}}, {{cookiecutter.current_whots_deployment_anchor_position_longitude}}, 
and the WHOTS-{{cookiecutter.previous_whots_deployment}} mooring were recovered 
on {{ (cookiecutter.previous_whots_recovery_date|string)[3:-5]}} {{ (cookiecutter.previous_whots_recovery_date|string)[:2]}},  {{ (cookiecutter.previous_whots_recovery_date|string)[-4:]}}. 
The scientific personnel that participated during the cruise are listed in 
{numref}`table-1`.

```{table} Scientific personnel on Ship Oscar Sette during the WHOTS-{{cookiecutter.current_whots_deployment_number}} deployment cruise.
:class: sd-m-auto
:align: center
:name: table-1
|           **Name**           |      **Title or function**       | **Affiliation** |
|:----------------------------:|:--------------------------------:|:---------------:|
|      Plueddeman, Albert      |         Chief Scientist          |      WHOI       |
|         Pietro, Ben          |   Senior Engineering Assistant   |      WHOI       |
|       Graham, Raymond        |        Research Associate        |      WHOI       |
|       Maloney, Kelsey        |        Student Assistant         |       UH        |
|       Fitzgerald, Dan        |  Marine Electronics Technician   |       UH        |
|        Rohrer, Tully         |        Research Associate        |       UH        |
| Santiago-Mandujano, Fernando |        Research Associate        |       UH        |
|         Tabata, Ryan         | Research Oceanography Specialist |       UH        |
|         Howins, Noah         |     Undergraduate Volunteer      |       UH        |
|        Pezoa, Sergio         |            Scientist             |      ESRL       |
|        Gonzales, Sean        |     Undergraduate Volunteer      |       HPU       |

```

The UH group conducted the shipboard oceanographic observations during the
cruise. A complete description of these operations is available in the
{cite}`Santiago-Mandujano2021`

A Sea-Bird CTD (conductivity, temperature, and depth) system was used measure
T, S, and O2 profiles during CTD casts. The time, location, and maximum CTD
pressure for each profile are listed in {numref}`table-2`. Eleven CTD casts
were conducted during the WHOTS-{{cookiecutter.current_whots_deployment_number}} cruise. CTD profile data were collected at
Station {{cookiecutter.previous_whots_deployment_station}} (near the WHOTS-{{cookiecutter.previous_whots_deployment}} buoy) 
and Station {{cookiecutter.current_whots_deployment_station}} (near the WHOTS-{{cookiecutter.current_whots_deployment_number}} buoy). 
A test cast was conducted at Station 20 (21°28.164´N, 158°21.552´W) offshore of
Makaha, HI, to an approximate depth of 1500 m to test three acoustic releases (
two to be used in the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring and one backup) were attached to the
rosette frame for function testing. Five CTD yo-yo casts were conducted to
obtain profiles for comparison with subsurface instruments on the WHOTS-{{cookiecutter.current_whots_deployment_number}}
mooring after deployment, and five yo-yo casts were performed for comparison
with the WHOTS-{{cookiecutter.previous_whots_deployment}} mooring before recovery. 
These casts were started less than 0.25 nm from the buoys with varying 
drift during each cast and consisted of 5 up-down cycles between near the 
surface and 218 dbar.

Water samples were taken from all casts; 3 to 4 samples for each of them. These
samples were to be analyzed for salinity at UH and used to calibrate the CTD
conductivity sensors.

```{table} CTD stations occupied during the WHOTS-{{cookiecutter.current_whots_deployment_number}} cruise (Datetime is in mm/dd/yyyy hh:mm)
:class: sd-m-auto
:align: center
:name: table-2
| **Station/cast** |  **Date**  | **In-water Time** |       **Location**        | **Maximum pressure (dbar)** |
|:----------------:|:----------:|:-----------------:|:-------------------------:|:---------------------------:|
|       20/1       | 10/05/2019 |       01:51       | 21°28.164´N, 158°21.552´W |            1502             |
|       52/1       | 10/10/2019 |       16:38       | 22°40.391´N, 157°58.744´W |             215             |
|       52/2       | 10/10/2019 |       19:55       | 22°40.551´N, 157°58.679´W |             211             |
|       52/3       | 10/10/2019 |       23:58       | 22°40.790´N, 157°58.635´W |             211             |
|       52/4       | 10/11/2019 |       04:05       | 22°41.023´N, 157°58.256´W |             211             |
|       52/5       | 10/11/2019 |       07:55       | 22°40.551´N, 157°58.323´W |             209             |
|       50/1       | 10/06/2019 |       16:10       | 22°45.101`N, 157°55.049´W |             213             |
|       50/2       | 10/06/2019 |       20:03       | 22°44.962´N, 157°54.839´W |             211             |
|       50/3       | 10/07/2019 |       00:04       | 22°45.136´N, 157°55.144´W |             218             |
|       50/4       | 10/07/2019 |       04:08       | 22°45.209´N, 157°55.006´W |             211             |
|       50/5       | 10/07/2019 |       07:56       | 22°44.787´N, 157°55.066´W |             210             |
```

Also, continuous ADCP and near-surface thermosalinograph data were obtained
while underway.

The R/V {{cookiecutter.current_whots_ship}} was equipped with a TRDI Ocean Surveyor 75 kHz ADCP,
set to function in broadband and narrowband configurations. The configuration
information is shown in {numref}`table-3`. The ADCP used input from a SAMOS
gyrometer and Furuno GP 150, a GPS receiver, to establish the ship's heading
and attitude.

```{table} Configuration of the Ocean Surveyor 75kHz ADCP on board the Ship Oscar Sette during the WHOTS-{{cookiecutter.current_whots_deployment_number}} cruise
:class: sd-m-auto
:align: center
:name: table-3
|    **Parameters**    | **OS75BB** | **OS75NB** |
|:--------------------:|:----------:|:----------:|
| Sample interval (s)  |    300     |    300     |
|    Number of bins    |     80     |     55     |
|    Bin Length (m)    |     8      |     16     |
| Transducer depth (m) |     5      |     5      |
| Blanking length (m)  |     8      |     8      |
```

Near-surface temperature and salinity data during the WHOTS-{{cookiecutter.current_whots_deployment_number}} cruise were
acquired from the thermosalinograph (TSG) system installed on the NOAA Ship
Oscar Sette. The sensors were sampling water from the continuous seawater
system running through the ship. They comprised one thermosalinograph
model SBE-21 (SN 3168) and a micro-thermosalinograph model SBE-45 (SN 0290),
both with (internal) temperature and conductivity sensors located in the ship’s
chemistry lab, about 70 m from the hull intake; and an SBE-38 (SN 266) external
temperature sensor located at the entrance of the water intake. All instruments
recorded data every second. The water intake is located at the ship's bow,
forward from the starboard side bow thruster at a depth of 3 m. The system has
a flow meter in the chemistry lab, showing a flow rate of about 1.1
liters/minute during the cruise. Only the SBE-45 has a debubbler. Salinity
water samples were taken every 8 hours from the exhaust in the Chemistry lab
using 0.25-liter glass bottles, to be measured in the UH lab to correct any
drift in the thermosalinograph conductivities.

Both thermosalinographs exhibited a number of conductivity and temperature
glitches due to air going into the plumbing. The system had to be secured the
last day of the cruise due to the bad weather because the system kept shutting
down due to air going into the plumbing causing the pumps to stop working. The
temperature differences between the internal SBE-45 and SBE-21 were between 0.2
and 0.4°C and the conductivity differences 17 were nearly 0.05 S/m resulting
in a salinity difference of about 0.28 g/kg. Sensor SBE-21 seems too large as
compared to surface salinity from CTD casts conducted during the cruise. A
diurnal cycle is apparent in the temperature and conductivity.

## WHOTS-{{cookiecutter.next_whots_deployment}} Cruise: WHOTS-{{cookiecutter.current_whots_deployment_number}} Mooring Recovery

The WHOI/UOP Group conducted the mooring turnaround operations during the
WHOTS-{{cookiecutter.next_whots_deployment}} cruise between 
{{ (cookiecutter.next_whots_cruise_start_date|string)[3:-5]}} {{ (cookiecutter.next_whots_cruise_start_date|string)[:2]}}, 
and {{ (cookiecutter.next_whots_cruise_end_date|string)[3:-5]}} {{ (cookiecutter.next_whots_cruise_end_date|string)[:2]}}, {{ (cookiecutter.next_whots_cruise_end_date|string)[-4:]}}.
The WHOTS-{{cookiecutter.next_whots_deployment}} mooring
was deployed at Station {{cookiecutter.next_whots_deployment_station}} on 
{{ (cookiecutter.next_whots_deployment_date|string)[3:-5]}} {{ (cookiecutter.next_whots_deployment_date|string)[:2]}}, {{ (cookiecutter.next_whots_deployment_date|string)[-4:]}}, 
{{cookiecutter.next_whots_deployment_time}} UTC at 
{{cookiecutter.next_whots_deployment_anchor_position_latitude}}, 
{{cookiecutter.next_whots_deployment_anchor_position_longitude}}, 
and the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring was 
recovered on {{ (cookiecutter.current_whots_recovery_date|string)[3:-5]}} {{ (cookiecutter.current_whots_recovery_date|string)[:2]}}, {{ (cookiecutter.current_whots_recovery_date|string)[-4:]}}, 
{{cookiecutter.current_whots_recovery_time}} UTC. The scientific personnel 
that participated during the cruise are listed in
{numref}`table-4`.

```{table} Scientific personnel on Ship Oscar Sette during the WHOTS-{{cookiecutter.next_whots_deployment}} deployment cruise.
:class: sd-m-auto
:align: center
:name: table-4
|           **Name**           |     **Title or function**     | **Affiliation** |
|:----------------------------:|:-----------------------------:|:---------------:|
|      Plueddeman, Albert      |        Chief Scientist        |      WHOI       |
|      Hasbrouck, Emerson      | Senior Engineering Assistant  |      WHOI       |
|       Fitzgerald, Dan        | Marine Electronics Technician |       UH        |
| Santiago-Mandujano, Fernando |      Research Associate       |       UH        |
|      Jackson, Caroline       |       Graduate Student        |       UH        |
|       Maloney, Kelsey        |       Student Assistant       |       UH        |
|        Harris, James         |       Student Assistant       |       HPU       |

```

The UH group conducted the shipboard oceanographic observations during the
cruise. A complete description of these operations is available in the WHOTS-{{cookiecutter.next_whots_deployment}}
cruise report {cite}`Santiago-Mandujano2022`

A Sea-Bird CTD system was used to measure T, S, and O2 profiles during CTD
casts. The time, location, and maximum CTD pressure for each profile are listed
in {numref}`table-5`. Ten CTD casts were conducted during the WHOTS-{{cookiecutter.next_whots_deployment}} cruise,
from  {{ (cookiecutter.next_whots_cruise_start_date|string)[3:-5]}} {{ (cookiecutter.next_whots_cruise_start_date|string)[:2]}}, 
through {{ (cookiecutter.next_whots_cruise_end_date|string)[3:-5]}}  {{ (cookiecutter.next_whots_cruise_end_date|string)[:2]}}, {{ (cookiecutter.next_whots_cruise_end_date|string)[-4:]}}.
CTD profile data were collected at Station 20 (in transit to the WHOTS 
mooring), Station {{cookiecutter.next_whots_deployment_station}} (near the WHOTS-{{cookiecutter.next_whots_deployment}}
buoy), Station {{cookiecutter.current_whots_deployment_station}} (near the WHOTS-{{cookiecutter.current_whots_deployment_number}} buoy), and at Station 2 at the ALOHA site.
The cast at Station 20 was 1508 m deep, and three acoustic releases (two to be
used in the WHOTS-{{cookiecutter.next_whots_deployment}} mooring and one backup) were attached to the rosette frame
for function testing. Five CTD yo-yo casts and one near-bottom CTD cast were
conducted to obtain profiles for comparison with subsurface instruments on the
WHOTS-{{cookiecutter.next_whots_deployment}} mooring after deployment, and two yo-yo casts were conducted for
comparison with the WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring before recovery. The yo-yo casts were
started about 0.25 nm from the buoys with varying drift during each cast, and
consisted of 5 up-down cycles between near the surface and 202 m. One
additional near-bottom CTD cast was conducted at Station ALOHA.

Water samples were taken from all casts; 3 to 4 samples for each of them. These
samples were to be analyzed for salinity at UH and used to calibrate the CTD
conductivity sensors.

```{table} CTD stations during the WHOTS-{{cookiecutter.next_whots_deployment}} cruise (WHOTS-{{cookiecutter.current_whots_deployment_number}} mooring recovery). Datetime is in UTC (mm/dd/yy hh:mm).
:class: sd-m-auto
:align: center
:name: table-5
| **Station/cast** | **Date**  | **In-water Time** |      **Location**       | **Maximum pressure (dbar)** |
|:----------------:|:---------:|:-----------------:|:-----------------------:|:---------------------------:|
|       2/1        | 8/31/2021 |       18:29       | 22°45.12´N, 157°59.98´W |            4796             |
|       20/1       | 8/24/2021 |       23:03       | 21°28.03´N, 158°20.83´W |            1508             |
|       50/1       | 8/29/2021 |       15:59       | 22°45.73´N, 157°55.25´W |             202             |
|       50/2       | 8/29/2021 |       21:55       | 22°46.17´N, 157°54.85´W |             202             |
|       50/3       | 8/29/2021 |       23:52       | 22°46.19´N, 157°54.72´W |             204             |
|       50/4       | 8/30/2021 |       04:02       | 22°45.89´N, 157°54.65´W |             202             |
|       50/5       | 8/30/2021 |       07:57       | 22°44.79´N, 157°54.53´W |             202             |
|       50/6       | 9/1/2021  |       01:36       | 22°44.28´N, 157°54.14´W |            4754             |
|       52/1       | 8/27/2021 |       19:58       | 22°40.69´N, 157°58.38´W |             202             |
|       52/2       | 8/28/2021 |       04:00       | 22°40.67´N, 157°58.73´W |             202             |
```

Also, continuous ADCP and near-surface thermosalinograph data were obtained
while underway.

The NOAA Ship Oscar Sette was equipped with a TRDI Ocean Surveyor 75 kHz ADCP,
set to function in broadband and narrowband configurations. The configuration
information is shown in {numref}`table-6`. The ADCP used input from a SAMOS
gyrometer and Furuno GP 170, a GPS receiver, to establish the ship's heading
and attitude.

```{table} Configuration of the Ocean Surveyor 75kHz ADCP on board the Ship Oscar Sette during the WHOTS-{{cookiecutter.next_whots_deployment}} cruise
:class: sd-m-auto
:align: center
:name: table-6
|    **Parameters**    | **OS75BB** | **OS75NB** |
|:--------------------:|:----------:|:----------:|
| Sample interval (s)  |    300     |    300     |
|    Number of bins    |     80     |     55     |
|    Bin Length (m)    |     8      |     16     |
| Transducer depth (m) |     5      |     5      |
| Blanking length (m)  |     8      |     8      |
```

Near-surface temperature and salinity data during the WHOTS-{{cookiecutter.next_whots_deployment}} cruise were
acquired from the thermosalinograph (TSG) system installed on the NOAA Ship
Oscar Sette. The sensors were sampling water from the continuous seawater
system running through the ship. They comprised of one thermosalinograph model
SBE-21 (SN 3168) and a micro-thermosalinograph model SBE-45 (SN 0290), both
with (internal) temperature and conductivity sensors located in the ship’s
chemistry lab, about 70 m from the hull intake; and an SBE-38 (SN 266) external
temperature sensor located at the entrance of the water intake. All instruments
recorded data every second. The water intake is located at the ship's bow,
forward from the starboard side bow thruster at a depth of 3 m. The system has
a flow meter in the chemistry lab, showing a flow rate of about 1.1
liters/minute during the cruise. Only the SBE-45 has a debubbler. Salinity
water samples were taken every 8 hours from the exhaust in the Chemistry lab
using 0.25-liter glass bottles, to be measured in the UH lab to correct any
drift in the thermosalinograph conductivities.
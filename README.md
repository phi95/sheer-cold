# SheerCold
Freeze your drinks instantly!

This is our project for GSU 2016 Hackathon.

Members:
 - Phi Long Nguyen
 - Khoa Ngo
 - Nghia Le
 - Justin Tumale
 - Dustin Nguyen

## How we came up with the idea?
Well, we all sat down and thought of a problem that we all have and that it is within
our powers to solve it. We concluded that one of the most annoying problem we have is
drinking beers that aren't cold enough. Sometimes after buying a pack, we forgot to put
them in the fridge or the ones we bought aren't cold enough and we really hated waiting
on them to get cold. So we thought it would be cool (no pun intended) to make a machine
that can instantly cool our drinks. Of course we could not work on the actual machine
before hackathon so we made a list of items to bring before hand and also worked on the
design and brought everything with us to assemble.

## Concepts
To create this project we utilized concepts of thermodynamics, heat transfer, electrical
circuits, and material design. The centerpiece of this project is the Peltier module. How
the Peltier module work is that it creates a temperature difference by transferring heat
between two electrical junctions. When current flows through the junctions, heat is removed
from one junction and transferred to the other junction, creating a cooling effect.

## Materials
 - Peltier module (x2)
 - Power cords (x2)
 - Power supply (x2)
 - Thermal paste (x1)
 - Water block (x2)
 - Cold plate mounting (x2)
 - Reservoir (x1)
 - Pump (x1)
 - Aluminum encasement (x1)
 - Radiator (x1)
 - Cooling fans (x3)

## How we did it?
Before the hackathon, we 3D printed the aluminum encasement which perfectly fits a standard sized canned drink. The cold plate and the water block sandwiched the Peltier module, with the cold plate facing the aluminum casing. To manage overheating, we applied thermal paste between the Peltier module and the water block. The water block draws heat from the casing and deposits it towards the water loop, which utilizes a radiator to finally expel heat from the system. A 1000 watt power supply connects to the water cooling system, and must be manually switched on before the system may operate.
The entire machine is located within a plexiglass base.

We programmed an Arduino with sensors to read temperatures of the aluminum casing and broadcast it
onto a computer software we wrote using Python. The Python program included logos and designs we
handmade during the hackathon, an alarm that would ring when the aluminum casing reaches a set amount
of degrees, and a visual graph that allows us to see through time the temperature drop as the machine
is running.

## Problems we encountered
 1. While working on this project we had problems with the water cooling mechanism.
 We realized that the placement of the reservoir matters. We had placed it below the pump
 and water would not pump, due to gravity having a greater force than the pump itself. After
 many trial-and-errors we learned that having the reservoir above the pump allowed water to flow.

 2. This one isn't so much a problem we encountered but rather a design flaw. We realized that
 to run this machine would require a tremendous amount of energy, needing two power supplies.

 3. This one is a software problem that we had. To most of us, we are using completely new software
 along with new hardware. Most of us are learning a new language as well as playing with some new
 hardware so there was definitely a learning curve during the first half of hackathon.

 4. We realized after we finished building the machine that we did not bring a voltage checker,
 therefore we were not able to fine tune the power supply to its optimal level.

## Award
We were awarded best hardware hack.
![award](project-pictures/award.jpg)

## The Process
These are pictures of use tuning the machine
![pic1](project-pictures/pic1.jpg)
![pic2](project-pictures/pic2.jpg)

Here we are taking a break at a local pho restaurant
![pic3](project-pictures/pic3.jpg)

Here is the finish document ready to be presented
![pic4](project-pictures/pic4.jpg)

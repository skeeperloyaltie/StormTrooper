## Storm Trooper Formatter
Create the function reWriteTrooperData that accepts no parameters, reads the data located in the Data file, and prints
- to the console the corresponding data in the format shown on Slide 2 for each line in the Data file.
- The Rendezvous Point for all Stormtroopers is at X:10 Y:10 Z:10
- The ‘Distance to Rendezvous’ is the 3D Euclidean distance from the Stormtrooper to the Rendezvous Point.
- You may, if you desire, programmatically manipulate the data in the Data file, in any intermediate way, and create one or more temporary files to assist you in displaying the correct output.
```Input```
### sample Data.txt
  - ST-1: X60Y31Z2 Sgt
  - ST-2: X32Y43Z5 MSgt
  - ST-3: X29Y79Z3 Sgt
  - ST-4: X13Y51Z8 Cp1
  - ST-5: X57Y52Z0 MSgt

```output``` 
- StormTrooper     X        Y     Z    Rank       DIstamce to Rendezvous
- 1                60      31    2    Sgt         54.82 KM
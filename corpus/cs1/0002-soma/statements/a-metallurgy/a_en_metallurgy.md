# The Great High-Precision Furnace

Welcome to the central refinery! Here we operate the Blast-X9000 Furnace, capable of reaching temperatures of **1538°C** for iron and **1085°C** for copper.

For the production of "Super Alloy Z", the process is extremely delicate. The ambient temperature must be exactly **23°C**, and the relative humidity cannot exceed **45%**. The furnace takes about **40 minutes** to preheat.

The Chief Engineer needs a report on the total load of raw materials. The process involves throwing two types of ore into the furnace. Despite all the complex variables of temperature, pressure (**101.3 kPa**), and cooling time (**12 hours**), Lavoisier's law of conservation of mass still reigns absolute: nothing is lost, everything is transformed.

Your task, amidst all these panel controls and complex sensor readings, is actually quite simple (but don't tell the boss!): we just need to know what the final weight of the mixture will be at the start of the process.

## Input
The furnace system will provide two integer values $X$ and $Y$, representing, respectively, the quantity (in kg) of **Ore A** and **Ore B**. (Ignore the temperature and pressure sensors, they are read by another subsystem).

*Domain: $-10^4 \leq X, Y \leq 10^4$*

## Output
Print a single integer representing the total mass that will be inside the furnace.

## Examples

| Input | Output |
| :--- | :--- |
| 2<br>7 | 9 |

| Input | Output |
| :--- | :--- |
| 10<br>5 | 15 |

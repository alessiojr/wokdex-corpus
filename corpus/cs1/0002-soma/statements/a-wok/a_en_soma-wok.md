# Space Warp Computing

The starship Wok-Enterprise is about to jump to hyperspace. The warp drive operates by bending the fabric of spacetime, creating an Einstein-Rosen bridge.

To calculate the energy required in MegaJoules, the onboard computer needs to sum the relativistic vector distances of two adjacent sectors. Due to time dilation at speeds close to light ($c \approx 3 \times 10^8 m/s$), coordinates may seem confusing, but for this short-range jump, we can ignore the Ricci Tensor and Riemann Curvature.

The Captain only needs the total linear travel distance (Sector X + Sector Y) to authorize ignition. Ignore quantum vacuum fluctuations.

## Input
The computer provides two integer values $X$ and $Y$, representing the light-year distance of the two sectors.
*Domain: $-10^4 \leq X, Y \leq 10^4$*

## Output
A single integer representing the total jump distance.

## Examples
| Input | Output |
| :--- | :--- |
| 2<br>7 | 9 |

| Input | Output |
| :--- | :--- |
| 10<br>5 | 15 |

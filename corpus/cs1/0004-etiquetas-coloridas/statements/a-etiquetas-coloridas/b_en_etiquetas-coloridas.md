# Colorful Cosmic Tags

At the Alpha base in the WOK Universe, astronauts are classifying spatial minerals using tags colored with specific integer numbers. Mapping similar samples is vital to keep the spaceship fueled.

Given a sequence of N collected minerals, where each mineral $i$ has a color tag $C_i$, your task is to write a program that calculates how many distinct pairs of minerals $(i, j)$, with $i < j$, have exactly the same tag color.

## Input

The first line contains an integer N (1 <= N <= 10^5), the total number of minerals.
The second line contains N integers C1, C2, ..., CN (1 <= Ci <= 10^9), representing the color tag of each mineral in collection order.

## Output

Print a single integer indicating the number of pairs of minerals with identically colored tags.

## Constraints

*   1 <= N <= 10^5
*   1 <= Ci <= 10^9

## Examples

### Example 1

| Input         | Output|
| :------------ | :---- |
| 5             | 2     |
| 1 2 1 3 2     |       |

### Example 2

| Input     | Output|
| :-------- | :---- |
| 4         | 6     |
| 1 1 1 1   |       |

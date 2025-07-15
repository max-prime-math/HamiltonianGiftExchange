# Hamiltonian Gift Exchange
This program creates a Hamiltonian cycle for a gift exchange with many people.  Can include pairs of people who don't want to give gifts to each other in the exchange, such as partners, or people who gave gifts to each other last year.  This is nice for large families during holidays where a gift exchange makes more sense than everybody buying for everybody.  A [Hamiltonian cycle](https://en.wikipedia.org/wiki/Hamiltonian_path) is a cycle that visits each vertex exactly once.  This is valuable in this usecase because it means the gift exchange can be done in one big cycle, where Person A gives to Person B, then Person B gives to Person C, until finally the last person gives to Person A.  It also prevents small cycles, such as Person A giving to Person B and Person B giving to Person A.

Feel free to build it yourself, or access it easily using this link.

https://max-prime-math.github.io/HamiltonianGiftExchange/

## Algorithm

1. Build a complete directed graph excluding bad pairs
2. Remove edges based on most recent year’s history
3. Search for Hamiltonian cycles
4. If no cycle found:
   - Restore edges from the previous year and try again
   - If only one cycle exists, restore additional years until more options exist
5. Randomly choose a cycle and display it

## Formatting CSV Files

You can either paste the data into the text boxes or upload CSV files. The expected formats are:

### Names CSV (or textarea)
A single line with comma-separated names:
```
Alice, Bob, Carol, Dave
```
**Notes:**
- No headers
- Order matters: the first name listed will be the starting giver in the cycle

### Bad Pairs CSV (or textarea)
Each line contains two names separated by a comma (giver, receiver). These are disallowed gift pairings:
```
Alice,Bob
Carol,Dave
```
**Notes:**
- Each line goes both ways: neither person will give nor recieve from the other.

### History CSV (or textarea)
Year headers followed by one-way gift pairings for that year:
```
2023
Alice,Bob
Bob,Carol
Carol,Dave
Dave,Alice
2024
Alice,Carol
Carol,Dave
Dave,Bob
Bob,Alice
```
**Notes:**
- Year lines contain just the 4-digit year (with or without a comma)
- Each subsequent line must be a gift pairing for that year
- Each pair is one-way: `Alice,Bob` means Alice gave to Bob

Make sure there are no extra spaces or blank lines at the end of the file for clean parsing.

## Mobile Support

On smaller screens:
- Layout collapses to a single-column view
- Fonts scale up for readability
- Graph and controls remain interactive

## Dark Mode

Toggle dark mode with the button in the top-right corner.

## Downloading Updated History

After generating a new result, click **Download** to export a `history_YYYY.csv` file containing the new year’s updated gift assignments appended to existing history.

## Future Ideas

- Support group exclusions (e.g., "no one from the same household")
- Visualize and explore all possible cycles
- Email or print results directly
- Save/load state from browser localStorage

## Contributions

Contributions, bug reports, and suggestions welcome! Feel free to fork or open an issue.

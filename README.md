# graph-scenario-generator
To generate specific scenarios for some graph database PoC

## Main Idea

I need to populate a graph database in an specific way to test some features.
I imagine it's going to be easier to just program some csv/json generator than
trying to find a dataset that fits my necessities.

Referencing a classic, I'll try to base my naming system off Roller Coaster Tycoon
naming standards, like GuestN and such.

## Stages

- Random people generator (n users)
- Random connection generator (m to n connections per user)
  - randomly inside the range
  - between random users
- event generator
- event association generator
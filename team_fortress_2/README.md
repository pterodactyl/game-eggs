# Team Fortress 2

## From their [Website](https://www.teamfortress.com/)

Team Fortress 2 is a team-based multiplayer first-person shooter developed by Valve. Players choose from nine character classes across game modes like Capture the Flag, Control Point, Payload, and King of the Hill.

## Recommended Server Settings

| RAM | CPU | Storage |
|-----|-----|---------|
| 2-4 GB | 2 Cores | 20 GB |

## Server Ports

TF2 needs 3 ports: a Primary Allocation for the game/RCON port, plus 2 Additional Allocations for the Client and SourceTV ports (set those two variables to match).

| Port | Default | Allocation |
|------|---------|------------|
| **Game/RCON** | **27015** | Primary |
| **Client** | **27005** | Additional |
| SourceTV | 27020 | Additional |

## GSLT

Public servers need a free Game Server Login Token from <https://steamcommunity.com/dev/managegameservers> (pick "Team Fortress 2"), set as the GSLT variable. Without one the server still runs, it just won't show up in the server browser.

## Steam Store Page

https://store.steampowered.com/app/440/Team_Fortress_2/

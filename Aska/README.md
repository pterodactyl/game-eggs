# Aska

Lay claim to unspoiled lands and pave the way for a fierce Viking tribe. Craft the ultimate settlement solo or together with up to x3 friends. Trust in the Gods and the power of the Eye of Odin and summon intelligent NPC villagers to provide camaraderie and relief from the toils of survival

## Server Ports

Aska makes use of a relay service provided by the Photon Fusion middleware. Therefore it doesn't request any ports.

At the time of writing, there were two ports configurable in the server's config file.
- A "steam game port" that the server ignores and doesn't listen on at all.
- A "steam query port" that listens but doesn't appear to respond to any type of traffic.

### Notes

A GSLT (Game Server Login Token) is required for the server to authenticate with the network.
The token needed for authentication is requested here https://steamcommunity.com/dev/managegameservers
For the Aska game (App ID: 1898300)

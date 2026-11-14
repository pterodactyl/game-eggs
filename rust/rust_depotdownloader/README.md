# Rust DepotDownloader

The only aim in Rust is to survive. To do this you will need to overcome struggles such as hunger, thirst and cold. Build a fire. Build a shelter. Kill animals for meat. Protect yourself from other players, and kill them for meat. Create alliances with other players and form a town. Do whatever it takes to survive.

An alternative to the SteamCMD based Rust eggs that installs and updates the server with [DepotDownloader](https://github.com/SteamRE/DepotDownloader) instead of SteamCMD. Useful on hosts where SteamCMD is unreliable.

* The install downloads DepotDownloader into `depotdownloader/` and retries failed Steam downloads automatically.
* Updates on boot still go through the Rust image's entrypoint: the install places a small `steamcmd/steamcmd.sh` script that runs DepotDownloader instead. A failed update never blocks the server from starting. Set `AUTO_UPDATE` to 0 to skip updates.
* `EXTRA_FLAGS` is passed to DepotDownloader on install and on every update, e.g. `-branch staging` to run the staging branch.
* Oxide and Carbon are supported through the `FRAMEWORK` variable, as in the regular Rust egg.

## Minimum RAM warning

The server requires at least 4096MB to run properly.
This is mostly needed for the startup only, once it is running (depending on your world size) it should consume less.

## Server Ports

Ports required to run the server.

| Port    | default |
|---------|---------|
| Game | 28015 UDP |
| Query | 27017 UDP |
| RCON | 28016 TCP |
| Rust+ App | 28082 TCP |

### Information about server updates can be found [here](https://steamdb.info/app/258550/depots/)

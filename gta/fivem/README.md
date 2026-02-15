# FiveM

## Supported architecture

FiveM **ONLY** supports **amd64**. **arm64** is **NOT** supported (like Oracle free cloud)


## Note on FiveM support from Pteroadactyl

Pterodactyl will not be providing support for FiveM. You are free to run a FiveM server but no support will be provided in the Pterodactyl Discord, check the discord annoucement below for details.

Worth a read if you plan on running a FiveM server
[Pterodactyl Discord Announcement](https://discord.com/channels/122900397965705216/124919575534895105/869733533495746560)

## From the [FiveM](https://fivem.net/) Site

FiveM is a modification for Grand Theft Auto V enabling you to play multiplayer on customized dedicated servers.

## Notice

Currently the script can get versions from the builds site.

The `FIVEM_VERSION` variable.

* Defaults to `latest` which is the latest recommended
* Can be set to a specific version Ex. `2431-350dd7bd5c0176216c38625ad5b1108ead44674d`.

The `DOWNLOAD_URL` only needs to be used if they turn on ddos protection. The variable needs to point to a `fx.tar.xz` file as I am too lazy to update the entire script.

## txAdmin

txAdmin is now supported and disabled by default. You set `TXADMIN_ENABLED` to `1` to enable it.

The last update to the egg changes the server to use txadmin to run. On first startup it will print a key to use to sign into the txadmin panel.
> [!WARNING]
> ### Your server will not go online until it's started from txadmin

With latest update see [txAdmin Github](https://github.com/citizenfx/txAdmin/blob/master/docs/env-config.md) some things changed.
For now this is added:
- TXHOST_TXA_PORT (Value can be changed by Admin)
- TXHOST_GAME_NAME (Value can be changed by Admin)
- TXHOST_DATA_PATH (hardcoded to /home/container/txData)
> [!NOTE]
> This Egg can also be used for REDM (Same Framework/Artifact builds/TxAdmin).
>  
> When using this egg for REDM change value of Game name : to redm.
> [!WARNING]
> Reinstall is needed to write the correct values to files for correct functioning
> 
> (if you change Game Name, fivem <-> redm after first install ! )

## Server Ports

Ports required to run the server in a table format.

| Port    | default |
|---------|---------|
| Game    | 30110   |
| Game+1  | 30120   |
| txAdmin | 40120   |

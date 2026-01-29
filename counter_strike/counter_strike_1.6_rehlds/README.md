# Counter-Strike 1.6 ReHLDS

## Description
Counter-Strike 1.6 ReHLDS (Reverse Engineered Half-Life Dedicated Server) is an optimized and updated version of the original HLDS, designed for stability, performance, and security. It provides a modern platform for hosting Counter-Strike 1.6 servers with improved support for custom plugins and modules.

This egg offers everything you need to set up a Counter-Strike 1.6 server using ReHLDS, MetaMod-R, AMX Mod X, and other popular tools.




## System Requirements

| Component    | Minimum             | Recommended        |
|--------------|---------------------|--------------------|
| Processor    | -                   | -                  |
| RAM          | 1 GB                | 2 GB               |
| Storage      | 2 GB                | 5 GB               |


## Server Ports

Ports required to run the server in a table format.

| Port    | default |
|---------|---------|
| Game    | 27015   |
| Source TV | 27020 |
| Client  | 27005   |
| Steam   | 26900   |


27015 is the default port, but any port can be used.
The only required port is the Game port, server can run perfectly fine without other allocations.


## Modules

- **ReHLDS**: Improved performance, crash protection, and extended features.
- **MetaMod-R**: Plugin loader for custom server modifications.
- **AMX Mod X**: Advanced scripting platform for server plugins.
- **ReAPI**: Enhances plugin capabilities with new native functions.
- **ReGameDLL**: Updated game library for improved functionality.
- **Reunion**: A Metamod plugin that allows protocol 47 and 48 non-steam clients to connect to ReHLDS servers


## Notes

- The server installation includes default configuration files such as `server.cfg`, `listip.cfg`, and `banned.cfg`.

For further configuration or plugin information, refer to the official [AMX Mod X documentation](https://amxmodx.org/) or the [ReHLDS GitHub repository](https://github.com/dreamstalker/rehlds).

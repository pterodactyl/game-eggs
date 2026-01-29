# Puck
### Game Description

Hop on your skates and jump into a physics based hockey game. No rules, no timeouts, just get the puck in the goal. May the best team win!

### Usefull links

- Steam: https://steamcommunity.com/app/2994020

### Author & Contributers
| Name        | Github Profile  | Buy me a Coffee |
| ------------- |-------------|-------------|
|   Red-Banana-Official  | https://github.com/Red-Banana-Official | / |
|   Rai68   | https://github.com/rai68 | https://ko-fi.com/rai68 |

### Server Ports

By default Puck requires 2 ports.

| Port    | default       |
|---------|---------------|
|Game    |     7777     |
|Query   |     7778     |


## Configuration

### **Where is the Server Configuration Stored?**
The Puck dedicated server configuration is stored in `server_configuration.json`.

Instead of manually editing this file, **you can set most key values directly in the Pterodactyl Panel** using environment variables.

Name, game phases, mods and admin lists must be edited manually.

---

### **Default Configuration File (`server_configuration.json`)**
On first startup, the server will generate the following structure:

```json
{
  "port": 7777,
  "pingPort": 7778,
  "name": "Pterodactyl Puck Server",
  "maxPlayers": 10,
  "password": "",
  "voip": false,
  "isPublic": true,
  "adminSteamIds": [],
  "reloadBannedSteamIds": false,
  "usePuckBannedSteamIds": true,
  "printMetrics": true,
  "kickTimeout": 300,
  "sleepTimeout": 60,
  "joinMidMatchDelay": 10,
  "targetFrameRate": 120,
  "serverTickRate": 100,
  "clientTickRate": 200,
  "startPaused": false,
  "allowVoting": true,
  "phaseDurationMap": {
    "Warmup": 600,
    "FaceOff": 3,
    "Playing": 300,
    "BlueScore": 5,
    "RedScore": 5,
    "Replay": 10,
    "PeriodOver": 15,
    "GameOver": 15
  },
  "mods": [
    {
      "id": 3493628417,
      "enabled": false,
      "clientRequired": false
    }
  ]
}
```

### Installation/System Requirements

|           | Recommended  | Extra info  |
|-----------|--------------|-------------|
| Processor | Recent x86/64 (AMD/Intel) processor. | You need min 1 Core for the Server. |
| RAM       |  512 MB     |
| Storage   |  1 GB  | 

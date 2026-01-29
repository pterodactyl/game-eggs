# Enshrouded

### Game Description

Enshrouded is a game of survival, crafting, and Action RPG combat, set within a sprawling voxel-based continent. As you journey across the mountains and deserts of an open world, you are free to choose your path and shape your destiny.

Ignite the Ancient power of the Flame, and piece together the fragments of a story that unfolds below the surface.

### Usefull links

- Homepage: https://enshrouded.com/
- Steam: https://store.steampowered.com/app/1203620/Enshrouded/
- Wiki: https://enshrouded.wiki.gg/wiki/Enshrouded_Wiki
- Discord: https://discord.gg/enshrouded

### Author & Contributers
| Name        | Github Profile  | Buy me a Coffee |
| ------------- |-------------|-------------|
|   Red-Banana-Official  | https://github.com/Red-Banana-Official | / |
|   Vapok   | https://github.com/Vapok | https://www.buymeacoffee.com/vapok |
|   QuintenQVD0   | https://github.com/QuintenQVD0 | / |
|   gOOvER   | https://github.com/gOOvER | https://ko-fi.com/B0B351D0Q  |

### Server Ports

By default Enshrouded requires 1 port.

| Port    | default       |
|---------|---------------|
|Game/Query   |     15637     |

## Configuration

### **Where is the Server Configuration Stored?**
The Enshrouded dedicated server configuration is stored in `enshrouded_server.json`, which is automatically managed by this egg.

Instead of manually editing this file, **you can set most key values directly in the Pterodactyl Panel** using environment variables.

---

### **How to Configure the Server**
**Most settings can be modified via Pterodactyl's environment variables.**  
Go to your **Pterodactyl Panel → Server Settings**, where you can edit:
- **Server Name (`SRV_NAME`)** – The name players will see in the server list.
- **User Group Passwords**:
  - **Admin Group (`SRV_PW`)** – Grants admin privileges.
  - **Friend Group (`SRV_PW2`)** – Grants reduced admin privileges.
  - **Guest Group (`SRV_PW3`)** – General access for users.
  - **Visitor Group (`SRV_PW4`)** – Minimal access for visitors.
- **Max Players (`MAX_PLAYERS`)** – Number of player slots (1-16).

Other settings, such as **game settings, IP binding, and log locations**, are still managed in `enshrouded_server.json`

---

### **Default Configuration File (`enshrouded_server.json`)**
On first startup, the server will generate the following structure:

```json
{
    "enableTextChat": false,
    "enableVoiceChat": false,
    "gameSettings": {
        "aggroPoolAmount": "Normal",
        "bossDamageFactor": 1,
        "bossHealthFactor": 1,
        "dayTimeDuration": 1800000000000,
        "enableDurability": true,
        "enableGliderTurbulences": true,
        "enableStarvingDebuff": false,
        "enemyDamageFactor": 1,
        "enemyHealthFactor": 1,
        "enemyPerceptionRangeFactor": 1,
        "enemyStaminaFactor": 1,
        "experienceCombatFactor": 1,
        "experienceExplorationQuestsFactor": 1,
        "experienceMiningFactor": 1,
        "factoryProductionSpeedFactor": 1,
        "foodBuffDurationFactor": 1,
        "fromHungerToStarving": 600000000000,
        "miningDamageFactor": 1,
        "nightTimeDuration": 720000000000,
        "pacifyAllEnemies": false,
        "perkCostFactor": 1,
        "perkUpgradeRecyclingFactor": 0.5,
        "plantGrowthSpeedFactor": 1,
        "playerBodyHeatFactor": 1,
        "playerHealthFactor": 1,
        "playerManaFactor": 1,
        "playerStaminaFactor": 1,
        "randomSpawnerAmount": "Normal",
        "resourceDropStackAmountFactor": 1,
        "shroudTimeFactor": 1,
        "tamingStartleRepercussion": "LoseSomeProgress",
        "threatBonus": 1,
        "tombstoneMode": "AddBackpackMaterials",
        "weatherFrequency": "Normal",
        "playerDivingTimeFactor": 1,
        "fishingDifficulty": "Normal",
        "curseModifier": "Normal"
    },
    "gameSettingsPreset": "Default",
    "ip": "0.0.0.0",
    "logDirectory": "./logs",
    "name": "My Enshrouded Server",
    "queryPort": 15637,
    "saveDirectory": "./savegame",
    "slotCount": 16,
    "tags": [],
    "userGroups": [
        {
            "canAccessInventories": true,
            "canEditBase": true,
            "canExtendBase": true,
            "canKickBan": true,
            "canEditWorld": true,
            "name": "Admin",
            "password": "ChangeMe1",
            "reservedSlots": 0
        },
        {
            "canAccessInventories": true,
            "canEditBase": true,
            "canExtendBase": true,
            "canKickBan": false,
            "canEditWorld": true,
            "name": "Friend",
            "password": "ChangeMe2",
            "reservedSlots": 1
        },
        {
            "canAccessInventories": false,
            "canEditBase": false,
            "canExtendBase": false,
            "canKickBan": false,
            "canEditWorld": false,
            "name": "Guest",
            "password": "ChangeMe3",
            "reservedSlots": 3
        },
        {
            "canAccessInventories": false,
            "canEditBase": false,
            "canExtendBase": false,
            "canKickBan": false,
            "canEditWorld": false,
            "name": "Visitor",
            "password": "ChangeMe4",
            "reservedSlots": 0
        }
    ],
    "bannedAccounts": [],
    "voiceChatMode": "Proximity"
}
```

### Installation/System Requirements

|           | Recommended  | Extra info  |
|-----------|--------------|-------------|
| Processor | Recent x86/64 (AMD/Intel) processor. | You need min 4 Cores for the Server. |
| RAM       |  4-6 GB     |
| Storage   |  30 GB (or more, depending on save size or frequency) |

### Server not showing in Serverlist?

The fact that the server is not displayed in the server list is a known problem.

As a workaround, you can add the server as a favourite via IP:queryport in the Steam server browser.
The server should then be at the top of the ingame server list

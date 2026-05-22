# HumanitZ

## [Documentation](https://store.steampowered.com/app/2728330/HZ_SERVER)

HumanitZ is a co-op, isometric, open world survival game in a world ended by the zombie outbreak. As one of the few human survivors, try to last as long as "humanly" possible. The past can't be changed, but you can make a difference today for the future of humanity.

## Install Notes

This egg provides comprehensive server configuration options for HumanitZ dedicated servers. All server settings can be configured through the Pterodactyl panel interface.

### Features
- Full server customization through environment variables
- RCON support for remote management
- Configurable difficulty settings for zombies, bandits, and animals
- Extensive loot rarity controls
- Weather system customization
- Building and decay mechanics
- Day/night cycle configuration
- Welcome message with color tag support

## Server Ports

| Port       | Default | Protocol |
|------------|---------|----------|
| Game Port  | 7777    | UDP      |
| Query Port | 27015   | UDP      |
| RCON Port  | 8888    | TCP      |

**Note:** The game port can be customized to any available port. RCON is disabled by default and must be enabled in server settings.

## Configuration

### Boolean Values
All boolean settings use numeric values:
- `1` = Enabled/True
- `0` = Disabled/False

### Key Settings

#### Server Identity
- **Server Name**: Display name in the server browser
- **Server Password**: Optional password protection
- **Search ID**: Custom identifier for server grouping (changing hides server from default list)
- **Admin Password**: Use `/adminaccess <password>` in-game for admin privileges

#### Difficulty Settings
Configure zombie, human bandit, and animal difficulty:
- **Health/Speed/Damage**: 0=Very Easy, 1=Easy, 2=Default, 3=Hard, 4=Very Hard, 5=Nightmare
- **Spawn Multipliers**: Adjust population (1=Default, 2=Double, 0.5=Half)
- **Respawn Timers**: Minutes until respawn (0=Disabled)

#### Loot Configuration
- **Rarity Levels**: 0=Scarce, 1=Low, 2=Default, 3=Plentiful, 4=Abundant
- Categories: Food, Drink, Melee, Ranged, Ammo, Armor, Resources, Other
- **Loot Respawn**: Enable/disable with configurable timer (minutes)

#### Survival Mechanics
- **PVP**: Player combat and item interaction
- **Perma Death**: Character loss on death
- **On Death Mode**: What items are lost (0=Nothing → 3=Everything)
- **Vital Drain**: Resource consumption rate (0=Slow, 1=Normal, 2=Fast)

#### World Settings
- **Day/Night Duration**: Real-time minutes for each cycle
- **Seasons**: Starting season and days per season
- **Weather Weights**: Customize spawn probability for each weather type
- **Time Freeze**: Pause time when server is empty

#### Building & Decay
- **Building Health**: Multiplier for player structures
- **Building Decay**: Real-life days until full decay (0=Disabled)
- **Territory Protection**: Prevent building in spawn point areas
- **Dismantle Options**: Allow players to remove their buildings/props

#### Companion Animals
- **Dog Companions**: Enable/disable dog spawns
- **Recruit Dogs**: Allow food-based recruitment
- **Companion Stats**: Health and damage levels (0=Low, 1=Default, 2=High)

### Advanced Options
- **RCON**: Enable remote console for server management and ping display
- **AI Events**: Raid frequency (0=Disabled → 4=Insane)
- **Multiplayer Sleep**: Time advancement when all players sleep
- **Voice Chat**: In-game VoIP communication

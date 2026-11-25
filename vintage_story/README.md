# Vintage Story

## The Vintage Story Server

The server supports mods

Egg supports following branches for server files: [pre](http://api.vintagestory.at/pre.json), [unstable](http://api.vintagestory.at/unstable.json), [stable](http://api.vintagestory.at/stable.json)

### from the developers

Vintage Story is an uncompromising wilderness survival sandbox game inspired by lovecraftian horror themes.
Find yourself in a ruined world reclaimed by nature and permeated by unnerving temporal disturbances.
Relive the advent of human civilization, or take your own path.
New to the game? Make sure to checkout their [starter page](https://wiki.vintagestory.at/index.php?title=Main_Page).

## Server Ports

Vintage Story requires a single port

| Port    | default |
|---------|---------|
| Game    | 42420   |

## Arm64 Nodes

Vintage Story is published for `linux-x64` only. On an arm64 node the install script automatically
replaces `Lib/` and the `VintagestoryServer` host files with the `linux-arm64` build from
[anegostudios/VintagestoryServerArm64](https://github.com/anegostudios/VintagestoryServerArm64),
which is the swap that project's README describes doing by hand. Everything else (`assets/`,
`VintagestoryLib.dll`, `VintagestoryAPI.dll`) is architecture neutral and comes from the official
archive, so both architectures run the same game files.

The `Arm64 build` (`ARM64_RELEASE`) variable selects the release. `auto`, the default, picks the
one matching the installed game's major.minor version - 1.22.6 uses the `1.22.0` release. Set an
exact tag to pin it. The variable is ignored on x86_64 nodes, where the official files are used
unchanged.

Mods that ship native libraries for `linux-x64` only will not work on arm64.

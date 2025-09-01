# mc-server-downloader-py
small python script that downloads a specific minecraft server.jar from mojang or a modloader

This app belongs to [delfi-ch/mc-server-panel](https://github.com/Delfi-CH/mc-server-panel). For a general overview of the project, please look there.

## Building

Linux

```bash
git clone https://github.com/Delfi-CH/mc-server-downloader-py.git

cd mc-server-downloader-py

build.sh
```

Windows

```bash
git clone https://github.com/Delfi-CH/mc-server-downloader-py.git

cd mc-server-downloader-py

build.bat
```

You will find the binary in a "dist" Folder.

## Usage

```
mcsvdl 
-v [Minecraft Server version number, eg. 1.21.6] 
-m [Modloader, accepts: vanilla, fabric, forge, neoforge, papermc, folia] 
-fv [Forge Version, only needed when "-m forge" is used] 
-nfv [NeoForge Version, only needed when "-m neoforge" is used]
```

## Legal

THIS SOFTWARE IS NOT AFFILIATED OR ENDORSED WITH MOJANG AB OR MICROSOFT.

By using this Software you agree to the Minecraft End User License Agreement (EULA).
For more information, please visit https://www.minecraft.net/en-us/eula.

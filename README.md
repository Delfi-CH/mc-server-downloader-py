# mc-server-downloader-py
small python script that downloads a specific minecraft server.jar from mojang

## Building

Install pyinstall

```
pip install pyinstall
```

Building the Project


```
git clone https://github.com/Delfi-CH/mc-server-downloader-py.git

cd mc-server-downloader-py

pyinstaller --onefile --hidden-import=requests main.py --name mcsvdl
```

You will find the binary in a "dist" Folder.

## Usage

```
mcsvdl -v [Minecraft Server version number, eg. 1.21.6]
```

## Legal

THIS SOFTWARE IS NOT AFFILIATED OR ENDORSED WITH MOJANG AB OR MICROSOFT.

By using this Software you agree to the Minecraft End User License Agreement (EULA).
For more information, please visit https://www.minecraft.net/en-us/eula.

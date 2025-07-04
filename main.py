import requests
import argparse
import sys
import re

def download_minecraft_server(version: str):
    output_file = "server.jar"
    manifest_url = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
    manifest = requests.get(manifest_url).json()

    version_info = next((v for v in manifest["versions"] if v["id"] == version), None)
    if not version_info:
        print(f"Version {version} not found.")
        sys.exit(1)

    version_manifest = requests.get(version_info["url"]).json()
    server_jar_url = version_manifest["downloads"]["server"]["url"]

    print(f"Downloading Vanilla Minecraft server {version}...")
    response = requests.get(server_jar_url)
    with open(output_file, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {output_file} for version {version}.")

def download_fabric_server(version: str):
    installer_url = "https://maven.fabricmc.net/net/fabricmc/fabric-installer/1.0.0/fabric-installer-1.0.0.jar"
    output_file = "installer.jar"

    print(f"Downloading Fabric installer for Minecraft {version}...")
    r = requests.get(installer_url)
    if r.status_code != 200:
        print("Failed to download Fabric installer.")
        sys.exit(1)

    with open(output_file, "wb") as f:
        f.write(r.content)

    print(f"Downloaded Fabric installer to {output_file}.")
    print(f"To install the Fabric server, run:")
    print(f"  java -jar {output_file} server -mcversion {version} -dir ./server")

def download_forge_server(minecraft_version: str, forge_version: str):
    
    if minecraft_version == "1.9.4":
        installer_filename = f"installer.jar"
        installer_url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}-{minecraft_version}/forge-{minecraft_version}-{forge_version}-{minecraft_version}-installer.jar"
    elif minecraft_version == "1.8.9":
        installer_filename = f"installer.jar"
        installer_url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}-{minecraft_version}/forge-{minecraft_version}-{forge_version}-{minecraft_version}-installer.jar"
    elif minecraft_version == "1.7.10":
        installer_filename = f"installer.jar"
        installer_url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}-{minecraft_version}/forge-{minecraft_version}-{forge_version}-{minecraft_version}-installer.jar"
    else: 
        installer_filename = f"installer.jar"
        installer_url = f"https://maven.minecraftforge.net/net/minecraftforge/forge/{minecraft_version}-{forge_version}/forge-{minecraft_version}-{forge_version}-installer.jar"

    print(f"Downloading Forge installer for {minecraft_version}-{forge_version} from {installer_url}...")
    r = requests.get(installer_url)
    if r.status_code != 200:
        print(f"Failed to download Forge installer for {forge_version}.")
        sys.exit(1)

    with open(installer_filename, "wb") as f:
        f.write(r.content)

    print(f"Downloaded Forge installer to {installer_filename}.")
    print(f"To install, run: java -jar {installer_filename} --installServer")

def download_neoforge_server(neoforge_version: str):

    installer_filename = f"installer.jar"
    installer_url = f"https://maven.neoforged.net/releases/net/neoforged/neoforge/{neoforge_version}/neoforge-{neoforge_version}-installer.jar"

    print(f"Downloading NeoForge installer for -{neoforge_version} from {installer_url}...")
    r = requests.get(installer_url)
    if r.status_code != 200:
        print(f"Failed to download Forge installer for {neoforge_version}.")
        sys.exit(1)

    with open(installer_filename, "wb") as f:
        f.write(r.content)

    print(f"Downloaded NeoForge installer to {installer_filename}.")
    print(f"To install, run: java -jar {installer_filename} --installServer")

def download_paper_server(version: str):
    output_file = "server.jar"
    print(f"Fetching PaperMC builds for Minecraft {version}...")
    versions_url = "https://api.papermc.io/v2/projects/paper"
    versions_data = requests.get(versions_url).json()

    if version not in versions_data["versions"]:
        print(f"Paper does not support Minecraft version {version}.")
        sys.exit(1)

    builds_url = f"https://api.papermc.io/v2/projects/paper/versions/{version}"
    builds = requests.get(builds_url).json()["builds"]
    latest_build = builds[-1]

    download_url = f"https://api.papermc.io/v2/projects/paper/versions/{version}/builds/{latest_build}/downloads/paper-{version}-{latest_build}.jar"

    print(f"Downloading Paper server build {latest_build} for Minecraft {version}...")
    r = requests.get(download_url)
    with open(output_file, "wb") as f:
        f.write(r.content)
    print(f"Downloaded PaperMC server to {output_file}.")

def download_folia_server(version: str):
    output_file = "server.jar"
    base = "https://api.papermc.io/v2/projects/folia"

    print(f"Fetching Folia versions for Minecraft {version}...")
    versions_data = requests.get(base).json()
    if version not in versions_data["version_groups"]:
        print(f"Folia does not support Minecraft version {version}.")
        sys.exit(1)

    builds_url = f"{base}/version_group/{version}/builds"
    builds_data = requests.get(builds_url).json()
    builds = builds_data.get("builds", [])
    if not builds:
        print(f"No builds found for Folia {version}.")
        sys.exit(1)

    latest_build = builds[-1]["build"]

    build_info_url = f"{base}/versions/{version}/builds/{latest_build}"
    build_info = requests.get(build_info_url).json()
    downloads = build_info.get("downloads", {})
    server_name = downloads.get("application", {}).get("name")
    if not server_name:
        print("Download name not found in build metadata.")
        sys.exit(1)

    download_url = f"{base}/versions/{version}/builds/{latest_build}/downloads/{server_name}"
    print(f"Downloading Folia server (Minecraft {version}, build {latest_build})...")
    r = requests.get(download_url)
    if r.status_code != 200:
        print("Failed to download Folia server jar.")
        sys.exit(1)

    with open(output_file, "wb") as f:
        f.write(r.content)
    print(f"Downloaded Folia server to {output_file}.")


def main():
    parser = argparse.ArgumentParser(description="Download a Minecraft server of a specific type and version.")
    parser.add_argument("--version", "-v", required=True, help="Minecraft version to download")
    parser.add_argument("--type", "-m", dest="server_type", choices=["vanilla", "fabric", "forge", "neoforge", "paper"], default="vanilla", help="Server type to download")
    parser.add_argument("--forge-version","-fv", help="Specific Forge version to download")
    parser.add_argument("--neoforge-version", "-nfv", help="Specific Forge version to download")

    args = parser.parse_args()

    print("DEBUG: parsed args =", args)

    if args.server_type == "vanilla":
        download_minecraft_server(args.version)
    elif args.server_type == "fabric":
        download_fabric_server(args.version)
    elif args.server_type == "forge":
        download_forge_server(args.version, args.forge_version)
    elif args.server_type == "neoforge":
        download_neoforge_server(args.neoforge_version)
    elif args.server_type == "paper":
        download_paper_server(args.version)
    elif args.server_type == "folia":
        download_folia_server(args.version)

if __name__ == "__main__":
    main()

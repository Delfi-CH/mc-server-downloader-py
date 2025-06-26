import requests
import argparse
import sys

def download_minecraft_server(version: str, output_file: str = "server.jar"):
    manifest_url = "https://piston-meta.mojang.com/mc/game/version_manifest_v2.json"
    manifest = requests.get(manifest_url).json()

    version_info = next((v for v in manifest["versions"] if v["id"] == version), None)
    if not version_info:
        print(f"Version {version} not found.")
        sys.exit(1)

    version_manifest = requests.get(version_info["url"]).json()
    server_jar_url = version_manifest["downloads"]["server"]["url"]

    print(f"Downloading Minecraft server {version}...")
    response = requests.get(server_jar_url)
    with open(output_file, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {output_file} for version {version}.")

def main():
    parser = argparse.ArgumentParser(description="Download Minecraft server.jar for a specific version.")
    parser.add_argument("--version", "-v", required=True, help="Minecraft version to download, e.g. 1.20.4")
    args = parser.parse_args()

    download_minecraft_server(args.version)

if __name__ == "__main__":
    main()

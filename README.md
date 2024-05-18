## Introduction
Hello! This project is a Minecraft village generator that I developed with two team members. Our task was to create a generator that produces random paths, houses, and decorations in Minecraft. For this, we used the Minecraft API, which you can reference here:(https://www.stuffaboutcode.com/p/minecraft-api-reference.html).

### Minecraft API Setup and Usage Guide

This README provides detailed instructions on how to set up and use the Minecraft Python API (MCPI) to generate Minecraft houses using the `main.py` script.

### Prerequisites

Ensure you have the following software installed on your system:

1. **Minecraft Java Edition**
2. **Python 3.x**
    - **Windows & MacOS:** Download and install from [python.org](https://www.python.org/). Ensure to check "Add Python to environment variables" during installation.
    - **Linux:** Use your distribution's package manager to install Python.
3. **Visual Studio Code (VS Code)**
    - Download and install from [code.visualstudio.com](https://code.visualstudio.com/).
4. **Java SDK**
    - Download and install the Java SE Development Kit from [oracle.com](https://www.oracle.com/java/technologies/javase-downloads.html). Ensure your Java version is 17 or higher.

### Step-by-Step Setup

#### 1. Install Minecraft Python API

1. Download the pre-configured zip archive for your operating system:
    - [Windows Download](#)
    - [Mac OS Download](#)
    - [Linux Download](#)
2. Unzip the content into a working directory (e.g., `Minecraft_Tools`).
3. Ensure `pip` is installed. If not, install it by following [these instructions](https://pip.pypa.io/en/stable/installation/).
4. Open your command prompt (cmd, terminal, bash, etc.) and navigate to the root of the unzipped directory (e.g., `Minecraft_Tools`).
5. Run the `Install_API` script:
    - **Windows:** Execute `Install_API.bat`.
    - **MacOS/Linux:** Ensure the script is executable: `chmod a+x Install_API.command`. Then run it: `./Install_API.command`.

#### 2. Configure and Run the Spigot Minecraft Server

##### Windows
1. Navigate to the server directory.
2. Run the `start_server.bat` script.

##### MacOS
1. Ensure the `start.command` script is executable: `chmod a+x start.command`.
2. Run the script: `./start.command`.

##### Linux
1. Ensure the `start_server.sh` script is executable: `chmod a+x start_server.sh`.
2. Run the script: `./start_server.sh`.

#### 3. Launch Minecraft

1. Open the Minecraft launcher.
2. Click the "PLAY" button to start the game. Ensure you are running the latest release (e.g., 1.19.4).

#### 4. Join the Local Network Game

1. In Minecraft, go to `Multiplayer`.
2. Join the multiplayer game that appears. If it doesn't appear, click "Direct Connection" and enter `localhost` as the server address.

### Experimenting with the API

1. Open Visual Studio Code.
2. Explore the Python API for Minecraft using the following commands:
    - **Printing "Hello, World!" in chat:**
        ```python
        from mcpi.minecraft import Minecraft
        mc = Minecraft.create()
        mc.postToChat("Hello, World!")
        ```
    - **Teleporting the player:**
        ```python
        mc.player.setTilePos(x, y, z)
        ```
    - **Creating new blocks:**
        ```python
        mc.setBlock(x, y, z, blockType)
        ```

### Running `main.py` to Generate Minecraft Houses

1. Ensure your Minecraft server is running and you are connected.
2. Open the `main.py` script in VS Code.
3. Run the script using the Python interpreter in VS Code.

The `main.py` script will interact with your Minecraft world, generating houses as specified in the code.

### Troubleshooting

- **Java Path Issues:** Ensure your Java installation path is correctly set. Verify by running `java -version` in your command line.
- **Script Execution Permissions:** If you encounter permission issues, ensure scripts are executable using `chmod a+x scriptname`.
- **Server Connection Issues:** Ensure your Minecraft server is running and accessible at `localhost`.

For further assistance, refer to the official documentation and community forums.

Happy coding and building in Minecraft!

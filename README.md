# 🎵 Streamline Your Media: YouTube to MP3 or MP4 in a Snap!

Welcome to the coolest corner of GitHub, where we take the magic of YouTube and turn it into sweet, sweet MP3 or MP4 files for your listening pleasure. Forget those days of keeping a browser tab open just to listen to your favorite tunes or talks. Download once, and it's yours forever!

## What is This Sorcery? 🧙‍♂️

In the beginning, there was chaos. And then came the internet, brimming with endless streams of knowledge, cat videos, and, most importantly, music. But even in this modern Eden, there's a serpent's whisper: "Why can't I keep these divine melodies offline?" Lo! We heard your prayers.

## How to Get Started 🏁

To get your environment set up and running with the Streamline project, please follow these clear and detailed steps:

1. **Clone the Repository**: Begin by cloning the repository to your local machine. Open your terminal (or anaconda prompt) and execute the following command:
   ```
   git clone https://github.com/aditya-xq/streamline.git
   ```
   This command downloads all the project files to a folder named `streamline` on your computer.

2. **Navigate to the Project Folder**: Once cloning is complete, move into the project directory by running:
   ```
   cd streamline
   ```
   This step is essential as all subsequent commands need to be run from within the project's root directory.

3. **Create a New Anaconda Environment**: Before installing the project dependencies, it's a good practice to create a new Anaconda environment. This helps in managing packages and avoiding conflicts between project requirements. Use the following command to create a new environment named `streamline_env` (you can choose a different name if you prefer):
   ```
   conda create --name streamline_env python=3.12
   ```
   After creation, activate the new environment with:
   ```
   conda activate streamline_env
   ```

4. **Install Project Dependencies**: With your Anaconda environment activated, install the necessary project dependencies by running:
   ```
   pip install -r requirements.txt
   ```
   This command reads the `requirements.txt` file in the project directory and installs all the specified Python packages.

5. **Set Up Your Environment Variables**: The project uses an environment file (`.env`) to manage configuration variables such as your desired download folder. Start by renaming the provided example file:
   ```
   mv .env.example .env
   ```
   Then, open the `.env` file in your favorite text editor and fill in the necessary details. The instructions within the file will guide you on what values are needed.

By following these steps, your project environment should be ready for development or usage, with all dependencies installed within a separate Anaconda environment to maintain a clean workspace.

## Summoning the Converter 📣

To transform that video into an MP3/MP4, follow these mystical steps:

1. **Start the app**: `python app.py` and visit `http://localhost:5000` on your favorite browser.
2. **Enter the YouTube URL**: Paste the video link into the cauldron's... um, the webpage's input field.
3. **Choose the download type**: Audio or Video.
4. **Hit 'Convert & Download'**: And watch the magic unfold. 🔮

## Features 🌟

- **User-Friendly Web Interface**: Who says magic can't be modern? Our Flask app makes converting videos a breeze.
- **High-Quality Audio/Video**: Get the best media, short of having the artist perform in your living room.
- **Absolutely Free**: Like the best things in life, our converter doesn't cost a dime or a drachma.

## Contribute to the Magic 🌈

Have a trick up your sleeve? We love pull requests! Share your spells, enhancements, or fixes, and help make this project even more magical. As the Akashic Records grow with collective wisdom, so too can this project with your insights. Together, we shall build the Alexandria Library of sound conversion.

## License 📜

Distributed under the MIT License.

## A Note of Caution ⚠️

This project is for educational purposes only. Please respect copyright laws and YouTube's terms of service.

## Acknowledgments 🎉

- Hat tip to anyone whose code was used
- Endless gratitude to the coffee and pizza that fueled this project
- Special thanks to PyTube and MoviePy for doing the heavy lifting

## Final Words 📢

Go forth and convert. Your music library will thank you. Just remember, with great power comes great responsibility. Use it wisely!

## Overview
This Python script allows you to split a video file into multiple parts based on either a specified number of segments or a specified duration for each segment. It uses FFmpeg to perform the actual video splitting.

## Features
- Split videos by count (number of segments)
- Split videos by duration (length of each segment in minutes)
- Automatically creates an output folder named after the input video
- User-friendly command-line interface

## Requirements
- Python 3.6 or higher
- FFmpeg (must be installed and added to your system PATH)

## Installation
1. Ensure you have Python 3.6 or higher installed on your system.
2. Install FFmpeg:
   - On Windows: Download from the official FFmpeg website and add it to your PATH.
   - On macOS: Use Homebrew: `brew install ffmpeg`
   - On Linux: Use your distribution's package manager, e.g., `sudo apt-get install ffmpeg`
3. Download the `video_splitter.py` script to your local machine.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `video_splitter.py` script.
3. Run the script:
   ```
   python video_splitter.py
   ```
4. Follow the prompts:
   - Enter the path of the original video file
   - Choose the split type (by count or by duration)
   - Enter the split value (number of segments or duration in minutes)

5. The script will create a new folder in the same directory as the input video, named after the input video file. The split video segments will be saved in this folder.

## Example
```
Enter the path of the original video file: /path/to/your/video.mp4
Select split type (1: Split by count, 2: Split by duration in minutes): 1
Enter the split value (count or minutes): 5
Video splitting completed. Output folder: /path/to/your/video
```

## Notes
- The script uses FFmpeg's copy mode (`-c copy`), which is fast but may not be frame-accurate. For more precise splitting, you may need to modify the FFmpeg command in the script.
- Large video files may take a long time to process.
- The script does not perform any video re-encoding, so it maintains the original video quality.

## Troubleshooting
- If you encounter a "command not found" error for FFmpeg, ensure that FFmpeg is properly installed and added to your system PATH.
- Make sure you have write permissions in the directory where you're running the script.

## License
This script is provided "as is", without warranty of any kind. You are free to use and modify it for personal or commercial use.

## Contributing
Contributions, issues, and feature requests are welcome. Feel free to check [issues page] if you want to contribute.

## Acknowledgments
- This script uses FFmpeg, a powerful multimedia framework. Visit [FFmpeg.org](https://ffmpeg.org/) for more information.

import os
import subprocess
from datetime import timedelta

def split_video(input_file, output_folder, split_type, split_value):
    # Get the base name of the input file (without extension)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    
    # Create the output folder
    os.makedirs(output_folder, exist_ok=True)
    
    # Get the duration of the video (in seconds)
    duration = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', input_file]).decode('utf-8').strip())
    
    if split_type == 'count':
        # Split into specified number of parts
        segment_duration = duration / split_value
    elif split_type == 'duration':
        # Split by specified duration in minutes
        segment_duration = split_value * 60
    else:
        raise ValueError("Invalid split_type. Use 'count' or 'duration'.")
    
    # Splitting process
    for i in range(int(duration // segment_duration) + 1):
        start_time = i * segment_duration
        output_file = os.path.join(output_folder, f"{base_name}_part{i+1}.mp4")
        
        cmd = [
            'ffmpeg',
            '-i', input_file,
            '-ss', str(timedelta(seconds=start_time)),
            '-t', str(segment_duration),
            '-c', 'copy',
            output_file
        ]
        
        subprocess.run(cmd, check=True)

def main():
    # Get user input
    input_file = input("Enter the path of the original video file: ")
    
    # Set output folder (original video folder/original video name)
    base_dir = os.path.dirname(input_file)
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_folder = os.path.join(base_dir, base_name)
    
    # Select split type
    while True:
        split_type_input = input("Select split type (1: Split by count, 2: Split by duration in minutes): ")
        if split_type_input in ['1', '2']:
            break
        print("Invalid input. Please enter 1 or 2.")
    
    split_type = 'count' if split_type_input == '1' else 'duration'
    
    # Input split value
    while True:
        try:
            split_value = int(input("Enter the split value (count or minutes): "))
            if split_value > 0:
                break
            print("Please enter a value greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Execute video splitting
    try:
        split_video(input_file, output_folder, split_type, split_value)
        print(f"Video splitting completed. Output folder: {output_folder}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()

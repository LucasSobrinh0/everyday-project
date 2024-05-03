import tkinter as tk  # Import the tkinter module for GUI
from tkinter import filedialog  # Import filedialog submodule from tkinter
from moviepy.editor import VideoFileClip  # Import VideoFileClip class from moviepy.editor


# Function to convert video to GIF
def convert_to_gif():
    # Retrieve input values from entry fields
    input_video = entry_video.get()
    output_path = entry_output.get()
    output_filename = entry_filename.get()
    duration = entry_duration.get()

    # Construct the full path for the output file
    output_gif = f"{output_path}/{output_filename}.gif" if output_filename else f"{output_path}/output.gif"

    try:
        duration = float(duration) if duration else None  # Convert duration to float if not None

        if input_video and output_path and output_filename:
            clip = VideoFileClip(input_video)  # Load the input video
            clip = clip.subclip(0, duration) if duration else clip  # Extract a subclip if duration is provided
            clip.write_gif(output_gif, fps=10)  # Write the GIF file
            label_status.config(text="Conversion completed!")  # Update status label
        else:
            label_status.config(text="Please fill in all required fields.")  # Prompt to fill all fields
    except Exception as e:
        label_status.config(text=f"Error converting: {str(e)}")  # Display error message if conversion fails


# Function to browse and select input video file
def browse_video():
    filename = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])  # Open file dialog
    if filename:
        entry_video.delete(0, tk.END)  # Clear any existing text in entry field
        entry_video.insert(0, filename)  # Insert selected file path into entry field


# Function to browse and select output directory
def browse_output():
    directory = filedialog.askdirectory()  # Open directory selection dialog
    if directory:
        entry_output.delete(0, tk.END)  # Clear any existing text in entry field
        entry_output.insert(0, directory)  # Insert selected directory path into entry field


# Initialize the GUI window
root = tk.Tk()
root.title("Video to GIF Converter")  # Set window title

# Create GUI widgets
label_video = tk.Label(root, text="Input Video:")  # Label for input video
entry_video = tk.Entry(root, width=50)  # Entry field for input video path
button_browse_video = tk.Button(root, text="Browse", command=browse_video)  # Button to browse input video

label_output = tk.Label(root, text="Output GIF Directory:")  # Label for output directory
entry_output = tk.Entry(root, width=50)  # Entry field for output directory path
button_browse_output = tk.Button(root, text="Browse", command=browse_output)  # Button to browse output directory

label_filename = tk.Label(root, text="GIF Filename:")  # Label for GIF filename
entry_filename = tk.Entry(root, width=50)  # Entry field for GIF filename

label_duration = tk.Label(root, text="GIF Duration (in seconds):")  # Label for GIF duration
entry_duration = tk.Entry(root, width=10)  # Entry field for GIF duration

button_convert = tk.Button(root, text="Convert to GIF", command=convert_to_gif)  # Button to trigger conversion
label_status = tk.Label(root, text="")  # Label to display conversion status

# Organize widgets in the window using grid layout
label_video.grid(row=0, column=0, sticky="w")  # Grid placement for input video label
entry_video.grid(row=0, column=1)  # Grid placement for input video entry field
button_browse_video.grid(row=0, column=2)  # Grid placement for browse button

label_output.grid(row=1, column=0, sticky="w")  # Grid placement for output directory label
entry_output.grid(row=1, column=1)  # Grid placement for output directory entry field
button_browse_output.grid(row=1, column=2)  # Grid placement for browse button

label_filename.grid(row=2, column=0, sticky="w")  # Grid placement for GIF filename label
entry_filename.grid(row=2, column=1)  # Grid placement for GIF filename entry field

label_duration.grid(row=3, column=0, sticky="w")  # Grid placement for GIF duration label
entry_duration.grid(row=3, column=1)  # Grid placement for GIF duration entry field

button_convert.grid(row=4, column=0, columnspan=3)  # Grid placement for convert button spanning 3 columns
label_status.grid(row=5, column=0, columnspan=3)  # Grid placement for status label spanning 3 columns

# Run the main event loop
if __name__ == "__main__":
    root.mainloop()

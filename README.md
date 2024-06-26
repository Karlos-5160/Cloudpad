# Cloudpad
Your own fully customizable Text Editor, now say bye bye to that old vintage style Notepad <br>
CloudPad is a simple, lightweight fully customizable text editor created using Python and Tkinter. It serves as an alternative to Notepad, providing text editing functionalities in a user-friendly interface.

## Features

- Open and edit text files
- Save text files
- Font customization (Style, Size, Color)
- undo redo functionality
- Lightweight and fast
- Comes with wide variety of inbuilt Themes
- Search Functionality
- Find and replace Functionality
- Status Bar customization
- Zoom In/Out
- Help Functionality

## Installation

### Prerequisites

- Python 3.x
- Tkinter (usually included with standard Python installations)

### Running from Source

1. Clone the repository:
   ```bash
   git clone https://github.com/Karlos-5160/Cloudpad.git
   cd Cloudpad
2. Run the application
     python CloudPad.py

## Creating an Executable
  To create an executable file (for Windows), you can use py2exe or PyInstaller. Below are the instructions for using PyInstaller.
  1. Install PyInstaller:
      pip install pyinstaller
  2. Create the executable:
      pyinstaller --onefile --noconsole --add-data "cloudpad.ico;." CloudPad.py
  3. The executable will be created in the dist folder.   
### Usage
Open CloudPad by running CloudPad.py or the generated executable. <br>
• Use the File menu to open or save text files.  <br>
• Use the Edit menu for basic text editing operations.
• Use the View menu to zoom in/ zoom out and toggle status bar
• Use the Font menu to customize font(style,size,color)
• Use the BG menu to change background color of the window
• Use the Theme menu to change the theme, there are many innovative inbuilt themes available
• USe the Help menu to get help and get about info

### Icon Not Found Error
  If you encounter an error related to the icon file (cloudpad.ico), ensure that:  <br>
    -The icon file is present in the same directory as CloudPad.py.  <br>
    -The path to the icon file is correctly referenced in the code.
  
## Antivirus Issues
  If the executable is flagged by antivirus software, consider:  <br>
    -Adding an exception in your antivirus software for the executable or the containing folder.  <br>
    -Signing the executable with a trusted certificate.
    
## Contributing
  If you'd like to contribute to CloudPad, please fork the repository and submit a pull request. Issues and feature requests can be reported in the GitHub Issues section.

## License
  This project is licensed under the © Karlos License. See the LICENSE file for more details.

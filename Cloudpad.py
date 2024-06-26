from tkinter import *
import tkinter.messagebox as tmsg
import tkinter as tk
import pyperclip
from tkinter import font

# Global Variables
texts = None
search_index = None
fontsize = 25
Zoom = 100
status_bar = None

# main Function 
def main(content=None):
    
    global texts, root, search_index, fontsize, Zoom, status_bar_visible, status_bar  # Declaring texts, root, and search_index as global variables

    status_bar_visible = True  # Tracking the visibility of the status bar
    
    if root:
        root.destroy()  # Closing previous main window if it exists
        
    search_index = None  # Initializing search_index as None
    Zoom = 100 # Initializing Zoom as 100
    fontsize = 25  # Initializing Default font size as 25
        
    root = Tk() # Creating the root window
    root.geometry("950x650")
    
    try:
        root.iconbitmap('cloudpad.ico')  
    except tk.TclError as e:
        print(f"Error: {e}. Icon not found or invalid.")
        
    root.title("Cloudpad")
    
    ############################################################# Writing functions for the file menubar 
    def window():
        if num_chars>0:
            ask = tmsg.askyesno('Save', 'Would you like to Save ?')
            if ask==True:
                save()
            else:
                pass
        else:
            pass
        
        main()
        
    def openn():
        win = Toplevel()  # for secondary windows we are using Top class instead of making  a new instrance of Tk class
        win.geometry("315x130")
        
        try:
            root.iconbitmap('cloudpad.ico')  
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
        
        win.title("Open")
        
        opun = StringVar()

        frame = Frame(win)
        frame.grid()
        
        Label(frame, text="Open file", font="Bear 15").grid(row=1, column=1, padx=10, pady=10)
        Entry(frame, textvariable=opun, width=12, font="Bear 15").grid(row=1, column=2)
        
        def open_file():
            global root
            filename = opun.get()
            try:
                with open(f'{filename}') as f:
                    content = f.read()
                win.destroy()
                main(content=content)
                # root.quit()  # Close the previous window
                # root = None  # Reset root to None after quitting
                
                
            except FileNotFoundError:
                # error_win = Toplevel()
                # error_win.title("Error")
                # Label(error_win, text="File not found!").pack(padx=10, pady=10)
                # Button(error_win, text="OK", command=error_win.destroy).pack(pady=5)
                tmsg.showerror('File Error', 'No such file in the Directory')

        Button(frame, text="Open", font="Bear 10", command=open_file, pady=5, padx=5, borderwidth=10, width=18).grid   (row=2, columnspan=2, column=2, pady=15)
    
    def save():
        with open('sample.txt', 'w') as f:
            f.write(texts.get(1.0, END))
        tmsg.showinfo('File', 'Saved Succesfully!')
        
        
    def saveas():
        win2 = Toplevel()  # for secondary windows we are using top class instead of making  a new instrance of Tk class
        win2.geometry("290x130")
        
        try:
            root.iconbitmap('cloudpad.ico') 
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
        
        win2.title("Save As")
        
        typeas = StringVar()
        
        frame = Frame(win2)
        frame.grid()
        
        Label(frame, text="Save as", font="Bear 15").grid(row=1, column=1, padx=10, pady=10)
        Entry(frame, textvariable=typeas, width=12, font="Bear 15").grid(row=1, column=2)

        def save_as_file():
            filename = typeas.get()
            if filename:
                with open(filename, 'w') as f:
                    f.write(texts.get(1.0, END))
                win2.destroy()
                tmsg.showinfo('File', 'Saved Succesfully!')
                
        Button(frame, text="Save", font="Bear 10", command=save_as_file, pady=5, padx=5, borderwidth=10, width=18).grid (row=2, columnspan=2, column=2, pady=15)
        
    def print():
        tmsg.showerror('Error', 'No Printer Found!')
        
        
#######################################################################################################################################################################################
#######################################################################################################################################################################################        
    ############################################################# Writing functions for the Edit menubar 
    def cut_text():
        take = texts.get(1.0, END)
        texts.delete(1.0, END)
        pyperclip.copy(take)
        
    def copy_text():
        take = texts.get(1.0, END)
        pyperclip.copy(take)
        
    def paste_text():
        global texts
        data = pyperclip.paste()
        texts.insert(END, data)
        
    def delete_text():
        texts.delete(1.0, END)
        
    def Undo():
        try:
            texts.edit_undo()
        except:
            tmsg.showinfo('Error', 'Cannot Undo')

    def Redo():
        try:
            texts.edit_redo()
        except:
            tmsg.showinfo('Error', 'Cannot Redo')
        
    def find_text():
        def find():
            text_to_find = find_entry.get()
            start_pos = texts.search(text_to_find, '1.0', END)
            if start_pos:
                end_pos = f"{start_pos}+{len(text_to_find)}c"
                texts.tag_add('found', start_pos, end_pos)
                texts.tag_config('found', background='yellow', foreground='black')
                texts.mark_set(INSERT, end_pos)
                texts.see(INSERT)
            else:
                tmsg.showinfo("Result", "Text not found")

        def find_next():
            text_to_find = find_entry.get()
            global search_index
            if search_index:
                start_pos = texts.search(text_to_find, search_index, END)
            else:
                start_pos = texts.search(text_to_find, '1.0', END)
            if start_pos:
                end_pos = f"{start_pos}+{len(text_to_find)}c"
                texts.tag_remove('found', '1.0', END)
                texts.tag_add('found', start_pos, end_pos)
                texts.tag_config('found', background='yellow', foreground='black')
                search_index = end_pos
                texts.mark_set(INSERT, end_pos)
                texts.see(INSERT)
            else:
                tmsg.showinfo("Result", "No more matches found")

        def find_previous():
            text_to_find = find_entry.get()
            global search_index
            if search_index:
                start_pos = texts.search(text_to_find, '1.0', search_index)
            else:
                start_pos = texts.search(text_to_find, '1.0', END)
            if start_pos:
                end_pos = f"{start_pos}+{len(text_to_find)}c"
                texts.tag_remove('found', '1.0', END)
                texts.tag_add('found', start_pos, end_pos)
                texts.tag_config('found', background='yellow', foreground='black')
                search_index = start_pos
                texts.mark_set(INSERT, start_pos)
                texts.see(INSERT)
            else:
                tmsg.showinfo("Result", "No more matches found")

        def replace_text():
            text_to_find = find_entry.get()
            replacement_text = replace_entry.get()
            content = texts.get('1.0', END)
            new_content = content.replace(text_to_find, replacement_text)
            texts.delete('1.0', END)
            texts.insert('1.0', new_content)

        win8 = Toplevel()
        win8.geometry("370x210")
        
        try:
            root.iconbitmap('cloudpad.ico')  
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
        
        win8.title("Find")

        find_label = Label(win8, text="Find:", font="Bear 15")
        find_label.grid(row=0, column=0, padx=10, pady=5)
        find_entry = Entry(win8, width=25)
        find_entry.grid(row=0, column=1, padx=10, pady=5)

        replace_label = Label(win8, text="Replace:", font="Bear 15")
        replace_label.grid(row=1, column=0, padx=10, pady=5)
        replace_entry = Entry(win8, width=25)
        replace_entry.grid(row=1, column=1, padx=10, pady=5)

        find_button = Button(win8, text="Find", borderwidth=8,  font="Bear 15", command=find)
        find_button.grid(row=2, column=0, padx=10, pady=5)
        find_next_button = Button(win8, text="Find Next", borderwidth=8,  font="Bear 15",  command=find_next)
        find_next_button.grid(row=2, column=1, padx=10, pady=5)
        find_previous_button = Button(win8, text="Find Previous", borderwidth=8,  font="Bear 15", command=find_previous)
        find_previous_button.grid(row=3, column=0, padx=10, pady=5)
        replace_button = Button(win8, text="Replace", font="Bear 15", borderwidth=8,  command=replace_text)
        replace_button.grid(row=3, column=1, padx=10, pady=5)
        
        
#######################################################################################################################################################################################
#######################################################################################################################################################################################

    ############################################################# Writing functions for the View menubar 
    def zoom_in():
        global fontsize, Zoom
        fontsize += 5
        texts.config(font=("Bear", fontsize))
        Zoom+=25
        update_status_bar()

    def zoom_out():
        global fontsize, Zoom
        fontsize -= 5
        texts.config(font=("Bear", fontsize))
        if Zoom > 0:
            Zoom -= 25
        update_status_bar()
        
        
    def update_status_bar(event=None):
        if status_bar:
            global num_chars
            content = texts.get(1.0, END)
            num_chars = len(content) - 1  # Subtract 1 to exclude the last newline character added by Tkinter
            num_lines = int(texts.index('end-1c').split('.')[0])
            status_bar.config(text=f"Chars: {num_chars}  Lines: {num_lines}  {Zoom}% || Windows  UTF-8")
        
    def show_status_bar():
        global status_bar_visible
        if status_bar_visible:
            status_bar.pack_forget()  # Hide the status bar
            status_bar_visible = False
        else:
            status_bar_visible = True
            status_bar.pack(side=BOTTOM, fill=X)  # Show the status bar
            # update_status_bar()
            
    
#######################################################################################################################################################################################
#######################################################################################################################################################################################    
    ############################################################# Writing functions for the Font menubar 
    def change_font(font_name):
        texts.config(font=(font_name, 25))
        
        
    def font_style():
        win3 = Toplevel()
        win3.geometry("400x400")
        
        try:
            root.iconbitmap('cloudpad.ico')  
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
        
        win3.title('Font Style')
        canvas = Canvas(win3)
        scrollbar = Scrollbar(win3, orient=VERTICAL, width=30)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        frame = Frame(canvas)
        
        font_list = [ 'Arial', 'Courier New', 'Comic Sans MS', 'Fixedsys', 'MS Serif', 'Symbol', 'Times New Roman', 'Helvetica', 'Verdana', 'System' 'WST_Swed', 'Marlett', 'Arial Greek', 'Arial Black', 'Bahnschrift', 'Bahnschrift SemiBold', 'Bahnschrift Light SemiCondensed', 'Bahnschrift SemiLight SemiConde', 'Bahnschrift SemiCondensed', 'Bahnschrift SemiBold SemiConden', 'Bahnschrift Light Condensed', 'Bahnschrift SemiLight Condensed', 'Bahnschrift Condensed', 'Bahnschrift SemiBold Condensed', 'Calibri', 'Calibri Light', 'Cambria', 'Cambria Math', 'Candara', 'Candara Light', 'Consolas', 'Constantia', 'Corbel', 'Corbel Light', 'Courier New Baltic', 'Courier New CE', 'Courier New CYR', 'Courier New Greek', 'Courier New TUR', 'Ebrima', 'Franklin Gothic Medium', 'Gabriola', 'Gadugi', 'Georgia', 'Impact', 'Ink Free', '', 'Bodoni MT Poster Compressed', 'Bookman Old Style', 'Bradley Hand ITC', 'Britannic Bold', 'Berlin Sans FB', 'Berlin Sans FB Demi']
        
        for font_name in font_list:
            btn = Button(frame, text=font_name, borderwidth=8, font="Bear 12", fg="black", command=lambda f=font_name: change_font(f))
            btn.pack(side=TOP, padx=10, pady=5)
        
        canvas.create_window((0, 0), window=frame, anchor='nw')
        canvas.update_idletasks()
        
        canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)
        canvas.pack(fill=BOTH, expand=True)
        scrollbar.config(command=canvas.yview)
        
    def update_font(font_size):
        global fontsize
        texts.config(font=("Bear", font_size))
        fontsize = font_size

    def font_size():
        win4 = Toplevel()
        win4.geometry("500x300")
        
        try:
            root.iconbitmap('cloudpad.ico')  
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
            
        win4.title("Font Size")
        frame = Frame(win4)
        Label(frame, font = "Bear 25", text="Font Size select").pack(side=TOP, padx=10, pady=10)
        myslider = Scale(frame, from_=10, to=80, font = "Bear 15", orient=HORIZONTAL, length=400, tickinterval=10, width=30)
        myslider.set(25)
        myslider.pack(padx=5, pady=10)
        Button(frame, borderwidth=8, font = "Bear 15", text="Resize", pady=5, command=lambda: update_font(myslider.get())).pack(pady=15)
        frame.pack()
        
    def white():
        texts.config(fg=("white"))
        
    def black():
        texts.config(fg=("black"))
        
    def red():
        texts.config(fg=("red"))
        
    def yellow():
        texts.config(fg=("yellow"))
        
    def blue():
        texts.config(fg=("blue"))
        
    def green():
        texts.config(fg=("green"))
        
    def violet():
        texts.config(fg=("violet"))
        
    def cyan():
        texts.config(fg=("cyan"))
        
    def orange():
        texts.config(fg=("orange"))
        
    def purple():
        texts.config(fg=("purple"))
        
    def white():
        texts.config(fg=("white"))
        
    def black():
        texts.config(fg=("black"))
        
#######################################################################################################################################################################################
    def white_bg():
        texts.config(bg=("white"))
        
    def black_bg():
        texts.config(bg=("black"))
        
    def red_bg():
        texts.config(bg=("red"))
        
    def yellow_bg():
        texts.config(bg=("yellow"))
        
    def blue_bg():
        texts.config(bg=("blue"))
        
    def green_bg():
        texts.config(bg=("green"))
        
    def violet_bg():
        texts.config(bg=("violet"))
        
    def cyan_bg():
        texts.config(bg=("cyan"))
        
    def orange_bg():
        texts.config(bg=("orange"))
        
    def purple_bg():
        texts.config(bg=("purple"))

    def font_color():
        win5 = Toplevel()
        win5.geometry("420x650")
        
        try:
            root.iconbitmap('cloudpad.ico')  
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
        
        win5.title("Font Color")
        Label(win5,text="Select Font Color", font = "Bear 20").pack(side=TOP, fill=Y)
        Button(win5,text="White", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="white", fg="black", command=white).pack(pady=5, side=LEFT)
        Button(win5,text="Black", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="black", fg="white", command=black).pack(pady=5, side=RIGHT)
        frame = Frame(win5)
        Button(win5,text="Red", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="red", fg="white", command=red).pack(pady=5, )
        Button(win5,text="Yellow", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="#e6e600", fg="white", command=yellow).pack(pady=5, )
        Button(win5,text="Blue", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="blue", fg="white", command=blue).pack(pady=5)
        Button(win5,text="Green", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="green", fg="white", command=green).pack(pady=5)
        Button(win5,text="Violet", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="violet", fg="white", command=violet).pack(pady=5)
        Button(win5,text="Cyan", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="cyan", fg="white", command=cyan).pack(pady=5)
        Button(win5,text="Orange", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="orange", fg="white", command=orange).pack(pady=5)
        Button(win5,text="Purple", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="purple", fg="white", command=purple).pack(pady=5)
        frame.pack()
        
        
#######################################################################################################################################################################################
#######################################################################################################################################################################################        
    ############################################################# Writing functions for the BG menubar 
    def bg_color():
        win6 = Toplevel()
        win6.geometry("600x430")
        
        try:
            root.iconbitmap('cloudpad.ico') 
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
        
        win6.title("Background Color")
        Label(win6,text="Select Background Color", font = "Bear 20").pack(side=TOP, fill=Y)
        Button(win6,text="Red", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="red", fg="white", command=red_bg).pack(pady=5, side=LEFT, fill=X)
        Button(win6,text="Yellow", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="#e6e600", fg="white", command=yellow_bg).pack(pady=5, side=RIGHT)
        Button(win6,text="Blue", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="blue", fg="white", command=blue_bg).pack(pady=5, side=LEFT)
        Button(win6,text="Green", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="green", fg="white", command=green_bg).pack(pady=5, side=RIGHT)
        Button(win6,text="Violet", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="violet", fg="white", command=violet_bg).pack(pady=5)
        Button(win6,text="Cyan", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="cyan", fg="white", command=cyan_bg).pack(pady=5)
        Button(win6,text="Orange", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="orange", fg="white", command=orange_bg).pack(pady=5)
        Button(win6,text="Purple", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="purple", fg="white", command=purple_bg).pack(pady=5)
        Button(win6,text="Black", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="black", fg="white", command=black_bg).pack(pady=5, side=RIGHT)
        Button(win6,text="White", font = "Bear 15",borderwidth=10, pady=5, padx=5, bg="white", fg="black", command=white_bg).pack(pady=5, side=LEFT)
        
        
#######################################################################################################################################################################################
#######################################################################################################################################################################################

    ############################################################# Writing functions for the Theme menubar 
    def cloudy():
        texts.config(bg="#2398c3", fg="#FFFFFF", font="Bear 25")
        
    def light_forest():
        texts.config(bg="#34a203", fg="#c1d11f", font="Bear 25")
        
    def dark_forest():
        texts.config(bg="#1e7743", fg="#c1d11f", font="Bear 25")
        
    def dust():
        texts.config(bg="#e69900", fg="#FFFFFF", font="Bear 25")
        
    def mist():
        texts.config(bg="#66b3ff", fg="#004080", font="Bear 25")
        
    def fire():
        texts.config(bg="#ff5a00", fg="#ffce00", font="Bear 25")
        
    def water():
        texts.config(bg="#2389da", fg="#C4BCA7", font="Bear 25")
        
    def mountain():
        texts.config(bg="#993333", fg="#ff9966", font="Bear 25")
        
    def rain():
        texts.config(bg="#3c5369", fg="#f6d9d5", font="Bear 25")
        
    def uganda():
        texts.config(bg="#18da8d", fg="#FFFFFF", font="Bear 25")
        
    def vibrant():
        texts.config(bg="#cc3399", fg="#00ffcc", font="Bear 25")
        
    def sunset():
        texts.config(bg="#ff901f", fg="#ffff1a", font="Bear 25")
        
    def light():
        texts.config(bg="#FFFFFF", fg="black", font="Bear 25")
        
    def dark():
        texts.config(bg="black", fg="#FFFFFF", font="Bear 25")
        
    def hidden():
        texts.config(bg="#FFFFFF", fg="#FFFFFF", font="Bear 25")
        tmsg.showwarning('Warning', 'This Theme is not recommended for beginners it is only for Advanvced Coders who can type at 300 wpm without seeing the Keyboard')
        tmsg.showinfo('I am Blind', 'Press (Ctrl + A) Everytime you wanna see the text and then to Hide it again, press left/right Arrow')
        
        
#######################################################################################################################################################################################
#######################################################################################################################################################################################        
    ############################################################# Writing functions for the help menubar 
    def help():
        tmsg.showinfo('Help', 'We will be happy to help you sir')
        tmsg.showinfo('Help', 'Please kindly mail us on cloudpad@gmail.com about the issue you are facing')

    def rate_us():
        reply = tmsg.askquestion('Rate Us', 'Was your experience Good with the App?')
        while(reply!='yes'):
            reply = tmsg.askquestion('Rate Us', 'Was your experience Good with the App?')
            
        tmsg.showinfo('Rate Us', 'Thanks for the feedback!')
        
    def about():
        win7 = Toplevel()
        win7.geometry("650x670")
        
        try:
            root.iconbitmap('cloudpad.ico')  
        except tk.TclError as e:
            print(f"Error: {e}. Icon not found or invalid.")
        
        win7.title("About")
        frame = Frame(win7)
        Label(frame, text="About", font="Bear 25", fg="#ff5a00").pack(side=TOP, pady=5, padx=5)
        texts2 = Text(frame, width=400, height=800, wrap=WORD, font="Bear 15", fg="#2398c3", borderwidth=5, padx=5, pady=5)
        texts2.insert(1.0, """Cloudpad Version: 1.1.2\nRelease Date: 26-06-2024 \n
        It's your own Text editor fully customizable and gives a fresh feel unlike your average Notepad with that boring vintage GUI. \n
        Features:\n
        1. Create and Edit Text Files\n
        2. Save Files with Different Names\n
        3. Print Option\n
        4. Cut, Copy, Paste, Delete Text\n
        5. Undo Redo Functionality\n
        6. Font customization (Style, Size, Color)\n
        7. Comes with wide variety of inbuilt Themes\n
        8. Background(BG) customization\n
        9. Search Functionality\n
        10. Find and replace Functionality\n
        11. Status Bar customization\n
        12. Zoom In/Out\n
        13. AutoSave\n
        14. Help Functionality\n\n
        Developer: Karlos\n
        Email: cloudpad@gmail.com\n
        GitHub: https://github.com/Karlos-5160\n
        """)
        texts2.pack(fill=BOTH, expand=TRUE, padx=10, pady=10)
        frame.pack() 


#######################################################################################################################################################################################
#######################################################################################################################################################################################

    ############################################################# Defining menubar
    menubar = Menu(root) 

    file = Menu(menubar, tearoff=0, font="Bear 10", fg="#2389da")
    file.add_command(label="New Window", command=window)
    file.add_command(label="Open", command=openn)
    file.add_command(label="Save", command=save)
    file.add_command(label="Save as", command=saveas)
    file.add_separator()
    file.add_command(label="Print", command=print)
    file.add_command(label="Close Window", command=exit)
    file.add_command(label="Exit", command=exit)

    edit = Menu(menubar, tearoff=0, font="Bear 10", fg="#2389da")
    edit.add_command(label="Cut", command=cut_text)
    edit.add_command(label="Copy", command=copy_text)
    edit.add_command(label="Paste", command=paste_text)
    edit.add_command(label="Delete", command=delete_text)
    edit.add_command(label="Undo", command=Undo)
    edit.add_command(label="Redo", command=Redo)
    edit.add_separator()
    edit.add_command(label="Find", command=find_text)
    edit.add_command(label="Find next", command=find_text)
    edit.add_command(label="Find Previous", command=find_text)
    edit.add_command(label="Replace", command=find_text)

    view = Menu(menubar, tearoff=0, font="Bear 10", fg="#2389da")
    view.add_command(label="Zoom in", command=zoom_in)
    view.add_command(label="Zoom out", command=zoom_out)
    view.add_command(label="Status Bar", command=show_status_bar)
    
    font_menu = Menu(menubar, tearoff=0, font="Bear 10", fg="#2389da")
    font_menu.add_command(label="Font style", command=font_style)
    font_menu.add_command(label="Font size", command=font_size)
    font_menu.add_command(label="Font Color", command=font_color)
    
    bg_colors = Menu(menubar, tearoff=0, font="Bear 10", fg="#2389da")
    bg_colors.add_command(label="Background color", command=bg_color)
    
    theme = Menu(menubar, tearoff=0, font="Bear 10")
    theme.add_command(label="cloudy (default)", foreground="#2398c3", command=cloudy)
    theme.add_command(label="light forest", foreground="#34a203", command=light_forest)
    theme.add_command(label="Dark forest", foreground="#1e7743", command=dark_forest)
    theme.add_command(label="Dusty", foreground="#e69900", command=dust)
    theme.add_command(label="Misty", foreground="#66b3ff", command=mist)
    theme.add_command(label="Fire", foreground="#ff5a00", command=fire)
    theme.add_command(label="Water", foreground="#2389da", command=water)
    theme.add_command(label="Mountain", foreground="#993333", command=mountain)
    theme.add_command(label="Rainy", foreground="#3c5369", command=rain)
    theme.add_command(label="Uganda", foreground="#18da8d", command=uganda)
    theme.add_command(label="Vibrant", foreground="#cc3399", command=vibrant)
    theme.add_command(label="Sunset", foreground="#ff901f", command=sunset)
    theme.add_command(label="light", foreground="black", command=light)
    theme.add_command(label="Dark", foreground="black", command=dark)
    theme.add_command(label="Hidden", foreground="#FFFFFF", command=hidden)
    
    help_menu = Menu(menubar, tearoff=0, font='Bear 10', fg="#2389da")
    help_menu.add_command(label="Help", command=help)
    help_menu.add_command(label="Rate Us", command=rate_us)
    help_menu.add_command(label="About Cloudpad", command=about)

    root.config(menu=menubar)
    
    menubar.add_cascade(label="File", menu=file)
    menubar.add_cascade(label="Edit", menu=edit)
    menubar.add_cascade(label="View", menu=view)
    menubar.add_cascade(label="Font", menu=font_menu)
    menubar.add_cascade(label="BG", menu=bg_colors)
    menubar.add_cascade(label="Theme", menu=theme)
    menubar.add_cascade(label="Help", menu=help_menu)
    
    # menubar.config(font=("Bear", 10))
    # menubar.config(bg = "GREEN",fg='white',activebackground='red',activeforeground='pink',relief=FLAT)

    ############################################### Creating  a scrollbar for our text area
    scrollbar = Scrollbar(root, width=30)
    scrollbar.pack(side=RIGHT, fill=Y)

    ############################################### Creating a text area using Text Widget
    texts = Text(root, bg="#2398c3", height=1000, fg="#FFFFFF", font=("Bear", fontsize), yscrollcommand = scrollbar.set, padx=10, pady=10, undo=True)
    # statusbar = Label(root, textvariable=char,  relief=SUNKEN, anchor="w", padx=8, pady=3)
    # statusbar.pack(side=BOTTOM, fill=X)
    
    ############################################### Adding a status bar at the bottom of our text Area
    status_bar = Label(root, text=f" Initializing... Chars: 0  Lines: 0  {Zoom}%  || Windows  UTF-8", anchor=E, fg="#2389da", padx=5, pady=5, font=("Bear", 15))
    status_bar.pack(side=BOTTOM, fill=X)

    texts.bind('<KeyRelease>', update_status_bar)
    texts.bind('<ButtonRelease>', update_status_bar)
    texts.pack(fill=BOTH, expand=True)
    scrollbar.config(command=texts.yview)
    
    if content: #If content is provided, insert it into texts widget
        texts.delete(1.0, END) #clear existing content if available
        texts.insert(1.0, content)  # Insert content if provided
    
    root.mainloop()
    
    ###################################################################################################################################################################################
    ###################################################################################################################################################################################
    
############################################################# main function calling()
if __name__ == "__main__": 
    root = None  # Initializing root as None initially
    main()

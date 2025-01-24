import tkinter
import pyshorteners


root = tkinter.Tk()
root.title('Url Shortener')
root.geometry("300x300")

def shorten():
	shortener = pyshorteners.Shortener()
	short_url = shortener.tinyurl.short(long_url_entry.get())
	short_url_entry.insert(0, short_url)

long_url_label = tkinter.Label(root, text="Enter the long Url",padx=10,pady=10) 
long_url_entry = tkinter.Entry(root)
long_url_label.pack(), long_url_entry.pack()

short_url_label = tkinter.Label(root, text="Output of the short Url",padx=10,pady=10) 
short_url_entry = tkinter.Entry(root)
short_url_label.pack(), short_url_entry.pack()

output_button = tkinter.Button(root, text="Click the button to submit", padx=10,pady=10, command=shorten)
output_button.pack()

root.mainloop()
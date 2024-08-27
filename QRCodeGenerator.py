from tkinter import *
from PIL import Image as PilImage, ImageTk
import qrcode

# Create the main application window
app = Tk()
app.title("QR Code Generator")
app.geometry("1000x600")
app.config(bg="#0080ff")

# Set the application icon
image_icon=PhotoImage(file="icon.png")
app.iconphoto(False, image_icon)

def generate():
    # Retrieve and clean input values
    name = title.get()
    text = url.get()

      # Check if either field is empty
    if not name or not text:
        error_label.config(text="Title and URL cannot be empty.")
        return
    
    # Generate the QR code and save it as a PNG file
    qr = qrcode.make(text)
    qr.save(f"{name}.png")

    try:
        # Open the saved image using PIL
        pil_image = PilImage.open(f"{name}.png")
        # Convert the PIL image to a Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(pil_image)
        # Update the label to display the QR code image
        image_view.config(image=tk_image)
        image_view.image = tk_image  # Keep a reference to avoid garbage collection
        error_label.config(text="QR Code generated successfully!")
    except Exception as e:
        # Display an error message if something goes wrong
        error_label.config(text=f"Error: {e}")

# Create a label for displaying the QR code image
image_view=Label(app, bg="grey")
image_view.pack(padx=50, pady=50, side=RIGHT)

# Create and place a label and entry for the QR code title
Label(app, text="Title", font="arial 15 bold", bg="#0080ff").place(x=40, y=80)
title = Entry(app, width=25, font="arial 15")
title.place(x=150, y=80)

# Create and place a label and entry for the URL
Label(app, text="URL", font="arial 15 bold", bg="#0080ff").place(x=40, y=120)
url = Entry(app, width=25, font="arial 15")
url.place(x=150, y=120)

# Create and place a button to generate the QR code
Button(app, text="Generate QR Code", width=18, height=2, bg="red", fg="white", font="arial 15 bold", command=generate).place(x=150, y=170)

# Create and place a label for displaying error messages
error_label = Label(app, text="", font="arial 19 bold", bg="#0080ff", fg="white")
error_label.place(x=80, y=250)

# Start the Tkinter event loop
app.mainloop()
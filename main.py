from PIL import ImageDraw, ImageFont
import PIL.Image
from tkinter import *
from tkinter import filedialog


# Add text function to an image
def add_text():
    image_URL = open_file()
    img = PIL.Image.open(image_URL)
    draw = ImageDraw.Draw(img)

    # Use Damion Google font
    font = ImageFont.truetype("fonts/Damion-Regular.ttf", 100)

    # User's text to add
    text = text_entry.get()
    draw.text((2, 2), text, font=font)

    # Edited filename
    new_name = output_image_name_entry.get()

    img.show()
    img.save(new_name)


# Select file function. It works inside add_text() function and return image url.
def open_file():
    result = filedialog.askopenfile(initialdir='/', title='Select file to ad a watermark',
                                    filetypes=(('JPEG Image', '.jpg'), ('all files', '*.*')))
    image_URL = result.name
    print(image_URL)
    return image_URL


# ---------------------------------------- UI Setup ----------------------------------------
window = Tk()
window.title("Image Watermark")
window.config(padx=50, pady=50)

# Logo
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_image = PhotoImage(file='images/logo_size.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
enter_text_label = Label(text="Enter a text to add: ", font=('Roboto', 18))
enter_text_label.grid(row=2, column=0)
output_image_name_label = Label(text="Enter a new name of the image: ", font=('Roboto', 18))
output_image_name_label.grid(row=3, column=0)

# Buttons
add_watermark_btn = Button(text="Add watermark", width=17, height=2, font=('Roboto', 18), command=add_text)
add_watermark_btn.grid(row=4, column=1)

# Entries
text_entry = Entry(width=20)
text_entry.grid(row=2, column=1)
output_image_name_entry = Entry(width=20)
output_image_name_entry.grid(row=3, column=1)
output_image_name_entry.insert(END, string='.jpg')

window.mainloop()
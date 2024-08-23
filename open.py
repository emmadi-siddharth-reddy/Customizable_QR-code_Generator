import tkinter as tk
from PIL import ImageTk, Image
import front1 as f1
import front2 as f2

root = tk.Tk()
root.title("Welcome")
root.geometry("720x720")
# Load images
image1 = Image.open("type1.png")
image2 = Image.open("type2.png")

# Resize images if necessary
image1 = image1.resize((250, 250))
image2 = image2.resize((250,250))

# Convert images to Tkinter PhotoImage
photo1 = ImageTk.PhotoImage(image1)
photo2 = ImageTk.PhotoImage(image2)
frame = tk.Frame(root)

# Create the buttons
button1 = tk.Button(frame, image=photo1, command=lambda: f1.Front1(),bg="#00FFFF")
button2 = tk.Button(frame, image=photo2, command=lambda: f2.Front2(),bg="#00FFFF")

# Pack the buttons in the frame
button1.pack(side=tk.LEFT, padx=10,pady=30)
button2.pack(side=tk.LEFT, padx=10,pady=30)

frame.pack(anchor=tk.CENTER)

# Add text labels
label1 = tk.Label(root, text="Click on the type of QR-code you want to generate from the above choices to create your Customized QR",bg="#E8D579")
label2 = tk.Label(root, text="A QR code (Quick Response code) is a type of two-dimensional matrix barcode.",bg="#E8D579")
label1.pack(padx=2,pady=3)
label2.pack(padx=2,pady=3)

root.config(background="grey")
root.mainloop()
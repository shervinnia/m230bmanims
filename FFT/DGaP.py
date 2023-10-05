import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
import numpy as np
from numpy.fft import fft2, fftshift

def draw_shape(img_draw, shape, num_x, num_y, spacing_x, spacing_y, size):
    # Define border offset
    border_offset = 10
    
    # Calculate total width and height occupied by shapes and spacings
    total_width = num_x * size + (num_x - 1) * spacing_x
    total_height = num_y * size + (num_y - 1) * spacing_y
    
    # Calculate starting point to center shapes
    start_x = (512 - total_width) // 2
    start_y = (512 - total_height) // 2
    
    # Ensure that shapes are within the border
    start_x = max(start_x, border_offset)
    start_y = max(start_y, border_offset)
    
    for y in range(num_y):
        for x in range(num_x):
            pos_x = start_x + x * (spacing_x + size)
            pos_y = start_y + y * (spacing_y + size)
            
            # Check if shape will be within border
            if pos_x + size + border_offset <= 512 and pos_y + size + border_offset <= 512:
                if shape == "Circle":
                    img_draw.ellipse((pos_x, pos_y, pos_x + size, pos_y + size), fill='white')
                elif shape == "Square":
                    img_draw.rectangle((pos_x, pos_y, pos_x + size, pos_y + size), fill='white')
                elif shape == "Triangle":
                    img_draw.polygon([pos_x, pos_y, pos_x + size, pos_y, pos_x + size // 2, pos_y + size], fill='white')
                elif shape == "Hexagon":
                    img_draw.polygon([
                        pos_x + size // 2, pos_y, pos_x + size * 3 // 2, pos_y,
                        pos_x + size * 2, pos_y + size, pos_x + size * 3 // 2, pos_y + size * 2,
                        pos_x + size // 2, pos_y + size * 2, pos_x, pos_y + size
                    ], fill='white')

def update_all(event=None):
    shape = shape_var.get()
    num_x = num_x_slider.get()
    num_y = num_y_slider.get()
    spacing_x = spacing_x_slider.get()
    spacing_y = spacing_y_slider.get()
    size = size_slider.get()
    
    img_pil = Image.new("RGB", (512, 512), 'black')
    img_draw = ImageDraw.Draw(img_pil)
    
    draw_shape(img_draw, shape, num_x, num_y, spacing_x, spacing_y, size)
    
    img_tk = ImageTk.PhotoImage(image=img_pil)
    shape_canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)
    shape_canvas.image = img_tk

    # Convert to grayscale NumPy array
    img_np = np.array(img_pil.convert('L'))
    
    # Calculate FFT
    f_transform = fft2(img_np)
    f_transform_shifted = fftshift(f_transform)
    f_transform_magnitude = np.abs(f_transform_shifted)
    magnitude_spectrum = 20 * np.log(f_transform_magnitude + 1e-5)
    magnitude_spectrum = np.uint8(255 * (magnitude_spectrum - np.min(magnitude_spectrum)) / (np.max(magnitude_spectrum) - np.min(magnitude_spectrum)))

    # Apply zoom to FFT image
    zoom_level = zoom_slider.get()
    center_x, center_y = 512 // 2, 512 // 2
    cropped_size = int(512 / zoom_level)
    x1 = max(center_x - cropped_size // 2, 0)
    x2 = min(center_x + cropped_size // 2, 512)
    y1 = max(center_y - cropped_size // 2, 0)
    y2 = min(center_y + cropped_size // 2, 512)
    cropped_fft = magnitude_spectrum[y1:y2, x1:x2]

    # Resize cropped image back to original size
    img_zoomed_fft = Image.fromarray(cropped_fft).resize((512, 512), Image.NEAREST)
    
    img_tk = ImageTk.PhotoImage(image=img_zoomed_fft)
    fft_canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)
    fft_canvas.image = img_tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Diffraction Gratings and Patterns by Ambarneil Saha and Shervin Nia")

    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    shape_var = tk.StringVar()
    shape_var.set("Circle")

    shape_menu = ttk.OptionMenu(main_frame, shape_var, "Circle", "Square", "Triangle", "Hexagon")
    shape_menu.grid(row=0, column=0, sticky=tk.W)

    shape_canvas = tk.Canvas(main_frame, bg='white', width=512, height=512)
    shape_canvas.grid(row=1, column=0, padx=5, pady=5)

    fft_canvas = tk.Canvas(main_frame, bg='white', width=512, height=512)
    fft_canvas.grid(row=1, column=1, padx=5, pady=5)

    num_x_slider = tk.Scale(main_frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Num X")
    num_x_slider.grid(row=2, column=0, sticky=tk.W)
    num_x_slider.set(5)

    num_y_slider = tk.Scale(main_frame, from_=1, to=20, orient=tk.HORIZONTAL, label="Num Y")
    num_y_slider.grid(row=3, column=0, sticky=tk.W)
    num_y_slider.set(5)

    spacing_x_slider = tk.Scale(main_frame, from_=0, to=50, orient=tk.HORIZONTAL, label="Spacing X")
    spacing_x_slider.grid(row=4, column=0, sticky=tk.W)
    spacing_x_slider.set(10)

    spacing_y_slider = tk.Scale(main_frame, from_=0, to=50, orient=tk.HORIZONTAL, label="Spacing Y")
    spacing_y_slider.grid(row=5, column=0, sticky=tk.W)
    spacing_y_slider.set(10)

    size_slider = tk.Scale(main_frame, from_=10, to=100, orient=tk.HORIZONTAL, label="Size")
    size_slider.grid(row=6, column=0, sticky=tk.W)
    size_slider.set(40)

    zoom_slider = tk.Scale(main_frame, from_=1, to=5, orient=tk.HORIZONTAL, label="Zoom", resolution=0.1)
    zoom_slider.grid(row=7, column=0, sticky=tk.W)
    zoom_slider.set(1)

    for widget in [num_x_slider, num_y_slider, spacing_x_slider, spacing_y_slider, size_slider, zoom_slider]:
        widget.bind("<Motion>", update_all)


    shape_var.trace_add("write", update_all)

    update_all()

    root.mainloop()

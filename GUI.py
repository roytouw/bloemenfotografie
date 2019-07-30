import matplotlib
import tkinter as tk
# import _thread
# import time
import json
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from tkinter import filedialog
from crop_foto import crop_image

matplotlib.use('Agg')


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        # self.root.geometry('800x600')
        self.root.title("Automatische Bloemenfotografie")
        self.imagePanel = tk.Label(self.root)
        self.imagePanel.pack(side="top", expand="yes")
        self.config_btn = tk.Button(self.root, text="Instellingen",
                                    command=self.create_window)
        self.config_btn.pack(side="top", fill="none", expand="yes")
        with open('config.json', 'r') as crop_config:
            self.data = json.load(crop_config)
        self.root.attributes("-fullscreen", True)

    def __del__(self):
        self.root.quit()

    def set_image(self, image):
        img = ImageTk.PhotoImage(image)
        self.imagePanel.config(image=img)
        self.imagePanel.image = img

    def create_window(self):
        config_window = tk.Toplevel(self.root)
        config_window.geometry('800x600')
        config_window.title("Instellingen")

        lbl_frame = tk.Frame(config_window)
        lbl_frame.pack(side="left", fill="both", expand="yes")

        fields_frame = tk.Frame(config_window)
        fields_frame.pack(side="right", fill="both", expand="yes")

        padding_lbl = tk.Label(lbl_frame, text="Padding in pixels")
        padding_lbl.pack(side="top", fill="both")
        padding_field = tk.Spinbox(fields_frame, from_=0, to=100, width=21)
        padding_field.pack(side="top")

        threshold_value_lbl = tk.Label(lbl_frame, text="Precentage kleur "
                                                       "verschil met "
                                                       "achtergrond")
        threshold_value_lbl.pack(side="top")
        threshold_field = tk.Spinbox(fields_frame, from_=0, to=100, width=21)
        threshold_field.pack(side="top")

        fust_color_lbl = tk.Label(lbl_frame, text="Fust kleur")
        fust_color_lbl.pack(side="top")
        fust_rgb_frame = tk.Frame(fields_frame)
        fust_rgb_frame.pack(side='top')
        fust_color_lbl_red = tk.Label(fust_rgb_frame, text='R:')
        fust_color_lbl_red.pack(side='left')
        fust_color_field_red = tk.Spinbox(fust_rgb_frame, from_=0, to=255,
                                          width=7)
        fust_color_field_red.pack(side='left')
        fust_color_lbl_green = tk.Label(fust_rgb_frame, text='G:')
        fust_color_lbl_green.pack(side='left')
        fust_color_field_green = tk.Spinbox(fust_rgb_frame, from_=0, to=255,
                                            width=7)
        fust_color_field_green.pack(side='left')
        fust_color_lbl_blue = tk.Label(fust_rgb_frame, text='B:')
        fust_color_lbl_blue.pack(side='left')
        fust_color_field_blue = tk.Spinbox(fust_rgb_frame, from_=0, to=255,
                                           width=7)
        fust_color_field_blue.pack(side='left')

        color_differentiation_lbl = tk.Label(lbl_frame,
                                             text="Precentage verschil in "
                                                  "fust kleur"
                                             )
        color_differentiation_lbl.pack(side="top")
        cdf_percentage_conversion = self.data['crop_config'][
                                        'color_differentiation'] * 100
        color_differentiation_field = tk.Spinbox(fields_frame, from_=
                                                 cdf_percentage_conversion,
                                                 to=100, width=21)
        color_differentiation_field.pack(side="top")

        current_selection = 'Huidige geselecteerde aspect ratio: {0}'.format(
            ':'.join(str(e) for e in self.data['crop_config']['ratio']))
        ratio_lbl = tk.Label(lbl_frame, text=current_selection)
        ratio_lbl.pack(side="top")
        ratio_field = Combobox(fields_frame, state='readonly')
        ratio_field['values'] = ('1:1', '3:2', '4:3')
        ratio_field.pack(side="top")

        network_folder_lbl = tk.Label(lbl_frame, text="Netwerk opslag locatie")
        network_folder_lbl.pack(side="top")
        network_folder_btn = tk.Button(fields_frame, text='Selecteer '
                                                          'opslag',
                                       command=self.choose_dir)
        network_folder_btn.pack(side='top')

        test_button = tk.Button(lbl_frame, text='test_btn',
                                command=self.crop_img)
        test_button.pack(side="top")

    def crop_img(self):
        test_name = "fust_bloemen.png"
        Image.open(test_name)
        img_cropped = crop_image(test_name)
        img = Image.open(img_cropped)
        img_resized = img.resize((800, 800), Image.ANTIALIAS)
        self.set_image(img_resized)

    def choose_dir(self):
        dirname = filedialog.askdirectory()
        save_loc = self.data['crop_config']['network_folder']
        # todo save location in config.json

    def show_location(self):
        pass

    def print_locatie(self):
        pass

    def save_config(self):
        pass

# def test(gui):
#     time.sleep(2)
#     new_image = Image.open("imgs/fust.jpg")
#     new_image = new_image.resize((400, 400), Image.ANTIALIAS)
#     gui.set_image(new_image)
#     time.sleep(2)
#     new_image = Image.open("imgs/fust2.jpg")
#     new_image = new_image.resize((400, 400), Image.ANTIALIAS)
#     gui.set_image(new_image)


# if __name__ == "__main__":
#     gui = GUI()
#     # _thread.start_new_thread(test, (gui, ))
#     _thread.start_new_thread(gui.root.mainloop(), ())

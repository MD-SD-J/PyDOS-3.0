#imports
import tkinter as tk
from tkinter import messagebox
import webbrowser
import subprocess
import platform
import tkinter.simpledialog
import os



class DesktopApp:
    def __init__(self, master):
        self.master = master
        master.title("Desktop with Apps")

        # Make the desktop fullscreen
        self.master.attributes('-fullscreen', True)

        # Canvas for the desktop
        self.canvas = tk.Canvas(master, bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # List to store app, file, and folder items
        self.desktop_items = []

        # Load images for app icons
        computer_img = tk.PhotoImage(file="computer.png")
        pip_installer_img = tk.PhotoImage(file="pip_installer.png")
        my_local_network_img = tk.PhotoImage(file="local_network.png")
        system_center_img = tk.PhotoImage(file="system_center.png")
        google_icon_img = tk.PhotoImage(file="google_icon.png")
        settings_img = tk.PhotoImage(file="settings.png")

        # Add apps to the desktop
        self.add_desktop_item("Computer", computer_img)
        self.add_desktop_item("Pip Installer", pip_installer_img)
        self.add_desktop_item("My Local Network", my_local_network_img)
        self.add_desktop_item("System Center", system_center_img)
        self.add_desktop_item("Google.com", google_icon_img)
        self.add_desktop_item("Settings", settings_img)

        # Bind drag-and-drop events
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonRelease-1>", self.drop)

    def add_desktop_item(self, item_name, icon_image):
        # Add an app to the desktop
        item = {"name": item_name, "icon": icon_image, "x": 0, "y": 0, "width": 100, "height": 100}
        self.desktop_items.append(item)
        self.update_desktop()

    def update_desktop(self):
        # Update the desktop to show apps, files, and folders
        self.canvas.delete("all")  # Clear the canvas

        # Organize items in a grid layout
        num_cols = 20
        col_width = self.canvas.winfo_width() // num_cols
        row_height = 100

        for i, item in enumerate(self.desktop_items):
            col = i % num_cols
            row = i // num_cols
            x = col * col_width
            y = row * row_height
            item["x"] = x
            item["y"] = y
            self.canvas.create_image(x + col_width // 2, y + row_height // 2, image=item["icon"],
                                     tags=(item["name"], "item"))
            self.canvas.create_text(x + col_width // 2, y + row_height + 20, text=item["name"],
                                    tags=(item["name"], "item"))

    def drag(self, event):
        # Handle dragging of items on the desktop
        x, y = event.x, event.y
        selected_item = self.canvas.find_withtag(tk.CURRENT)
        if selected_item:
            item_name = self.canvas.gettags(selected_item[0])[0]
            for item in self.desktop_items:
                if item["name"] == item_name:
                    item["x"] = x - item["width"] // 2
                    item["y"] = y - item["height"] // 2
                    break
            self.update_desktop()

    def drop(self, event):
        # Handle dropping of items on the desktop
        selected_item = self.canvas.find_withtag(tk.CURRENT)
        if selected_item:
            item_name = self.canvas.gettags(selected_item[0])[0]
            if item_name == "Computer":
                self.open_computer_app()
            elif item_name == "Pip Installer":
                self.open_pip_installer_app()
            elif item_name == "My Local Network":
                self.open_local_network_app()
            elif item_name == "System Center":
                self.open_system_center_app()
            elif item_name == "Google.com":
                self.open_google_app()
            elif item_name == "Settings":
                self.open_settings_app()

    def open_computer_app(self):
        # Placeholder logic for opening the Computer app
        tk.messagebox.showinfo("Computer App", "Opening Computer App...")

    def open_pip_installer_app(self):
        # Placeholder logic for opening the Pip Installer app
        tk.messagebox.showinfo("Pip Installer App", "Opening Pip Installer App...")

    def open_local_network_app(self):
        # Placeholder logic for opening the Local Network app
        tk.messagebox.showinfo("Local Network App", "Opening Local Network App...")

    def open_system_center_app(self):
        # Placeholder logic for opening the System Center app
        tk.messagebox.showinfo("System Center App", "Opening System Center App...")

    def open_google_app(self):
        # Placeholder logic for opening the Google app
        webbrowser.open("https://www.google.com")

    def open_settings_app(self):
        # Placeholder logic for opening the Settings app
        tk.messagebox.showinfo("Settings App", "Opening Settings App...")


def desktop():
    root = tk.Tk()
    app = DesktopApp(root)
    root.mainloop()


def main():
    mode = '1'

    if mode == '1':
        desktop()


if __name__ == "__main__":
    main()

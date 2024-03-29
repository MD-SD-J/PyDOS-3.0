import pygame
import sys
import webbrowser
import os

def boot():
    print("PyDOS MF BOOTLOADER")
    print()
    print("[Python Disk Operating System]")
    print("[Version 3.0 Experimental]")
    print("[CDP-PyOS]")
    print("[PyDOS Next Generation]")
    print("(R)Registered Nova Robotics S-Corporation")
    print()
    print("What would you like to do?")
    print()
    print("[1] [Start PyDOS]")
    print("[2] [Maintenance]")
    print("[3] [Terminal]")
    bootmode = input(">>> ")
    if bootmode == '1':
        start()
    elif bootmode == '2':
        maintenance()
    elif bootmode == '3':
        terminal()

def maintenance():
    # placeholder
    pass

def terminal():
    # placeholder
    pass

def show_context_menu(screen, font, black, position):
    menu_rect = pygame.Rect(position[0], position[1], 150, 100)
    pygame.draw.rect(screen, (200, 200, 200), menu_rect)

    options = ["Create New File", "Create New Folder", "Compress ZIP File"]
    for i, option in enumerate(options):
        text = font.render(option, True, black)
        text_rect = text.get_rect(center=(menu_rect.centerx, menu_rect.centery + i * 25))
        screen.blit(text, text_rect)

def create_new_file():
    print("Creating new file... Opening text editor.")

def create_new_folder():
    print("Creating new folder on the desktop.")

def start():
    pygame.init()

    width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    pygame.display.set_caption("PyDOS 3.0 EXP (PyDOS NG)")

    # Define colors
    background_color = (52, 235, 180)
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Define grid parameters
    grid_size = 50  # Adjust the grid size here
    num_rows = height // grid_size
    num_cols = width // grid_size
    offset_x = 45  # Offset between columns
    icon_spacing = 45  # Spacing between icons

    # Define app names
    app_names = [
        "This Computer",
        "Settings",
        "System Center",
        "My Subroutines",
        "Terminal",
        "My Local Network",
        "Entertainment Center",
        "Google"
    ]

    # Create a list to store app rectangles
    app_rects = []

    # Populate the app rectangles
    for col in range(num_cols):
        for row, app_name in enumerate(app_names):
            x = col * (grid_size + icon_spacing) + offset_x
            y = row * (grid_size + icon_spacing)
            app_rects.append(pygame.Rect(x, y, grid_size, grid_size))

    # Main loop
    dragging = False
    drag_offset = (0, 0)
    selected_rect = None
    double_click_time = 0  # Variable to track the time of the last click
    double_click_threshold = 500  # Adjust this threshold based on your preference (in milliseconds)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if pygame.time.get_ticks() - double_click_time < double_click_threshold:
                        # Double-click detected
                        for rect in app_rects:
                            if rect.collidepoint(event.pos):
                                if app_names[app_rects.index(rect)] == "Google":
                                    # Open Google.com in a new window
                                    webbrowser.open("https://www.google.com")
                                    # Add more conditions for other apps if needed
                    double_click_time = pygame.time.get_ticks()
                elif event.button == 3:  # Right mouse button
                    for rect in app_rects:
                        if rect.collidepoint(event.pos):
                            show_context_menu(screen, font, black, event.pos)

        font_size = 18  # Adjust the font size
        font = pygame.font.Font(None, font_size)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        for rect in app_rects:
                            if rect.collidepoint(event.pos):
                                dragging = True
                                selected_rect = rect
                                drag_offset = (rect.x - event.pos[0], rect.y - event.pos[1])
                    elif event.button == 3:  # Right mouse button
                        for rect in app_rects:
                            if rect.collidepoint(event.pos):
                                show_context_menu(screen, font, black, event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        dragging = False
                        selected_rect = None
                elif event.type == pygame.MOUSEMOTION:
                    if dragging:
                        selected_rect.x = event.pos[0] + drag_offset[0]
                        selected_rect.y = event.pos[1] + drag_offset[1]
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        create_new_file()
                    elif event.key == pygame.K_n and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        create_new_folder()

            # Draw background
            screen.fill(background_color)

            # Draw app rectangles
            for rect, app_name in zip(app_rects, app_names):
                pygame.draw.rect(screen, white, rect)
                text = font.render(app_name, True, black)
                text_rect = text.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height + font_size))
                screen.blit(text, text_rect)

            # Snap to the closest grid spot
            if selected_rect:
                closest_rect = min(app_rects, key=lambda r: ((selected_rect.x - r.x)**2 + (selected_rect.y - r.y)**2)**0.5)
                selected_rect.x, selected_rect.y = closest_rect.x, closest_rect.y

            # Update the display
            pygame.display.flip()

# Run the boot function before starting Pygame
boot()
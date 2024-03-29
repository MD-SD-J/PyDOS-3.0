import pygame
import sys
import webbrowser # for Google
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

def show_context_menu(screen, position):
    menu_rect = pygame.Rect(position, (200, 160))  # Rectangle for the menu
    option_rects = []  # List to store option rectangles

    # Define menu options
    options = ["Create New File", "Create New Folder", "Compress ZIP File"]

    for i, option in enumerate(options):
        option_rect = pygame.Rect(position[0], position[1] + i * 40, 200, 40)
        option_rects.append(option_rect)

    # Define close button
    close_button_rect = pygame.Rect(position[0] + 180, position[1], 20, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, option_rect in enumerate(option_rects):
                        if option_rect.collidepoint(event.pos):
                            handle_menu_option(i)
                            return
                    if close_button_rect.collidepoint(event.pos):
                        return

        # Draw menu rectangle
        pygame.draw.rect(screen, (200, 200, 200), menu_rect)

        # Draw menu options
        for i, option_rect in enumerate(option_rects):
            pygame.draw.rect(screen, (150, 150, 150), option_rect)
            font = pygame.font.Font(None, 20)
            text = font.render(options[i], True, (0, 0, 0))
            text_rect = text.get_rect(center=option_rect.center)
            screen.blit(text, text_rect)

        # Draw close button
        pygame.draw.line(screen, (255, 0, 0), close_button_rect.topleft, close_button_rect.bottomright, 2)
        pygame.draw.line(screen, (255, 0, 0), close_button_rect.bottomleft, close_button_rect.topright, 2)

        pygame.display.flip()

def handle_menu_option(option_index):
    if option_index == 0:
        create_new_file()
    elif option_index == 1:
        create_new_folder()
    elif option_index == 2:
        compress_zip_file()

def create_new_file():
    print("Creating new file... Opening text editor.")

def create_new_folder():
    print("Creating new folder on the desktop.")

def compress_zip_file():
    print("Compressing ZIP file... Placeholder.")

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
    grid_size = 70
    num_rows = 6
    num_cols = 12
    start_x = 5  # Starting x-coordinate for the first column
    offset_x = 20  # Offset between columns

    # Define app names and order
    app_order = ["This Computer", "Settings", "System Center", "My Subroutines", "Terminal", "My Local Network", "Google"]

    # Create a list to store app rectangles
    app_rects = []

    # Populate the app rectangles
    for col in range(num_cols):
        for row, app_name in enumerate(app_order):
            app_rects.append(pygame.Rect(col * grid_size * 2 + start_x + col * offset_x, row * grid_size + 50, grid_size, grid_size))

    # Main loop
    dragging = False
    drag_offset = (0, 0)
    selected_rect = None

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
                            show_context_menu(screen, event.pos)
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
        for rect, app_name in zip(app_rects, app_order):
            pygame.draw.rect(screen, white, rect)
            font = pygame.font.Font(None, 18)
            text = font.render(app_name, True, black)
            text_rect = text.get_rect(center=(rect.x + rect.width // 2, rect.y + rect.height // 2))
            screen.blit(text, text_rect)

        # Snap to the closest grid spot
        if selected_rect:
            closest_rect = min(app_rects, key=lambda r: ((selected_rect.x - r.x) ** 2 + (selected_rect.y - r.y) ** 2) ** 0.5)
            selected_rect.x, selected_rect.y = closest_rect.x, closest_rect.y

        # Update the display
        pygame.display.flip()

# Run the boot function before starting Pygame
boot()
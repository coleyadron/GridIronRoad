import pygame
import gridironRoad
from cursor import TextCursor

def inputStaff(screen):
    bgi = pygame.image.load("assets/images/BGI-2.png")
    font = pygame.font.Font("assets/Fonts/MinecraftRegular-Bmg3.otf", 35)

    # Text surfaces
    labels = {
        "offense": font.render("Offensive Coordinator: ", True, (255, 255, 255)),
        "defense": font.render("Defensive Coordinator: ", True, (255, 255, 255)),
        "special": font.render("Special Teams Coordinator: ", True, (255, 255, 255)),
        "confirm": font.render("Are these names correct: ", True, (255, 255, 255))
    }

    # Input fields
    fields = {
        "offense": {"text": "", "rect": pygame.Rect(labels["offense"].get_width() + 85, 55, 140, 35)},
        "defense": {"text": "", "rect": pygame.Rect(labels["defense"].get_width() + 85, 105, 140, 35)},
        "special": {"text": "", "rect": pygame.Rect(labels["special"].get_width() + 85, 155, 140, 35)},
        "confirm": {"text": "", "rect": pygame.Rect(labels["confirm"].get_width() + 80, 
                                                  screen.get_height() - labels["confirm"].get_height() - 30, 
                                                  140, 35)}
    }

    # Field order and current field
    field_order = ["offense", "defense", "special", "confirm"]
    current_field = 0
    cursor = TextCursor(fields[field_order[current_field]]["rect"].x, 
                       fields[field_order[current_field]]["rect"].y, 
                       fields[field_order[current_field]]["rect"].height)

    staffOpen = True
    while staffOpen:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gridironRoad.killgame(screen)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    gridironRoad.killgame(screen)
                
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if fields[field_order[current_field]]["text"].strip() != "":
                        if current_field < len(field_order) - 1:
                            current_field += 1
                            # Reset cursor position for new field
                            cursor.rect.x = fields[field_order[current_field]]["rect"].x
                            cursor.rect.y = fields[field_order[current_field]]["rect"].y
                        else:
                            # Confirmation logic
                            confirmation = fields["confirm"]["text"].strip().upper()
                            if confirmation in ("YES", "Y"):
                                staffOpen = False
                                return [fields["offense"]["text"], 
                                        fields["defense"]["text"], 
                                        fields["special"]["text"]]
                            elif confirmation in ("NO", "N"):
                                # Reset all fields
                                for field in fields.values():
                                    field["text"] = ""
                                current_field = 0
                                cursor.rect.x = fields[field_order[current_field]]["rect"].x
                                cursor.rect.y = fields[field_order[current_field]]["rect"].y
                
                elif event.key == pygame.K_BACKSPACE:
                    if fields[field_order[current_field]]["text"]:
                        fields[field_order[current_field]]["text"] = fields[field_order[current_field]]["text"][:-1]
                
                else:  # Regular character input
                    if event.unicode.isprintable() and len(fields[field_order[current_field]]["text"]) < 20:
                        fields[field_order[current_field]]["text"] += event.unicode

        # Update cursor position
        text_width = font.size(fields[field_order[current_field]]["text"])[0]
        cursor.rect.x = fields[field_order[current_field]]["rect"].x + text_width
        cursor.rect.y = fields[field_order[current_field]]["rect"].y
        cursor.update(cursor.rect.x, cursor.rect.y, fields[field_order[current_field]]["rect"].height)

        # Update input box widths
        for field in fields.values():
            field["rect"].w = max(100, font.size(field["text"])[0] + 10)

        # Drawing
        screen.blit(bgi, (0, 0))
        
        # Draw labels and fields
        screen.blit(labels["offense"], (85, 55))
        screen.blit(labels["defense"], (85, 105))
        screen.blit(labels["special"], (85, 155))
        
        # Draw input boxes
        for field in fields.values():
            pygame.draw.rect(screen, pygame.Color('black'), field["rect"])
        
        # Draw text
        screen.blit(font.render(fields["offense"]["text"], True, (255, 255, 255)), 
                    (fields["offense"]["rect"].x, fields["offense"]["rect"].y))
        screen.blit(font.render(fields["defense"]["text"], True, (255, 255, 255)), 
                    (fields["defense"]["rect"].x, fields["defense"]["rect"].y))
        screen.blit(font.render(fields["special"]["text"], True, (255, 255, 255)), 
                    (fields["special"]["rect"].x, fields["special"]["rect"].y))
        
        # Confirmation
        if current_field == 3:
            screen.blit(labels["confirm"], (80, screen.get_height() - labels["confirm"].get_height() - 30))
            screen.blit(font.render(fields["confirm"]["text"], True, (255, 255, 255)), 
                        (fields["confirm"]["rect"].x, fields["confirm"]["rect"].y))

        # Draw cursor
        cursor.draw(screen)
        
        pygame.display.flip()
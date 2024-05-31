"""logo"""
import os
import random


ingram_icon = r"""
          _    __..-:┑
   ║`====╩=╩=======╣ |
==#║_______███_/ @ ║ |
   ╚===.===╦==╦=╤==╩#█
       \___║::║/      
           ║::║|      
           ║::║|      
           ║::║_\     
            ██        
            ██        
            ██        
            ██        
            ██        
"""


ingram_fonts = [
r"""
 SlickMercyX      
""",
]


def generate_logo() -> list:
    """concatenate the icon and font"""
    icon = [i for i in ingram_icon.split('\n') if i.strip()]
    icon_width = max([len(i) for i in icon])
    icon = [' ' * icon_width] + icon + [' ' * icon_width]
    icon_height = len(icon)

    # do not longger than the terminal width!!!
    found = False
    for _ in range(100):
        font = random.choice(ingram_fonts).split('\n')
        font_width = max([len(i) for i in font])
        font_height = len(font)
        try:
            if font_width + icon_width + 2 < os.get_terminal_size()[0]:
                found = True
                break
        except:
            found = True
            break
    if not found:
        font = ['']
        font_height = 1

    if icon_height > font_height:
        num = icon_height - font_height
        if num & 1: head, tail = num // 2, num // 2 + 1
        else: head, tail = num // 2, num // 2
        font = [' '] * head + font + [' '] * tail
    
    elif icon_height < font_height:
        num = font_height - icon_height
        if num & 1: head, tail = num // 2, num // 2 + 1
        else: head, tail = num // 2, num // 2
        icon = [' ' * icon_width] * head + icon + [' ' * icon_width] * tail
    
    return [icon, font]


logo = generate_logo()


if __name__ == '__main__':
    for left, right in zip(*logo):
        print(f"{left}  {right}")
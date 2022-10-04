import platform, os
from rich.console import Console

import classes as c
import get_faces as face

console = Console()
def startup_sequence():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    console.print("""
    [bold red]
 ██████╗ ███████╗███╗   ███╗██╗██╗   ██╗███╗   ███╗
██╔═══██╗██╔════╝████╗ ████║██║██║   ██║████╗ ████║
██║   ██║███████╗██╔████╔██║██║██║   ██║██╔████╔██║
██║   ██║╚════██║██║╚██╔╝██║██║██║   ██║██║╚██╔╝██║
╚██████╔╝███████║██║ ╚═╝ ██║██║╚██████╔╝██║ ╚═╝ ██║
 ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚═╝     ╚═╝    
[/bold red][italic bold]       A fake identity generator by [/][bold yellow]@Kaiser[/]

[bold cyan][G][/] - [italic]Generate a new identity[/]
[bold cyan][I][/] - [italic]Generate a new fake image[/]
[bold cyan][Q][/] - [italic]Quit[/]
""")

if __name__ == '__main__':
    startup_sequence()

    while True:
        i = console.input("[bold cyan]>>>[/] ").lower()
        if i == "g":
            id = c.FakeIdentity()
            id.generate_all()
            id.prettyprint()
        elif i == "i":
            face.generate()
        elif i == "q":
            break

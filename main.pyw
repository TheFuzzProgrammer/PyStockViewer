__author__ = 'Fuzz'

import UserInterface.main

stylesheet = """
    CVMain {
        background-image: url("/img/background.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == "__main__":
    UserInterface.main.start_ui(stylesheet)
else:
    print("StockViewer by Fuzz \nThis module only can run as user")

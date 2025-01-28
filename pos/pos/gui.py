import tkinter as tk
import threading
import time


            
class GUI:
    def __init__(self, pos_state, auto=False):
        self.pressed = False # redundant
        self.pos_state = pos_state
        
        

        self.window = tk.Tk()
        self.window.title("POS")
        self.label = tk.Label(self.window, text="POS")
        self.label.pack(pady=60)
        self.button = tk.Button(self.window, text="Done", command=self.done)
        self.button.pack()
        
        self.card = tk.Label(self.window)
        self.card.pack()
        
        self.items = tk.Label(self.window)
        self.items.pack()
        
        self.prices = tk.Label(self.window)
        self.prices.pack()
        
        self.total_price = tk.Label(self.window)
        self.total_price.pack()

            
        self.mainloop(pos_state)
        
        self.window.mainloop()
        

        
        

        
            
    def mainloop(self, pos_state):
        self.card.config(text="Card #: " + str(pos_state["card"]))
        self.items.config(text="Items: " + str(pos_state["items"]))
        self.prices.config(text="Prices: " + str(pos_state["prices"]))
        self.total_price.config(text="Total price: " + str(sum(pos_state["prices"])))
        

        if self.pressed and pos_state["card"]:  # Assuming its "accepted"
            print("Sale.")
            pos_state["items"] = []
            pos_state["prices"] = []
            pos_state["card"] = None
            # CHANGE BUTTON TODO

            
        # Schedule the next iteration after a delay
        self.window.after(100, self.mainloop, pos_state)

        
    
    
    def back(self):
        self.pressed = False
        self.button.config(text="Done", command=self.done)
        self.pos_state["ringing up"] = True
    
    def done(self):
        self.pressed = True
        self.button.config(text="Back", command=self.back)
        self.pos_state["ringing up"] = False
        
if __name__ == '__main__':
    main()

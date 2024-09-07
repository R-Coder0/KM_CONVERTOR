def convertor():
    km = int(kilometer_entry.get())
    miles = km* 0.621371
    output_text.config(state = tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Total miles for {km} km are {miles:.2f}")
    output_text.config(state = tk.DISABLED)
    
import tkinter as tk 
root = tk.Tk()
root.geometry("700x500")
root.title("KM converter")
kilometer_label = tk.Label(text = "Enter the kilometer", font = 20)
kilometer_label.grid(row = 0, column = 0, padx = 25, pady = 25)

kilometer_entry = tk.Entry(width= 50, bg = "powderblue", borderwidth = 10)
kilometer_entry.grid(row = 0, column=1)

convert_button = tk.Button(text = "CONVERT", command = convertor, bg="lightgreen")
convert_button.grid(row = 1, column= 1)

output_text = tk.Text(height = 10, width=50, bg="powderblue")
output_text.grid(row = 3, column = 1, pady = 0)

root.mainloop()
from tkinter import *


def miles_to_km():
    #you must change the miles type to float so you can multiply it later
    miles = float(miles_input.get())
    km = miles * 1.609
    #change kilometer_label to the new km value
    kilometer_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)


is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

#,command is used to trigger the miles_to_km function
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
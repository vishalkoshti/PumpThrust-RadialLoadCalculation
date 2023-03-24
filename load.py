import tkinter as tk

# Function to calculate the pump loads
def calculate_loads():
    flow_rate = float(flow_rate_entry.get())
    head = float(head_entry.get())
    speed = float(speed_entry.get())
    shaft_dia = float(shaft_dia_entry.get())
    shaft_length = float(shaft_length_entry.get())

    # Calculate radial load
    radial_load = 1.414 * flow_rate * head / speed / 1000

    # Calculate thrust load
    thrust_load = 1.414 * flow_rate * head / 2 / speed / 1000 * shaft_dia / shaft_length

    # Display the results
    radial_label.config(text="Radial Load: {:.2f} kN".format(radial_load))
    thrust_label.config(text="Thrust Load: {:.2f} kN".format(thrust_load))

# Create the main window
root = tk.Tk()
root.title("Pump Load Calculator")

# Create the input elements
flow_rate_label = tk.Label(root, text="Flow Rate (m^3/hr):")
flow_rate_label.grid(row=0, column=0, padx=5, pady=5)
flow_rate_entry = tk.Entry(root)
flow_rate_entry.grid(row=0, column=1, padx=5, pady=5)

head_label = tk.Label(root, text="Head (m):")
head_label.grid(row=1, column=0, padx=5, pady=5)
head_entry = tk.Entry(root)
head_entry.grid(row=1, column=1, padx=5, pady=5)

speed_label = tk.Label(root, text="Speed (RPM):")
speed_label.grid(row=2, column=0, padx=5, pady=5)
speed_entry = tk.Entry(root)
speed_entry.grid(row=2, column=1, padx=5, pady=5)

shaft_dia_label = tk.Label(root, text="Shaft Diameter (mm):")
shaft_dia_label.grid(row=3, column=0, padx=5, pady=5)
shaft_dia_entry = tk.Entry(root)
shaft_dia_entry.grid(row=3, column=1, padx=5, pady=5)

shaft_length_label = tk.Label(root, text="Shaft Length (mm):")
shaft_length_label.grid(row=4, column=0, padx=5, pady=5)
shaft_length_entry = tk.Entry(root)
shaft_length_entry.grid(row=4, column=1, padx=5, pady=5)

# Create the button to calculate the loads
calculate_button = tk.Button(root, text="Calculate Loads", command=calculate_loads)
calculate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create the label to display the results
radial_label = tk.Label(root, text="")
radial_label.grid(row=6, column=0, padx=5, pady=5)
thrust_label = tk.Label(root, text="")
thrust_label.grid(row=7, column=0, padx=5, pady=5)

# Run the main loop
root.mainloop()

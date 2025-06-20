import tkinter as tk
from tkinter import messagebox

def send_alert():
    alert_text = text_entry.get("1.0", tk.END).strip()
    if alert_text:
        # Here you would send the alert to the transmitter or save it
        print(f"Sending alert:\n{alert_text}")
        messagebox.showinfo("Alert Sent", "Your EAS alert/test was sent.")
        text_entry.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Empty", "No alert to send.")

root = tk.Tk()
root.title("KLOT Text Workstation")

text_entry = tk.Text(root, height=10, width=60)
text_entry.pack(padx=10, pady=10)

send_button = tk.Button(root, text="Send Alert", command=send_alert)
send_button.pack(pady=5)

root.mainloop()
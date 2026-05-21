import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Flipkart Frontend")
root.geometry("800x600")
root.config(bg="white")

# Header
header = tk.Frame(root, bg="#2874F0", height=60)
header.pack(fill="x")

logo = tk.Label(header, text="Flipkart", font=("Arial", 24, "bold"), fg="white", bg="#2874F0")
logo.pack(side="left", padx=20)

search = tk.Entry(header, width=40, font=("Arial", 14))
search.pack(side="left", padx=20, pady=10)

search_btn = tk.Button(header, text="Search", bg="yellow", font=("Arial", 12, "bold"))
search_btn.pack(side="left")

# Product Section
products_frame = tk.Frame(root, bg="white")
products_frame.pack(pady=20)

products = [
    ("iPhone 15", "₹79,999"),
    ("Samsung TV", "₹45,000"),
    ("Laptop", "₹55,000"),
    ("Shoes", "₹2,000"),
]


def buy_product(product_name):
    messagebox.showinfo("Order", f"You bought {product_name} successfully!")


row = 0
col = 0

for product, price in products:
    card = tk.Frame(products_frame, bg="#f1f3f6", bd=2, relief="solid", padx=20, pady=20)
    card.grid(row=row, column=col, padx=20, pady=20)

    name_label = tk.Label(card, text=product, font=("Arial", 16, "bold"), bg="#f1f3f6")
    name_label.pack(pady=10)

    price_label = tk.Label(card, text=price, font=("Arial", 14), fg="green", bg="#f1f3f6")
    price_label.pack(pady=10)

    buy_btn = tk.Button(card, text="Buy Now", bg="#FB641B", fg="white",
                         font=("Arial", 12, "bold"),
                         command=lambda p=product: buy_product(p))
    buy_btn.pack(pady=10)

    col += 1
    if col > 1:
        col = 0
        row += 1

# Footer
footer = tk.Label(root, text="© Flipkart Clone in Python", bg="#2874F0", fg="white",
                  font=("Arial", 12))
footer.pack(side="bottom", fill="x")

root.mainloop()


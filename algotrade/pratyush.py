
# options terminal 2
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

root = tk.Tk()
root.title("Options Payoff Graph")
root.geometry("800x600")

main_frame = ttk.Frame(root)
main_frame.pack(padx=10, pady=10)
def handle_calculate():
    spot_price = float(spot_price_entry.get())
    contracts = contract_frames

    plot_payoff_graph(spot_price, contracts)

calculate_button = ttk.Button(root, text="Calculate", command=handle_calculate)
calculate_button.pack(pady=10)

spot_price_label = ttk.Label(main_frame, text="Spot Price:")
spot_price_label.grid(row=0, column=0, padx=5, pady=5)
spot_price_entry = ttk.Entry(main_frame)
spot_price_entry.grid(row=0, column=1, padx=5, pady=5)

contract_frames = []


def add_contract():
    contract_frame = ttk.LabelFrame(main_frame, text="Contract")
    contract_frame.grid(row=len(contract_frames) + 1, column=0, columnspan=2, padx=5, pady=5)

    strike_price_label = ttk.Label(contract_frame, text="Strike Price:")
    strike_price_label.grid(row=0, column=0, padx=5, pady=5)
    strike_price_entry = ttk.Entry(contract_frame)
    strike_price_entry.grid(row=0, column=1, padx=5, pady=5)

    option_type_label = ttk.Label(contract_frame, text="Option Type:")
    option_type_label.grid(row=1, column=0, padx=5, pady=5)
    option_type_combobox = ttk.Combobox(contract_frame, values=["Call", "Put"])
    option_type_combobox.grid(row=1, column=1, padx=5, pady=5)

    buy_sell_label = ttk.Label(contract_frame, text="Buy/Sell:")
    buy_sell_label.grid(row=2, column=0, padx=5, pady=5)
    buy_sell_combobox = ttk.Combobox(contract_frame, values=["Buy", "Sell"])
    buy_sell_combobox.grid(row=2, column=1, padx=5, pady=5)

    premium_label = ttk.Label(contract_frame, text="Premium:")
    premium_label.grid(row=3, column=0, padx=5, pady=5)
    premium_entry = ttk.Entry(contract_frame)
    premium_entry.grid(row=3, column=1, padx=5, pady=5)

    contract_frame.strike_price_entry = strike_price_entry
    contract_frame.option_type_combobox = option_type_combobox
    contract_frame.buy_sell_combobox = buy_sell_combobox
    contract_frame.premium_entry = premium_entry

    contract_frames.append(contract_frame)  

add_contract_button = ttk.Button(root, text="Add Contract", command=add_contract)
add_contract_button.pack(padx=5, pady=5)

canvas_graph = tk.Canvas(root, width=700, height=400)
canvas_graph.pack(padx=10, pady=5)
def plot_payoff_graph(spot_price, contracts):
    fig, ax = plt.subplots()
    ax.axhline(0, color='black', lw=2)

    spot_prices = np.linspace(0.8 * spot_price, 1.2 * spot_price, 100)

    cumulative_payoff = np.zeros_like(spot_prices)

    for contract_frame in contracts:
        strike_price = float(contract_frame.strike_price_entry.get())
        option_type = contract_frame.option_type_combobox.get()
        buy_sell = contract_frame.buy_sell_combobox.get()
        premium = float(contract_frame.premium_entry.get())

        num_contracts = 1 if buy_sell == "Buy" else -1

        if option_type == "Call":
            payoffs = -(np.maximum(spot_prices - strike_price, 0) - premium)
        elif option_type == "Put":
            payoffs = -(np.maximum(strike_price - spot_prices, 0) - premium)

        cumulative_payoff += num_contracts * payoffs

    ax.plot(spot_prices, cumulative_payoff, label='Cumulative Payoff')

    ax.set_xlabel("Spot Price")
    ax.set_ylabel("Profit/Loss")
    ax.set_title("Options Payoff Graph")
    ax.legend()
    ax.grid(True)

    plt.tight_layout()
    plt.show()



root.mainloop()
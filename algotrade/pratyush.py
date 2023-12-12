# # google sheets


# import os
# import pickle
# import google.auth.transport.requests
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from google.oauth2 import service_account

# # Set up the scopes and credentials file
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# CREDENTIALS_FILE = '/Users/anushka/Desktop/algotrade/algotrade/pratyushmarket123-de41dafa811b.json'
# TOKEN_FILE = 'token.pickle'

# def get_credentials():
   
#     credentials = service_account.Credentials.from_service_account_file( CREDENTIALS_FILE, scopes=SCOPES)
#     return credentials

# def main():
#     # Authenticate and get credentials
#     credentials = get_credentials()
#     service = build('sheets', 'v4', credentials=credentials)

#     # Spreadsheet ID (you can find it in the URL of your Google Sheets)
#     spreadsheet_id = '1pfxeRxF332J3aJMHablWitNmx4Zms0tGapBmZx9QBMw'
#     # Data to write
#     data =[[1]]

#     # Define the range where you want to write the data (e.g., A1:C3)
#     range_ = 'Sheet8!A1'

#     # Call the Sheets API to update the data
#     request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption='RAW', body={'values': data})
#     response = request.execute()

#     print('Data successfully written to Google Sheets.')

# if __name__ == '__main__':
#     main()

# options terminal 1


# import tkinter as tk
# from tkinter import ttk
# import matplotlib.pyplot as plt
# import numpy as np

# root = tk.Tk()
# root.title("Options Payoff Graph")
# root.geometry("800x600")

# main_frame = ttk.Frame(root)
# main_frame.pack(padx=10, pady=10)

# spot_price_label = ttk.Label(main_frame, text="Spot Price:")
# spot_price_label.grid(row=0, column=0, padx=5, pady=5)
# spot_price_entry = ttk.Entry(main_frame)
# spot_price_entry.grid(row=0, column=1, padx=5, pady=5)

# contract_frames = []

# def add_contract():
#     contract_frame = ttk.LabelFrame(main_frame, text="Contract")
#     contract_frame.grid(row=len(contract_frames)+1, column=0, columnspan=2, padx=5, pady=5)

#     strike_price_label = ttk.Label(contract_frame, text="Strike Price:")
#     strike_price_label.grid(row=0, column=0, padx=5, pady=5)
#     strike_price_entry = ttk.Entry(contract_frame)
#     strike_price_entry.grid(row=0, column=1, padx=5, pady=5)

#     option_type_label = ttk.Label(contract_frame, text="Option Type:")
#     option_type_label.grid(row=1, column=0, padx=5, pady=5)
#     option_type_combobox = ttk.Combobox(contract_frame, values=["Call", "Put"])
#     option_type_combobox.grid(row=1, column=1, padx=5, pady=5)

#     buy_sell_label = ttk.Label(contract_frame, text="Buy/Sell:")
#     buy_sell_label.grid(row=2, column=0, padx=5, pady=5)
#     buy_sell_combobox = ttk.Combobox(contract_frame, values=["Buy", "Sell"])
#     buy_sell_combobox.grid(row=2, column=1, padx=5, pady=5)

#     premium_label = ttk.Label(contract_frame, text="Premium:")
#     premium_label.grid(row=3, column=0, padx=5, pady=5)
#     premium_entry = ttk.Entry(contract_frame)
#     premium_entry.grid(row=3, column=1, padx=5, pady=5)

#     contract_frame.strike_price_entry = strike_price_entry
#     contract_frame.option_type_combobox = option_type_combobox
#     contract_frame.buy_sell_combobox = buy_sell_combobox
#     contract_frame.premium_entry = premium_entry

#     contract_frames.append(contract_frame)

# add_contract_button = ttk.Button(main_frame, text="Add Contract", command=add_contract)
# add_contract_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# canvas_graph = tk.Canvas(root, width=700, height=400)
# canvas_graph.pack(padx=10, pady=5)

# def plot_payoff_graph(spot_price, contracts):
#     fig, ax = plt.subplots()
#     ax.axhline(0, color='black', lw=2)

#     spot_prices = np.linspace(0.8 * spot_price, 1.2 * spot_price, 100)

#     for contract in contracts:
#         strike_price = contract["strike_price"]
#         option_type = contract["option_type"]
#         num_contracts = contract["num_contracts"]
#         premium = contract["premium"]

#         if contract["buy_sell"] == "Sell":
#             num_contracts *= -1

#         if option_type == "Call":
#             payoffs = -(np.maximum(spot_prices - strike_price, 0) - premium)
#         elif option_type == "Put":
#             payoffs = -(np.maximum(strike_price - spot_prices, 0) - premium)

#         ax.plot(spot_prices, num_contracts * payoffs, label=f'{num_contracts} {option_type} @ {strike_price}')

#     ax.set_xlabel("Spot Price")
#     ax.set_ylabel("Profit/Loss")
#     ax.set_title("Options Payoff Graph")
#     ax.legend()
#     ax.grid(True)

#     plt.tight_layout()
#     plt.show()

# def handle_calculate():
#     spot_price = float(spot_price_entry.get())
#     contracts = []

#     for contract_frame in contract_frames:
#         strike_price = float(contract_frame.strike_price_entry.get())
#         option_type = contract_frame.option_type_combobox.get()
#         buy_sell = contract_frame.buy_sell_combobox.get()
#         premium = float(contract_frame.premium_entry.get())

#         num_contracts = 1
#         if buy_sell == "Sell":
#             num_contracts *= -1

#         contract = {
#             "strike_price": strike_price,
#             "option_type": option_type,
#             "num_contracts": num_contracts,
#             "premium": premium,
#             "buy_sell": buy_sell
#         }
#         contracts.append(contract)

#     plot_payoff_graph(spot_price, contracts)

# calculate_button = ttk.Button(main_frame, text="Calculate", command=handle_calculate)
# calculate_button.grid(row=len(contract_frames)+2, column=0, columnspan=2, padx=5, pady=5)

# root.mainloop()

# 5paisa

# App Name	5P53700772 
# App Source	5793
# User ID	U5XLxxpPP7g
# Password	fHzfCHaxIIu 
# User Key	G0RNtcBkVTKDfvokfStElzPT7X6qthAw 
# Encryption Key	YbuTd5c0SMSRAEvJliCPVY8hVBYdHXZH 
# from py5paisa import FivePaisaClient
# cred={
#     "APP_NAME":"5P53700772",
#     "APP_SOURCE":"5793",
#     "USER_ID":"U5XLxxpPP7g",
#     "PASSWORD":"fHzfCHaxIIu",
#     "USER_KEY":"G0RNtcBkVTKDfvokfStElzPT7X6qthAw",
#     "ENCRYPTION_KEY":"YbuTd5c0SMSRAEvJliCPVY8hVBYdHXZH"}

# #This function will automatically take care of generating and sending access token for all your API's

# client = FivePaisaClient(cred=cred)

# # New TOTP based authentication
# client.get_totp_session('53700772','098164','525625')

# # OAUTH Approach
# # First get a token by logging in to -> https://dev-openapi.5paisa.com/WebVendorLogin/VLogin/Index?VendorKey=<G0RNtcBkVTKDfvokfStElzPT7X6qthAw>&ResponseURL=< https://www.5paisa.com/technology/developer-apis>
# # VendorKey is UesrKey for individuals user
# # for e.g. you can use ResponseURL as https://www.5paisa.com/technology/developer-apis
# # Pass the token received in the response url after successful login to get an access token (this also sets the token for all the APIs you use)-

# # Please note that you need to copy the request token from URL and paste in this code and start the code within 30s.

#  client.get_oauth_session('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IjUzNzAwNzcyIiwicm9sZSI6IkcwUk50Y0JrVlRLRGZ2b2tmU3RFbHpQVDdYNnF0aEF3IiwibmJmIjoxNjkxMTY3NzU5LCJleHAiOjE2OTExNjc3ODksImlhdCI6MTY5MTE2Nzc1OX0.w0h5QMfqbPt0MVVEtx4hdGmd2m7rPN12COoAa_XaWh8&state=')

# print(client.holdings())

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


# def plot_payoff_graph(spot_price, contracts):
#     fig, ax = plt.subplots()
#     ax.axhline(0, color='black', lw=2)

#     spot_prices = np.linspace(0.8 * spot_price, 1.2 * spot_price, 100)

#     for contract_frame in contracts:
#         strike_price = float(contract_frame.strike_price_entry.get())
#         option_type = contract_frame.option_type_combobox.get()
#         buy_sell = contract_frame.buy_sell_combobox.get()
#         premium = float(contract_frame.premium_entry.get())

#         num_contracts = 1 if buy_sell == "Buy" else -1

#         if option_type == "Call":
#             payoffs = -(np.maximum(spot_prices - strike_price, 0) - premium)
#         elif option_type == "Put":
#             payoffs = -(np.maximum(strike_price - spot_prices, 0) - premium)

#         ax.plot(spot_prices, num_contracts * payoffs, label=f'{num_contracts} {option_type} @ {strike_price}')

#     ax.set_xlabel("Spot Price")
#     ax.set_ylabel("Profit/Loss")
#     ax.set_title("Options Payoff Graph")
#     ax.legend()
#     ax.grid(True)

#     plt.tight_layout()
#     plt.show()

# def handle_calculate():
#     spot_price = float(spot_price_entry.get())
#     contracts = contract_frames

#     plot_payoff_graph(spot_price, contracts)

# calculate_button = ttk.Button(root, text="Calculate", command=handle_calculate)
# calculate_button.pack(pady=10)

root.mainloop()
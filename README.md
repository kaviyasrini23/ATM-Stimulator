# Advanced ATM Simulator

The "Advanced ATM Simulator" is a fully interactive Python-based application developed using the Tkinter library. This project mimics the core functionalities of an Automated Teller Machine (ATM), allowing users to securely log in, check their account balance, deposit and withdraw money, view their transaction history, and even export this history to a CSV file. The simulator provides an intuitive and modern interface, featuring daily withdrawal limits and secure PIN management to ensure a realistic user experience.

## Key Features

#1. "User Authentication"

    "Username and PIN Login": Secure login process that ensures only authenticated users can access their accounts. Each user has a unique PIN for added security.
     "Custom Error Handling": Alerts users if they enter an incorrect username or PIN, improving usability.

# 2. "Account Balance Inquiry"
     "Instant Balance Check": Users can quickly view the available balance in their savings account with just a click.
     "Clear Display": The balance is presented in an easy-to-read format with comma-separated values for large amounts (e.g., ₹50,000).

# 3. "Deposit & Withdrawal Functions"

    "Depositing Money": Users can deposit any amount into their savings account, with an immediate update to their balance.
     "Withdrawing Money": The simulator enforces a daily withdrawal limit of ₹20,000, allowing users to withdraw money while preventing excessive daily withdrawals.
     "Insufficient Balance Alerts": The system checks if users have sufficient funds before allowing withdrawals and displays appropriate messages when the balance is too low.

# 4. "Transaction History Management"
    
  "View Transaction History": Users can view a detailed list of all their transactions (both deposits and withdrawals).
  "Export to CSV": The entire transaction history can be exported to a CSV file for easy access outside of the simulator, enabling users to keep permanent records.

# 5. "PIN Management"
  "Change PIN": Users have the option to securely change their PIN from within the simulator. The new PIN must be 4 digits long, ensuring standard ATM security practices are followed.

# 6. "User Interface (UI) and Experience"

  "Modern, Custom Design": The simulator features a dark-themed interface with a custom title bar and rounded corners, giving it a sleek and polished appearance.
  "Custom Title Bar": The title bar includes maximize, minimize, and close buttons, providing full control over the window.
  "Progress Bar": A progress bar adds to the experience by simulating loading animations during balance inquiries, deposits, and withdrawals, enhancing realism.
  "Responsive Design": The ATM simulator automatically adjusts to screen sizes and is centered on launch for a better user experience.

# 7. "Daily Limits and Security"
    
  "Daily Withdrawal Limit": Users can withdraw a maximum of ₹20,000 per day, mimicking real ATM limits and preventing excessive withdrawals.
  "Secure PIN Handling": PINs are handled securely, with error messages for invalid or improperly formatted PINs.

# Technical Stack

 "Programming Language": Python
 "GUI Library": Tkinter for designing the graphical user interface (GUI).
 "Data Management": User information, account balances, and transaction history are stored in Python dictionaries for easy data handling during runtime.
 "File Handling": CSV file format is used to export transaction histories for future reference.

## Project Structure

atm_simulator/
│
├── atm_simulator.py  # Main application code
├── README.md         # Project documentation
├── requirements.txt  # Dependencies (if any)
└── screenshots/      # Directory for screenshots used in the README
    └── login.png
    └── main_menu.png

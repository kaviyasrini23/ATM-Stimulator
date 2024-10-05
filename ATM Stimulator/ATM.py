import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import time
import csv

class ATM:
    def __init__(self, root, users, current_user=None):
        self.users = users
        self.current_user = current_user
        self.daily_withdrawal_limit = 20000
        self.withdrawn_today = 0
        
        # Customize root window
        self.root = root
        self.root.title("Advanced ATM Simulator")
        self.center_window(600, 600)  # Center the window
        self.root.configure(bg="#2C2F33")  # Dark background
        self.root.overrideredirect(True)  # Remove window decorations
        self.create_custom_title_bar()

        # Create a canvas for rounded corners
        self.canvas = tk.Canvas(self.root, bg="#2C2F33", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.create_rectangle(0, 0, 600, 600, fill="#23272A", outline="")

        self.create_login_screen()

    def center_window(self, width, height):
        """Center the window on the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_custom_title_bar(self):
        """Create a custom title bar."""
        title_bar = tk.Frame(self.root, bg="#7289DA", relief="flat")
        title_bar.pack(fill=tk.X)

        # Title label
        title_label = tk.Label(title_bar, text="ATM Simulator", bg="#7289DA", font=("Times New Roman", 16, 'bold'), fg='white')
        title_label.pack(side=tk.LEFT, padx=10)

        # Maximize button
        max_button = tk.Button(title_bar, text="🗖", command=self.maximize_window, bg="#7289DA", fg='white', borderwidth=0)
        max_button.pack(side=tk.RIGHT, padx=5)

        # Minimize button
        min_button = tk.Button(title_bar, text="🗕", command=self.minimize_window, bg="#7289DA", fg='white', borderwidth=0)
        min_button.pack(side=tk.RIGHT)

        # Exit button
        exit_button = tk.Button(title_bar, text="✖", command=self.root.quit, bg="#D50000", fg='white', borderwidth=0)
        exit_button.pack(side=tk.RIGHT)

        title_bar.bind("<B1-Motion>", self.move_window)  # Allow moving the window

    def move_window(self, event):
        """Move the window."""
        self.root.geometry(f'+{event.x_root}+{event.y_root}')

    def clear_screen(self):
        """Clear all widgets from the current screen."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_login_screen(self):
        """Create the login screen interface."""
        self.clear_screen()

        title = tk.Label(self.root, text="Welcome to the ATM", font=("Times New Roman", 24, 'bold'), bg="#23272A", fg="#7289DA")
        title.pack(pady=20)

        self.user_label = tk.Label(self.root, text="Username:", font=("Times New Roman", 12), bg="#23272A", fg="white")
        self.user_label.pack(pady=5)

        self.user_entry = tk.Entry(self.root, font=("Times New Roman", 12), justify='center', bd=2)
        self.user_entry.pack(pady=5)

        self.pin_label = tk.Label(self.root, text="PIN:", font=("Times New Roman", 12), bg="#23272A", fg="white")
        self.pin_label.pack(pady=5)

        self.pin_entry = tk.Entry(self.root, show="*", font=("Times New Roman", 12), justify='center', bd=2)
        self.pin_entry.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", width=15, command=self.authenticate, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.login_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", width=15, command=self.root.quit, bg="#D50000", fg='white', font=("Times New Roman", 12))
        self.quit_button.pack(pady=10)

    def authenticate(self):
        """Authenticate the user based on username and PIN."""
        username = self.user_entry.get()
        pin = self.pin_entry.get()
        
        if username in self.users and self.users[username]['pin'] == pin:
            self.current_user = username
            self.withdrawn_today = 0
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Invalid Username or PIN!")

    def create_main_menu(self):
        """Create the main ATM menu."""
        self.clear_screen()

        welcome_label = tk.Label(self.root, text=f"Welcome, {self.current_user}", font=("Times New Roman", 24, 'bold'), bg="#23272A", fg="#7289DA")
        welcome_label.pack(pady=20)

        self.check_balance_button = tk.Button(self.root, text="Check Balance", width=20, command=self.check_balance, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.check_balance_button.pack(pady=10)

        self.deposit_button = tk.Button(self.root, text="Deposit Money", width=20, command=self.deposit_money, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.deposit_button.pack(pady=10)

        self.withdraw_button = tk.Button(self.root, text="Withdraw Money", width=20, command=self.withdraw_money, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.withdraw_button.pack(pady=10)

        self.history_button = tk.Button(self.root, text="Transaction History", width=20, command=self.show_history, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.history_button.pack(pady=10)

        self.export_button = tk.Button(self.root, text="Export History", width=20, command=self.export_history, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.export_button.pack(pady=10)

        self.change_pin_button = tk.Button(self.root, text="Change PIN", width=20, command=self.change_pin, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.change_pin_button.pack(pady=10)

        self.quit_button = tk.Button(self.root, text="Log Out", width=20, command=self.create_login_screen, bg="#7289DA", fg='white', font=("Times New Roman", 12))
        self.quit_button.pack(pady=10)

        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=20)

    def show_loading(self, message="Processing"):
        """Simulate a loading animation using a progress bar."""
        self.progress['value'] = 0
        self.root.update_idletasks()
        for i in range(101):
            time.sleep(0.02)  # Adjust speed of progress
            self.progress['value'] = i
            self.root.update_idletasks()

    def check_balance(self):
        """Display the current balance for the logged-in user."""
        self.show_loading("Checking balance")
        balance_info = f"Checking Balance:\nSavings: ₹{self.users[self.current_user]['accounts']['savings']:,}"
        messagebox.showinfo("Balance", balance_info)

    def deposit_money(self):
        """Deposit money into the user's savings account."""
        amount = self.get_amount("Deposit Money")
        if amount and amount > 0:
            self.show_loading("Depositing money")
            self.users[self.current_user]['accounts']['savings'] += amount
            self.users[self.current_user]['transaction_history'].append(f"Deposited: ₹{amount:,}")
            messagebox.showinfo("Success", f"Deposited ₹{amount:,}.\nNew Balance: ₹{self.users[self.current_user]['accounts']['savings']:,}")
        else:
            messagebox.showerror("Error", "Deposit amount must be positive!")

    def withdraw_money(self):
        """Withdraw money from the user's savings account, enforcing daily limit."""
        amount = self.get_amount("Withdraw Money")
        if amount:
            if amount > self.users[self.current_user]['accounts']['savings']:
                messagebox.showerror("Error", "Insufficient balance!")
            elif amount <= 0:
                messagebox.showerror("Error", "Withdrawal amount must be positive!")
            elif self.withdrawn_today + amount > self.daily_withdrawal_limit:
                messagebox.showerror("Error", f"Exceeded daily limit of ₹{self.daily_withdrawal_limit:,}. You have already withdrawn ₹{self.withdrawn_today:,} today.")
            else:
                self.show_loading("Withdrawing money")
                self.users[self.current_user]['accounts']['savings'] -= amount
                self.withdrawn_today += amount
                self.users[self.current_user]['transaction_history'].append(f"Withdrew: ₹{amount:,}")
                messagebox.showinfo("Success", f"Withdrew ₹{amount:,}.\nNew Balance: ₹{self.users[self.current_user]['accounts']['savings']:,}")

    def show_history(self):
        """Display the user's transaction history."""
        history_window = tk.Toplevel(self.root)
        history_window.title("Transaction History")
        history_window.geometry("400x300")
        history_window.configure(bg="#23272A")

        # Center the history window
        history_window.eval('tk::PlaceWindow %s center' % history_window.winfo_toplevel())

        if self.users[self.current_user]['transaction_history']:
            history_label = tk.Label(history_window, text="Transaction History:", font=("Times New Roman", 14), bg="#23272A", fg="#7289DA")
            history_label.pack(pady=10)

            history_text = tk.Text(history_window, width=50, height=13, fg="white", bg="#23272A", font=("Times New Roman", 12), wrap=tk.WORD)
            history_text.pack(pady=10)
            
            for transaction in self.users[self.current_user]['transaction_history']:
                history_text.insert(tk.END, f"{transaction}\n")
                
            history_text.config(state=tk.DISABLED)
        else:
            no_history_label = tk.Label(history_window, text="No transaction history available.", font=("Times New Roman", 12), bg="#23272A", fg="white")
            no_history_label.pack(pady=20)

    def export_history(self):
        """Export the user's transaction history to a CSV file."""
        filename = f"{self.current_user}_transaction_history.csv"
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Transaction History"])
                writer.writerow([])  # Add an empty row for spacing
                for transaction in self.users[self.current_user]['transaction_history']:
                    writer.writerow([transaction])
            messagebox.showinfo("Export Successful", f"Transaction history exported to {filename}.")
        except Exception as e:
            messagebox.showerror("Export Failed", f"An error occurred: {e}")

    def change_pin(self):
        """Allow the user to change their PIN."""
        new_pin = simpledialog.askstring("Change PIN", "Enter new PIN:", show="*")
        if new_pin:
            if len(new_pin) != 4 or not new_pin.isdigit():
                messagebox.showerror("Error", "PIN must be 4 digits!")
            else:
                self.users[self.current_user]['pin'] = new_pin
                messagebox.showinfo("Success", "PIN changed successfully!")
        else:
            messagebox.showerror("Error", "PIN change was cancelled.")

    def get_amount(self, title):
        """Prompt the user for an amount and validate it."""
        try:
            amount = simpledialog.askinteger(title, "Enter amount (₹):")
            if amount is None:
                return None
            if amount < 0:
                raise ValueError
            return amount
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive amount.")
            return None

    def minimize_window(self):
        """Minimize the ATM window."""
        self.root.iconify()

    def maximize_window(self):
        """Maximize the ATM window."""
        self.root.state('zoomed')

if __name__ == "__main__":
    users = {
        "kaviya": {
            "pin": "1234",
            "accounts": {"savings": 50000},
            "transaction_history": []
        },
        "jashini": {
            "pin": "5678",
            "accounts": {"savings": 80000},
            "transaction_history": []
        }
    }

    root = tk.Tk()
    app = ATM(root, users)
    root.mainloop()  
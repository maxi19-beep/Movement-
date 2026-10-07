# ==============================================
# Simple App Simulation - Account & Home Screen
# ==============================================

def create_account():
    print("\n" + "="*40)
    print("        📝 CREATE YOUR ACCOUNT")
    print("="*40)
    
    name = input("Enter your Full Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone Number: ")
    password = input("Create a Password: ")
    
    print("\n✅ Account Created Successfully! 🎉")
    print(f"Welcome aboard, {name}!")
    input("\nPress Enter to go to Home Screen...")
    return name


def home_screen(username):
    while True:
        print("\n" + "="*40)
        print(f"       🏠 HOME SCREEN — Hi {username}")
        print("="*40)
        print("  1. 📊 View Dashboard")
        print("  2. 👤 My Profile")
        print("  3. 💳 My Wallet")
        print("  4. ⚙️ Settings")
        print("  5. 📢 Notifications")
        print("  6. ❓ Help & Support")
        print("  0. 🔙 Logout")
        print("="*40)
        
        choice = input("Enter your choice (0-6): ")
        
        if choice == "1":
            print("\n📊 Opening Dashboard...")
        elif choice == "2":
            print("\n👤 Opening Your Profile...")
        elif choice == "3":
            print("\n💳 Opening Wallet...")
        elif choice == "4":
            print("\n⚙️ Opening Settings...")
        elif choice == "5":
            print("\n📢 No new notifications")
        elif choice == "6":
            print("\n❓ Need help? Contact support@app.com")
        elif choice == "0":
            print("\n👋 Logged out successfully. Bye!")
            break
        else:
            print("\n❌ Invalid choice, try again")
        
        input("\nPress Enter to continue...")


def main():
    print("\n" + "🎯"*20)
    print("      WELCOME TO MY APP")
    print("🎯"*20)
    print("\n1. Create New Account")
    print("2. Skip & See Home Screen")
    
    pick = input("\nWhat do you want to do? (1 or 2): ")
    
    if pick == "1":
        user_name = create_account()
        home_screen(user_name)
    elif pick == "2":
        home_screen("Guest")
    else:
        print("\n❌ Wrong option. Restart the program.")


# RUN THE PROGRAM
if __name__ == "__main__":
    main()

# ==============================================
# UPGRADED: All 6 Menu Options Now Work!
# ==============================================

def create_account():
    print("\n" + "="*40)
    print("        📝 CREATE YOUR ACCOUNT")
    print("="*40)
    
    name = input("Enter your Full Name: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone Number: ")
    password = input("Create a Password: ")
    
    print("\n✅ Account Created Successfully! 🎉")
    print(f"Welcome aboard, {name}!")
    input("\nPress Enter to go to Home Screen...")
    return name


# ========== ALL 6 MENU PAGES ==========
def page_dashboard():
    print("\n" + "━"*40)
    print("📊 📈 YOUR DASHBOARD")
    print("━"*40)
    print("  Total Income:    ₦ 45,200.00")
    print("  Total Expenses:  ₦ 12,800.00")
    print("  Active Tasks:    7")
    print("  Completed:       23")
    print("  Status:          ✅ Good Standing")
    print("━"*40)


def page_profile(username):
    print("\n" + "━"*40)
    print(f"👤 PROFILE — {username}")
    print("━"*40)
    print("  Name:      ", username)
    print("  Email:      user@example.com")
    print("  Phone:      080-XXX-XXXX")
    print("  Member Since: Oct 2026")
    print("  Status:      ⭐ Regular Member")
    print("━"*40)


def page_wallet():
    print("\n" + "━"*40)
    print("💳 MY WALLET")
    print("━"*40)
    print("  Balance:       ₦ 32,400.00")
    print("")
    print("  🔹 1. Deposit Funds")
    print("  🔹 2. Withdraw Funds")
    print("  🔹 3. Transaction History")
    print("  🔹 4. Linked Cards")
    print("━"*40)


def page_settings():
    print("\n" + "━"*40)
    print("⚙️ SETTINGS")
    print("━"*40)
    print("  🔹 1. Edit Profile")
    print("  🔹 2. Change Password")
    print("  🔹 3. Notification Settings")
    print("  🔹 4. Dark Mode:   OFF")
    print("  🔹 5. Language:    English")
    print("  🔹 6. Delete Account")
    print("━"*40)


def page_notifications():
    print("\n" + "━"*40)
    print("📢 NOTIFICATIONS")
    print("━"*40)
    print("  📅 Today — System update complete")
    print("  ✅ 2 days ago — Withdrawal successful")
    print("  ℹ️ 3 days ago — New features added")
    print("  💡 1 week ago — Welcome message")
    print("━"*40)


def page_help():
    print("\n" + "━"*40)
    print("❓ HELP & SUPPORT")
    print("━"*40)
    print("  📧 Email:    support@myapp.com")
    print("  📞 Call:     0800-123-4567")
    print("  💬 WhatsApp: +234-XXX-XXXXXXX")
    print("  🕒 Hours:    Mon-Fri, 8AM - 6PM")
    print("  🌐 Website:  www.myapp.com/help")
    print("━"*40)


# ========== HOME SCREEN ==========
def home_screen(username):
    while True:
        print("\n" + "="*40)
        print(f"       🏠 HOME SCREEN — Hi {username}")
        print("="*40)
        print("  1. 📊 Dashboard")
        print("  2. 👤 My Profile")
        print("  3. 💳 My Wallet")
        print("  4. ⚙️ Settings")
        print("  5. 📢 Notifications")
        print("  6. ❓ Help & Support")
        print("  0. 🔙 Logout")
        print("="*40)
        
        choice = input("Enter your choice (0-6): ")
        
        if choice == "1":
            page_dashboard()
        elif choice == "2":
            page_profile(username)
        elif choice == "3":
            page_wallet()
        elif choice == "4":
            page_settings()
        elif choice == "5":
            page_notifications()
        elif choice == "6":
            page_help()
        elif choice == "0":
            print("\n👋 Logged out successfully. Bye!")
            break
        else:
            print("\n❌ Invalid choice! Please enter 0-6")
        
        input("\nPress Enter to go back to Home Screen...")


def main():
    print("\n" + "🎯"*20)
    print("      WELCOME TO MY APP")
    print("🎯"*20)
    print("\n1. Create New Account")
    print("2. Skip & See Home Screen")
    
    pick = input("\nWhat do you want to do? (1 or 2): ")
    
    if pick == "1":
        user_name = create_account()
        home_screen(user_name)
    elif pick == "2":
        home_screen("Guest")
    else:
        print("\n❌ Wrong option. Restart the program.")


# RUN THE PROGRAM
if __name__ == "__main__":
    main()

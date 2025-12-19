from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Wichtige Imports für die Eingabe von Text
from email_generator import EmailGenerator
import random
import string
import json


class AccountManager:
    def __init__(self, driver=None):
        if driver is None:
            self.driver = webdriver.Firefox()
        else:
            self.driver = driver

    def open_site(self, url):
        self.driver.get(url)
        sleep(1)

    def click_signup_button(self):
        sign_up_btn = self.driver.find_element(by=By.CSS_SELECTOR, value=".navigation-auth_signup-button")
        sleep(1)
        sign_up_btn.click()

    def fill_signup_form(self, email, pw):
        email_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="input.field-0-2-88:nth-child(1)")
        pw_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="input.field-0-2-88:nth-child(2)")
        policy_btn = self.driver.find_element(by=By.CSS_SELECTOR, value="label.label-0-2-92:nth-child(2) > span:nth-child(2) > span:nth-child(2)")

        email_btn.click()
        sleep(0.5)
        email_btn.send_keys(email)
        sleep(1)

        pw_btn.click()
        sleep(0.5)
        pw_btn.send_keys(pw)
        sleep(1)

        policy_btn.click()
        sleep(1)

    def submit_signup_form(self):
        final_signup_button = self.driver.find_element(by=By.CSS_SELECTOR, value=".button-0-2-75")
        final_signup_button.click()

    def customize_profile(self, nickname):
        self.open_site("https://www.codingame.com/settings")
        sleep(2)

        # Versuche den Nickname-Eingabefeld zu finden (möglicherweise ein <input>-Tag)
        try:
            nicknamebox = self.driver.find_element(by=By.CSS_SELECTOR, value="input[name='gamertag']")  # Beispiel Selektor
            nicknamebox.clear()  # Lösche den aktuellen Wert
            nicknamebox.send_keys(nickname)  # Setze den neuen Nickname
            nicknamebox.send_keys(Keys.RETURN)  # Sende die Eingabe
            sleep(2)  # Gib der Seite Zeit, die Änderungen zu speichern
        except Exception as e:
            print("Fehler beim Anpassen des Nicknames:", e)

    def create_account(self, email, pw, nickname):
        self.open_site("https://www.codingame.com/multiplayer/clashofcode")
        self.click_signup_button()
        self.fill_signup_form(email, pw)
        self.submit_signup_form()
        sleep(4)  # Warte, bis das Konto erstellt wurde
        self.customize_profile(nickname)  # Nickname ändern
        return {"email": email, "password": pw, "nickname": nickname}

    def close_driver(self):
        self.driver.quit()

    def save_to_json(self, accounts, filename="accounts.json"):
        with open(filename, 'w') as f:
            json.dump(accounts, f, indent=4)

    def generate_password(self, length=12):
        return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))


def create_multiple_accounts(num_accounts=5):
    email_generator = EmailGenerator()
    account_manager = AccountManager()

    accounts = []
    for _ in range(num_accounts):
        email = email_generator.generate_random_email()
        password = account_manager.generate_password()
        nickname = f"nickname{random.randint(1000, 9999)}"
        account_info = account_manager.create_account(email, password, nickname)
        accounts.append(account_info)

    account_manager.save_to_json(accounts)
    # account_manager.close_driver()  # Optional, wenn du den WebDriver schließen willst

    print(f"{num_accounts} accounts were created and saved to 'accounts.json'.")


if __name__ == "__main__":
    create_multiple_accounts(1)
import datetime
import time

# Dictionary of French months
french_months = {
   1: "janvier",
   2: "février", 
   3: "mars",
   4: "avril",
   5: "mai",
   6: "juin",
   7: "juillet",
   8: "août",
   9: "septembre",
   10: "octobre",
   11: "novembre",
   12: "décembre"
}

# Get current month and year
now = datetime.datetime.now()
month = french_months[now.month]
year = now.year

# Write email subject
keyboard.send_keys(f"Fiche de paie {month} {year}")

# Move focus to email body 
keyboard.send_key("<tab>")
time.sleep(0.2)

# Email body template
message = f"""Bonjour Magalie,

En PJ la fiche de paie pour le mois de {month}.

Bonne journée,"""

keyboard.send_keys(message)
# Write email subject
keyboard.send_keys(f"Facture XXX")

# Move focus to email body 
keyboard.send_key("<tab>")

# Email body template
message = f"""Bonjour NOM,

En PJ la facture XXX.

Bonne journée,"""

keyboard.send_keys(message)

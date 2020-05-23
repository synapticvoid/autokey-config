text = clipboard.get_selection()
keyboard.send_key("<delete>")
keyboard.send_keys("```{}\n\n```".format(text))
keyboard.send_key("<up>")

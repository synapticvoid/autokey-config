text = clipboard.get_selection()
keyboard.send_keys('<ctrl>+t')

keyboard.send_keys(f' {text}')
keyboard.send_key('<enter>')
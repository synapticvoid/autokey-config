text = clipboard.get_selection()
url = clipboard.get_clipboard()
keyboard.send_key("<delete>")
keyboard.send_keys("[{text}]({url})".format(
                    text=text,          
                    url=url))
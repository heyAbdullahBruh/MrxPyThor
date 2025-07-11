from universalChecker import matchResult
pattern = r"\b[a-z0-9]+(?:\.[a-z0-9]+)*@+[a-z]+\.+[a-z]{2,10}\b"
text ="abus11@gmail.com"
matchResult(pattern,text)
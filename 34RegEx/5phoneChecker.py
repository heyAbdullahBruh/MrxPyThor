from universalChecker import matchResult

# pattern = r"\b8801[3,9][0-9]{8}+\b" #BD
pattern = r"\b1(\d{3})-?\s?\d{3}-\d{4}\b" #US
text ="1334-567-8900"
matchResult(pattern,text)
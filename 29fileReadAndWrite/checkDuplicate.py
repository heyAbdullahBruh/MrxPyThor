fileW = open("res.txt","a")

emails =["Nagel4Vegas@gmail.com","sandraceciliapolanco@gmail.com","HassielG@gmail.com","djanderson86@gmail.com","iam.brittanynicolesmith@gmail.com","Nagel4Vegas@gmail.com","Javierzamora05@gmail.com.","Teamcannonbooking@gmail.com","lmtayl3@gmail.com.","londonerrockwall@gmail.com.","Reneegula91@gmail.com","janiyahfox@gmail.com","horacionarvaez2307@gmail.com","Javierzamora05@gmail.com.","sandraceciliapolanco@gmail.com"]
modified =[]
i = 0
while i< len(emails):
    if emails[i] not in modified :
        modified.append(emails[i])
    i=i+1
    
i=0
while i < len(modified) :
    fileW.write(f"\n{modified[i]}")
    i=i+1
    
print(len(modified))
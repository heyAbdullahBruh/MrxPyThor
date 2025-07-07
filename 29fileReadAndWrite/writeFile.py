
'''
# Write file using append --> 
file = open('hello.txt','a') # if add a new line and save prev value in file use a(appped)
file.write("\nI am abdullah saye")

# Write file using write --> 
file = open('hello.txt','w') # if add a new line and cut prev value in file use w(write)
file.write("I am abdullah saye")
'''
fileHtml = open('index.html','a')

fileHtml.write("<!DOCTYPE html>")
fileHtml.write("\n <html lang='en'>")
fileHtml.write("\n <head>")
fileHtml.write("\n \t title>Create Html file with Python</title>")
fileHtml.write("\n </head>")
fileHtml.write("\n </body>")
fileHtml.write("\n \t <h1>Hello Python</h1>")
fileHtml.write("\n </body> ")
fileHtml.write("\n </html> ")

fileHtml.close()
from urllib. request import urlopen

# Link to website api
link = 'https://wttr.in/Perth?A'

# Gets url and opens it
wget = urlpoen(link)

# Gets whats on website in clear text
webtext = wget.read()

#Print it to the screen 
print(webtext.decode(' utf-8'))
import requests
print(requests.__version__)

requests.get("https://www.google.com/")

# display raw source code
r = requests.get("https://github.com/ava-g/cmput404-lab1/blob/master/lab1.py")
print(r.text)

# write to file to display retrieved html website
file = open('out.html','w')
file.write(r.text)
file.close()

import re

fic = "c:\\tmp\\data\\jenkins.json"
data = ""

def main():
    # Open file and read each line
    with open(fic, "r") as fileHandler:
        for line in fileHandler:
            data = line
            print(data.strip()) # strip new line character
# Create a pattern to match string
patternObj = re.compile(data)

# search for the pattern in the string and return the match object
matchObj = patternObj.search(data)

# check if match object is not Null
if matchObj:
    print('Sub-string Found')
else:
    print('Sub-string Not Found')


if __name__ == '__main__':
    main()

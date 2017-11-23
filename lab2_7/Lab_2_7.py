# Create file object for write only
f = open('myfile.txt','w')
# Write into file
f.write("Hello file world!")
# Close file with saving it's content
f.close()

# Create file object for read and write
f = open('myfile.txt','r+')
# Read and print file content
print(f.read())
f.seek(len("Hello "))
f.write("my " + "file world!") # Try it with "my file" and you will see how work data update in files
f.flush()

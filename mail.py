import re
input_file = raw_input("Input File: ")
output_file = raw_input("Output File: ")
open(output_file, 'a+').close()

def saver(data,file_name):
    data = list(set(data))
    print 'A collection of ', len(data), 'is being saved now ...'
    for line in data:
        if line not in open(file_name, 'r').read():
            open(file_name, 'a+').write(line + '\n')

mailsFound = []
with open(input_file) as file_data:
    for line in file_data:
        line = line.lower()
        li = re.findall('[a-z0-9._]+@[a-z0-9.-]+', line)
        mailsFound.extend(li)
        li[:] = []
        #save 20000 mails when reached and clear the list to save memory
        if len(mailsFound) == 20000:
            saver(mailsFound, output_file)
            mailsFound[:] = []
print 'Scan complete!'
print 'Saving to file ...'
saver(mailsFound, output_file)
print 'Saved successfully to', output_file

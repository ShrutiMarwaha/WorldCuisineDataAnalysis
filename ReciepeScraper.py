import urllib2
import os

# Step-1: Get the whole website & extract .txt links of cuisine.
# wget --mirror --convert-links --adjust-extension --page-requisites --no-parent www.recipesource.com

# Step-2: Another round of wget to extract all the contents.
RECIEPES = "/Users/shruti/websites/cuisine_links.txt"

reciepe_lines = []
with open(RECIEPES) as f:
    reciepe_lines = f.readlines()

reciepe_lines = [x.strip('\n') for x in reciepe_lines]

for reciepe in reciepe_lines:
    print "processing: %s \n" % reciepe
    output_file_name = reciepe.replace("http://recipesource.com/text", "/Users/shruti/reciepesource")

    response = urllib2.urlopen(reciepe)
    html = response.read()

    output_directory = os.path.dirname(output_file_name)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_file = open(output_file_name, 'w')
    output_file.write(html)
    output_file.close()

print "Processing Done!"
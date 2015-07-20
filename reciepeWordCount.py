import re
import os
import operator

reciepe_files = []
reciepe_directory = "/Users/shruti/reciepesource/ethnic/asia"
for root, dirs, files in os.walk(reciepe_directory):
    for file in files:
        if file.endswith(".txt"):
             reciepe_files.append(os.path.join(root, file))

wordHistogram = {}
for filename in reciepe_files:

    # 1st Step: Processing the file.
    file_object = open(filename, 'r')
    file_contents = file_object.read()
    #print("Printing file: " + file_contents)

    # 2nd Step: Finding words.
    words = re.split('\s+', file_contents)
    #print("Printing words from Array:")
    #print(words)

    #3th Step: Finding Histogram.
    #print("Adding to Historgram")
    for word in words:
        word = word.strip().lower()
        if len(word) > 0:
            if word in wordHistogram:
                wordHistogram[word] += 1
            else:
                wordHistogram[word] = 1

    file_object.close()

histogram_output_file = reciepe_directory + "/wordcount.dat"
writer = open(histogram_output_file, 'w')

#common = ['salt','sugar','butter','rice','beans','wheat','oil','pepper','egg','lemon','mushroom']
for key, value in wordHistogram.iteritems():
    writer.write(str(key) + '\t' + str(value) + "\n")
#
#    if key in common:
#        print str(key) + '\t' + str(value) + "\n"

# Get Top 100 words sorted by frequency.
top = sorted(wordHistogram.iteritems(), key=operator.itemgetter(1), reverse=True)[:100]
for key, value in top:
    print(str(key) + '\t' + str(value) + "\n")


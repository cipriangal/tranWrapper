from PIL import Image
import sys

import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
print("Available tools:", tools)
# Ex: Will use tool 'libtesseract'

###langs = tool.get_available_languages()
###print("Available languages: %s" % ", ".join(langs))
###nLang = 0
###for language in langs:
###    ##print(nLang,language)
###    if language == "ron":
###        break
###    nLang+=1
###
###lang = langs[nLang]
###print("Will use lang '%s'" % (lang))

line_and_word_boxes = tool.image_to_string(
    Image.open('./input/1pg.png'), lang="ron",
    builder=pyocr.builders.LineBoxBuilder())

for line in line_and_word_boxes:
    for wordBox in line.word_boxes:
        print(wordBox.position, ">>> ", wordBox.content, " <<<<", wordBox.confidence)


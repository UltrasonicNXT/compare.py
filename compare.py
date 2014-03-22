import re, os

originalpath = 'c:/users/adam/prog/resources/wf'
rewritepath = 'c:/users/adam/prog/wikimedia/mediawiki-core/extensions/WikiForum'

originaltext = ''

for filename in os.listdir(originalpath):
    if filename.endswith('.php'):
        f = open(originalpath + '/' + filename, 'r')
        originaltext += f.read()
        f.close()

rewritetext = ''

for filename in os.listdir(rewritepath):
    if filename.endswith('.php'):
        f = open(rewritepath + '/' + filename, 'r')
        rewritetext += f.read()
        f.close()

pattern = re.compile('/\*.+?\*/', re.DOTALL)
originaltext = re.sub(pattern, '', originaltext)
rewritetext = re.sub(pattern, '', rewritetext)

def countline(line):
    line = ''.join(line.split()) #remove all whitespace
    line = line.replace('}', '').replace(')', '').replace(';', '') #remove pointles chars

    if not len(line):
        return 0

    if line.startswith('//') or line.startswith('#'):
        return 0

    return 1

originallines = 0

for line in originaltext.splitlines():
    originallines += countline(line)

rewritelines = 0

for line in rewritetext.splitlines():
    rewritelines += countline(line)

print "Original:", originallines
print "Rewrite:", rewritelines

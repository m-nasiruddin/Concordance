import subprocess
import sys

devnull = open("/dev/null", "w")
output = subprocess.Popen(["/usr/bin/scp", 'BatchFeatureExtractor.py', 'SimpleFeatureExtractor.py', 'InfoSemCor.py',
                           "nasirudd@bach1:" + sys.argv[1]], stderr=subprocess.PIPE,
                          stdout=subprocess.PIPE).communicate()[0]
print(output)
import re
import os
with open("../vectordrawable/res/values/attrs.xml") as infile:
	attrsFile = infile.read()
	attribs = re.findall(r'name="([^"]*)"', attrsFile)

a2 = []
for a in attribs:
	if not "android:" in a:
		a2.append(("android:" + a, "vec:" + a))
a2.append(('xmlns:android="http://schemas.android.com/apk/res/android"', 
	'xmlns:android="http://schemas.android.com/apk/res/android" xmlns:vec="http://schemas.android.com/apk/res-auto"'))
a2.append(('<vector', '<net.zhuoweizhang.vectordrawable.VectorDrawable'))
a2.append(('</vector', '</net.zhuoweizhang.vectordrawable.VectorDrawable'))
a2.append(('xmlns:android="http://schemas.0android.0com/apk/res/android"', 
	'xmlns:android="http://schemas.android.com/apk/res/android" xmlns:vec="http://schemas.android.com/apk/res-auto"'))

for folder in os.walk("res_preproc"):
	for filename in folder[2]:
		path = folder[0] + "/" + filename
		with open(path) as infile:
			outContents = infile.read()
		for a in a2:
			outContents = outContents.replace(a[0], a[1])
		print(outContents)
		with open(path.replace("res_preproc", "res"), "w") as outfile:
			outfile.write(outContents)

import os
while True:
	a=input(">>>")
	if a=="new":
		os.system(f"hexo new {input('type:')} {input('name:')}")
	else:
		os.system(f"hexo new {input('name:')}")

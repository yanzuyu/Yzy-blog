import os
while True:
	a=input(">>>")
	try:
		if a.split()[0]=="start":
			b=a.split()[1]
			os.startfile(f"\"source\\_posts\\{b}.md\"")
		elif a=="new":
			a=input('type:')
			b=input('name:')
			os.system(f"hexo new {a} {b}")
			os.startfile(f"\"source\\{a}\\{b}.md\"")
		else:
			b=a
			os.system(f"hexo new {b}")
			os.startfile(f"\"source\\_posts\\{b}.md\"")
	except:
		...
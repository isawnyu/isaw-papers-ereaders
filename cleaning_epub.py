########################################################################################

### DO NOT LAUNCH THAT SCRIPT : IT IS AUTOMATICALLY LAUMCHED BY THE BAHS SCRIPT #######

########################################################################################

from bs4 import BeautifulSoup
import re
import os
import shutil

""" Make the appropriate changes in the html encoding in order to be able to prduce a satisfying ePub
	
	:param soup: the article that we want to clean
	:type soup: BeautifulSoup object
	:return soup: Same object but cleaned
	"""
def cleaning(soup):
	if soup.header and soup.header.h2 :
		h2_header = soup.header.find_all('h2')
		for h2 in h2_header :
			h2.name = 'div'
	
	css = soup.find("link", {"rel" : re.compile("stylesheet*")})
	css['href']= '../isaw-ereaders.css'
	
	#getting rid of h2 in order to avoid page break 
	h4s = soup.find_all('h4')
	for h4 in h4s :
		h4.name = 'h5'
	
	h3s = soup.find_all('h3')
	for h3 in h3s :
		h3.name = 'h4'
	
	h2s = soup.find_all('h2')
	for h2 in h2s :
		h2.name = 'h3'
	
	# adding alt to the images that have figcaptions
	images = soup.find_all("figure")

	for image in images :
		if image.figcaption :
			alternative = image.figcaption.get_text()
		if image.img :
			try :
				image.img["alt"]=alternative
			except :
				print("already an alt")
	# links to the full size images 
	for image in images :
		if image.img :
			caption = image.figcaption
			try :
				ids = image["id"]
			except KeyError :
				try :
					ids = image.img["id"]
				except:
					try :
						ids = image.p["id"]
					except :
						print ("id not found")
			if caption :
				caption.append('<br/><a href="http://dlib.nyu.edu/awdl/isaw/isaw-papers/'+str(i)+'/#'+ids+'">Full size image here ↗</a>')
			else :
				image.append('<br/><a href="http://dlib.nyu.edu/awdl/isaw/isaw-papers/'+str(i)+'/#'+ids+'">Full size image here ↗</a>')

	soup = str(soup).replace("&gt;", ">")
	soup = str(soup).replace("&lt;", "<")
	return soup 



def copy_pictures() : 
	"""Copy the pictures from isaw-papers submodules into the isaw-papers-ereaders directories
	"""

	if os.path.isdir("isaw-papers/isaw-papers-"+str(i)+"/images"):
		if os.path.isdir(str(i)+"/images"):
			shutil.rmtree(str(i)+"/images")
		shutil.copytree("isaw-papers/isaw-papers-"+str(i)+"/images", str(i)+"/images")


def video_11() :
	"""Replace videos in ISAW Papers 11 by link to the online version of the ebook
	"""
	with open('11/isaw-papers-11-ereaders.xhtml', 'r') as paper:
		isawPaper = paper.read()
		isawPaper = isawPaper.replace('animations/','http://dlib.nyu.edu/awdl/isaw/isaw-papers/11/animations/')
		isawPaper = isawPaper.replace('<video controls="yes" width="100%">','')
		isawPaper = isawPaper.replace('</video>','')
		isawPaper = isawPaper.replace('Your browser does not support the video tag.','')
		soup = BeautifulSoup(isawPaper)

	sources_webm = soup.find_all("source", {"type":"video/webm"})
	for source_webm in sources_webm :
		source_webm.decompose()
		
	sources = soup.find_all("source")
	for source in sources :
		source.name="a"
		del source["type"]
		source["href"] = source["src"]
		del source["src"]
		source.append("Click here for the link")

	soup.prettify()

	with open('11/isaw-papers-11-ereaders.xhtml', 'w') as paper:
		paper.write(str(soup))


# applying all of the changes

for i in range(1, 14):
	with open('isaw-papers/isaw-papers-'+str(i)+'/isaw-papers-'+str(i)+'.xhtml') as paper:

		# manual change of all the links in ISAW Papers 7
		text = paper.read()
		text = text.replace("elliott-heath-muccigrosso/", "elliott-heath-muccigrosso/isaw-papers-7-1.xhtml")
		text = text.replace("acheson/", "acheson/isaw-papers-7-2.xhtml")
		text = text.replace("almas-babeu-krohn/", "almas-babeu-krohn/isaw-papers-7-3.xhtml")
		text = text.replace("benefiel-sprenkle/", "benefiel-sprenkle//isaw-papers-7-4.xhtml")
		text = text.replace("blackwell-smith/", "blackwell-smith//isaw-papers-7-5.xhtml")
		text = text.replace("elliott-jones/", "elliott-jones/isaw-papers-7-6.xhtml")
		text = text.replace("hafford/", "hafford/isaw-papers-7-7.xhtml")
		text = text.replace("heath/", "heath/isaw-papers-7-8.xhtml")
		text = text.replace("horne/", "horne/isaw-papers-7-9.xhtml")
		text = text.replace("kansa/", "kansa/isaw-papers-7-10.xhtml")
		text = text.replace("lana/", "lana/isaw-papers-7-11.xhtml")
		text = text.replace("liuzzo/", "liuzzo/isaw-papers-7-12.xhtml")
		text = text.replace("mackay/", "mackay/isaw-papers-7-13.xhtml")
		text = text.replace("mcmichael/", "mcmichael/isaw-papers-7-14.xhtml")
		text = text.replace("meadows-gruber/", "meadows-gruber/isaw-papers-7-15.xhtml")
		text = text.replace("meyers/", "meyers/isaw-papers-7-16.xhtml")
		text = text.replace("murray/", "murray/isaw-papers-7-17.xhtml")
		text = text.replace("nurmikko-fuller/", "nurmikko-fuller/isaw-papers-7-18.xhtml")
		text = text.replace("pearce-schmitz/", "pearce-schmitz/isaw-papers-7-19.xhtml")
		text = text.replace("pett/", "pett/isaw-papers-7-20.xhtml")
		text = text.replace("poehler/", "poehler/isaw-papers-7-21.xhtml")
		text = text.replace("rabinowitz/", "rabinowitz/isaw-papers-7-22.xhtml")
		text = text.replace("reinhard/", "reinhard/isaw-papers-7-23.xhtml")
		text = text.replace("romanello/", "romanello/isaw-papers-7-24.xhtml")
		text = text.replace("roueche-lawrence-lawrence/", "roueche-lawrence-lawrence/isaw-papers-7-25.xhtml")
		text = text.replace("seifried/", "seifried/isaw-papers-7-26.xhtml")
		text = text.replace("simon-barker-desoto-isaksen/", "simon-barker-desoto-isaksen/isaw-papers-7-27.xhtml")
		text = text.replace("taylor/", "taylor/isaw-papers-7-28.xhtml")
		text = text.replace("tsonev/", "tsonev/isaw-papers-7-29.xhtml")
		text = text.replace("vankeer/", "vankeer/isaw-papers-7-30.xhtml")

		soup = BeautifulSoup(text, "lxml")
		soup = cleaning(soup)
		copy_pictures()

	with open(str(i)+'/isaw-papers-'+str(i)+'-ereaders.xhtml', 'w') as paper:
		paper.write(str(soup))
		print("ISAW Papers" + str(i) + "is ready")
video_11()


	

	
# applying the changes to all the files of ISAW Papers 7 
for element in os.listdir('isaw-papers/isaw-papers-7'):
	if os.path.isdir('isaw-papers/isaw-papers-7/'+ str(element)):
		if not os.path.isdir('7/'+str(element)):
			shutil.copytree('isaw-papers/isaw-papers-7/'+ str(element), '7/'+str(element))
		for el in os.listdir('isaw-papers/isaw-papers-7/'+ str(element)):
			if re.match("isaw-papers-7-*", str(el)):
				with open ('isaw-papers/isaw-papers-7/'+ str(element) + '/'+ str(el), "r") as paper : 
					soup = BeautifulSoup(paper, "lxml")
					soup = cleaning(soup)
					el = el.replace(".xhtml", "-ereaders.xhtml")
				with open('7/'+ str(element)+'/' + str(el), 'w') as paper:
					paper.write(str(soup))


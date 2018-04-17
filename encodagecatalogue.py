with open("catalogue.sql","r",encoding="utf-8") as f, open("catalogueencode.sql","w",encoding="utf-8") as g:

	for lines in f:

		laligne=""
		
		i=0
		
		while i < len(lines):
			
			if lines[i]=="Ã":
				
				i=i+1
				
				if lines[i]=="©":
					é=lines[i-1]+lines[i]
					laligne=laligne+"é"
					#c'est le é
				elif lines[i]=="¨":
					è=lines[i-1]+lines[i]
					laligne=laligne+"è"
					#c'est le è
				elif lines[i]=="§":
					ç=lines[i-1]+lines[i]
					laligne=laligne+"ç"
					#c'est le ç
				elif lines[i]=="¶":
					ö=lines[i-1]+lines[i]
					laligne=laligne+"ö"
					#c'est le ö
				elif lines[i]=="¤" or lines[i]=="¼":
					ä=lines[i-1]+lines[i]
					laligne=laligne+"ä"
					#c'est le ä
				elif lines[i]=="¸":
					ø=lines[i-1]+lines[i]
					laligne=laligne+"ø"
					#c'est le ø
				elif lines[i]=="«":
					ë=lines[i-1]+lines[i]
					laligne=laligne+"ë"
					#c'est le ë
				elif lines[i]=="‰":
					É=lines[i-1]+lines[i]
					laligne=laligne+"É"
					#c'est le É
				elif lines[i]=="¹":
					ù=lines[i-1]+lines[i]
					laligne=laligne+"ù"
					#c'est le ù
				elif lines[i]=="ª":
					ê=lines[i-1]+lines[i]
					laligne=laligne+"ê"
					#c'est le ê
				elif lines[i]=="®":
					î=lines[i-1]+lines[i]
					laligne=laligne+"î"
					#c'est le î
				elif lines[i]=="¢":
					â=lines[i-1]+lines[i]
					laligne=laligne+"â"
					#c'est le â
				elif lines[i]=="¯":
					ï=lines[i-1]+lines[i]
					laligne=laligne+"ï"
					#c'est le ï
				elif lines[i]=="´":
					ô=lines[i-1]+lines[i]
					laligne=laligne+"ô"
					#c'est le ô
				elif lines[i]=="¡":
					á=lines[i-1]+lines[i]
					laligne=laligne+"á"
					#c'est le á
				elif lines[i]=="Ÿ":
					ß=lines[i-1]+lines[i]
					laligne=laligne+"ß"
					#c'est le ß
				elif lines[i]=="–":
					œ=lines[i-1]+lines[i]
					laligne=laligne+"œ"
					#c'est le œ
				elif lines[i]=="ˆ":
					È=lines[i-1]+lines[i]
					laligne=laligne+"È"
					#c'est le È
				elif lines[i]=="»":
					û=lines[i-1]+lines[i]
					laligne=laligne+"û"
					#c'est le û
				elif lines[i]==" ":
					à=lines[i-1]+lines[i]
					laligne=laligne+"à"
					#c'est le à

			else:
				laligne=laligne+lines[i]
		
			i=i+1
		
		g.write(laligne)
	
	


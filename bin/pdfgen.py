from reportlab.pdfgen import canvas
from pickle import *

class GenerarPdf():
	def __init__(self, datos):
		info = open("bin/src/sbu.bin", "rb")
		valor = load(info)
		info.close()
		nombre = datos[0]
		nombres = "Multas Generadas/"+nombre+".pdf"
		c = canvas.Canvas(nombres)
		c.drawImage("bin/img/ttmp.png", 30, 770, 250, 40)
		c.drawImage("bin/img/ttmp.png", 30, 340, 250, 40)
		c.setFont("Times-Bold", 12)
		numeroBoleta = "BOLETA DE SANCIÓN N° "+ datos[0]
		c.drawString(290,770,numeroBoleta)
		c.drawString(290,340,numeroBoleta)
		c.setFont("Times-Bold", 12)
		
		c.drawString(30,740,"COOPERATIVA: ")
		c.rect(125,740,260,18)
		c.drawString(30,310,"COOPERATIVA: ")
		c.rect(125,310,260,18)
		c.setFont("Times-Roman", 14)
		c.drawString(150,740, datos[1])
		c.drawString(150,310, datos[1])
		c.setFont("Times-Bold", 12)
		
		c.drawString(395,740,"FECHA: ")
		c.drawString(395,310,"FECHA: ")
		c.rect(450,740,100,18)
		c.rect(450,310,100,18)
		c.setFont("Times-Roman", 14)
		fecha_nueva = datos[3][8:10]+"-"+datos[3][5:7]+"-"+datos[3][0:4]
		c.drawString(460,740, fecha_nueva)
		c.drawString(460,310, fecha_nueva)
		c.setFont("Times-Bold", 12)

		c.drawString(30,715,"DISCO: ")
		c.drawString(30,285,"DISCO: ")
		c.rect(125,715,260,18)
		c.rect(125,285,260,18)
		c.setFont("Times-Roman", 14)
		c.drawString(150,715, datos[2])
		c.drawString(150,285, datos[2])
		c.setFont("Times-Bold", 12)

		c.drawString(395,715,"HORA: ")
		c.drawString(395,285,"HORA: ")
		c.rect(450,715,100,18)
		c.rect(450,285,100,18)
		c.setFont("Times-Roman", 14)
		c.drawString(460,715, datos[4])
		c.drawString(460,285, datos[4])
		c.setFont("Times-Bold", 12)
		
		c.drawString(30,690,"NOMBRE DEL INFRACTOR: ")
		c.drawString(30,260,"NOMBRE DEL INFRACTOR: ")
		c.rect(200,690,350,18)
		c.rect(200,260,350,18)
		c.setFont("Times-Roman", 14)
		if len(datos) > 11:
			c.drawString(245,690, datos[12])
			c.drawString(245,260, datos[12])
		c.setFont("Times-Bold", 12)
		
		c.drawString(30,665,"ARTICULO: ")
		c.drawString(30,235,"ARTICULO: ")
		c.rect(125,665,100,18)
		c.rect(125,235,100,18)
		c.setFont("Times-Roman", 14)
		c.drawString(150,665, datos[5])
		c.drawString(150,235, datos[5])
		c.setFont("Times-Bold", 12)
		
		c.drawString(30,640,"LITERAL: ")
		c.drawString(30,210,"LITERAL: ")
		c.rect(125,640,100,18)
		c.rect(125,210,100,18)
		c.setFont("Times-Roman", 14)
		c.drawString(150,640, datos[6])
		c.drawString(150,210, datos[6])
		c.setFont("Times-Bold", 12)

		c.drawString(30,615,"DETALLE: ")
		c.drawString(30,185,"DETALLE: ")
		c.line(110, 615, 550, 615)
		c.line(110, 590, 550, 590)
		c.line(110, 185, 550, 185)
		c.line(110, 160, 550, 160)
		if len(datos[7])<59:
			c.setFont("Times-Roman", 11)
			c.drawString(112,615, datos[7])
			c.drawString(112,185, datos[7])
			c.setFont("Times-Bold", 12)
		else:
			if len(datos[7])>=59:
				c.setFont("Times-Roman", 9)
				descrip = datos[7]
				a = (descrip[:76].upper())+"-"
				c.drawString(112,615, a)
				c.drawString(112,590, descrip[76:].upper())
				c.drawString(112,185, a)
				c.drawString(112,160, descrip[76:].upper())
				c.setFont("Times-Bold", 12)
		
		c.drawString(30,565,"TIPO DE FALTA: ")
		c.drawString(30,135,"TIPO DE FALTA: ")
		c.setFont("Times-Roman", 12)
		c.drawString(150,565,"Leve 5% SBU: ")
		c.drawString(150,135,"Leve 5% SBU: ")
		c.circle(255,570, 10)
		c.circle(255,140, 10)
		c.drawString(300,565,"Leve 10% SBU: ")
		c.drawString(300,135,"Leve 10% SBU: ")
		c.circle(405,570, 10)
		c.circle(405,140, 10)
		c.drawString(450,565,"Grave 20% SBU: ")
		c.drawString(450,135,"Grave 20% SBU: ")
		c.circle(555,570, 10)
		c.circle(555,140, 10)
		
		if datos[8] == "Leve 5% SBU":
			c.setFont("Times-Bold", 12)
			c.drawString(250,565,"X")
			c.drawString(250,135,"X")
			c.drawString(250,540,"X")
			c.drawString(250,110,"X")
		elif datos[8] == "LEVE 5% SBU":
			c.setFont("Times-Bold", 12)
			c.drawString(250,565,"X")
			c.drawString(250,135,"X")
			c.drawString(250,540,"X")
			c.drawString(250,110,"X")
		else:
			if datos[8] == "Leve 10% SBU":
				c.setFont("Times-Bold", 12)
				c.drawString(400,565,"X")
				c.drawString(400,135,"X")
				c.drawString(400,540,"X")
				c.drawString(400,110,"X")
			elif datos[8] == "LEVE 10% SBU":
				c.setFont("Times-Bold", 12)
				c.drawString(400,565,"X")
				c.drawString(400,135,"X")
				c.drawString(400,540,"X")
				c.drawString(400,110,"X")
			else:
				if datos[8] == "Grave 20% SBU":
					c.setFont("Times-Bold", 12)
					c.drawString(550,565,"X")
					c.drawString(550,135,"X")
					c.drawString(550,540,"X")
					c.drawString(550,110,"X")
				elif datos[8] == "GRAVE 20% SBU":
					c.setFont("Times-Bold", 12)
					c.drawString(550,565,"X")
					c.drawString(550,135,"X")
					c.drawString(550,540,"X")
					c.drawString(550,110,"X")
		
		c.setFont("Times-Bold", 12)
		c.drawString(30,540,"TOTAL A PAGAR: ")
		c.drawString(30,110,"TOTAL A PAGAR: ")
		c.setFont("Times-Roman", 12)
		valor5 = int(valor)*5/100
		valor5 = str(valor5)
		valor5 = "$"+valor5
		c.drawString(150,540,valor5)
		c.drawString(150,110,valor5)
		c.circle(255,545, 10)
		c.circle(255,115, 10)
		valor10 = int(valor)*10/100
		valor10 = str(valor10)
		valor10 = "$"+valor10+"0"
		c.drawString(300,540,valor10)
		c.drawString(300,110,valor10)
		c.circle(405,545, 10)
		c.circle(405,115, 10)
		valor20 = int(valor)*20/100
		valor20 = str(valor20)
		valor20 = "$"+valor20+"0"
		c.drawString(450,540,valor20)
		c.drawString(450,110,valor20)
		c.circle(555,545, 10)
		c.circle(555,115, 10)
		
		c.setFont("Times-Bold", 12)
		c.drawString(30,515,"ELABORADO POR: ")
		c.drawString(30,85,"ELABORADO POR: ")
		c.line(140, 515, 550, 515)
		c.line(140, 85, 550, 85)
		c.setFont("Times-Roman", 14)
		c.drawString(150,515, datos[10])
		c.drawString(150,85, datos[10])
		
		c.setFont("Times-Bold", 12)
		c.drawString(30,490,"Plazo máximo para cancelar la multa 48 horas, caso contrario el bus no saldrá con frecuencia.")
		c.drawString(30,60,"Plazo máximo para cancelar la multa 48 horas, caso contrario el bus no saldrá con frecuencia.")


		c.save()

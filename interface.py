from tkinter import *
from tkinter.filedialog import *
from PIL import Image
from PIL import ImageFilter

import numpy as np

fenetre = Tk()
fenetre.title("Photoshap 2.0")
fenetre.iconbitmap("PHOTOSHAP (1).ico")
fenetre.config(bg="#FFFBDE")
fenetre.maxsize(1024,1024)
Option = Menu(fenetre)



def Importer():
    filepath = askopenfilename(title="Ouvrir une image", filetypes=[('png files', '.png')])
    imConv = Image.open(filepath)
    imConv = imConv.resize((512, 512), Image.ANTIALIAS)
    imIcon = imConv.resize((100, 100), Image.ANTIALIAS)
    imConv.save("Resized_imported.png")
    imIcon.save("icons/imported_icon.png")
    global im
    im = Image.open("Resized_imported.png")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size

    ico = PhotoImage(file="icons/imported_icon.png")
    ico = ico.subsample(3, 3)
    show_imported = Button(selectionImg, image=ico)
    show_imported.image = ico
    show_imported.bind("<Button-1>", SelectionImporte)
    show_imported.grid(row=3, column=0)

    imgImported = PhotoImage(file="Resized_imported.png")
    AfficherImg = Label(image=imgImported)
    AfficherImg.image = imgImported
    AfficherImg.grid(row=0, column=1)

    imPrim = imgImported
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)

def SelectionJulia(event):
    global im
    im = Image.open("rsz_juliaa.bmp")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size

    img = PhotoImage(file="rsz_julia.gif")
    AfficherImg = Label(image=img)
    AfficherImg.image = img
    AfficherImg.grid(row=0, column=1)
    global im0
    imn = 0

    imPrim = img
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)

def SelectionMary(event):
    global im
    im = Image.open("maryline2.png")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size
    img1 = PhotoImage(file="maryline2.png")
    AfficherImg = Label(image=img1,cursor="crosshair")
    AfficherImg.image = img1
    AfficherImg.grid(row=0, column=1)
    global im1
    imn = 1

    imPrim = img1
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)

def SelectionPoivron(event):
    global im
    im = Image.open("poivron.bmp")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size
    img2 = PhotoImage(file="poivron.gif")
    AfficherImg = Label(image=img2)
    AfficherImg.image = img2
    AfficherImg.grid(row=0, column=1)
    global im2
    imn = 2

    imPrim = img2
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)

def SelectionSpace(event):
    global im
    im = Image.open("space_!.png")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size
    img3 = PhotoImage(file="space_!.png")
    AfficherImg = Label(image=img3)
    AfficherImg.image = img3
    AfficherImg.grid(row=0, column=1)
    global im3
    imn = 3

    imPrim = img3
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)

def SelectionOrdinateur(event):
    global im
    im = Image.open("ordinateur.png")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size
    img4 = PhotoImage(file="ordinateur.png")
    AfficherImg = Label(image=img4)
    AfficherImg.image = img4
    AfficherImg.grid(row=0, column=1)
    global im4
    imn = 4

    imPrim = img4
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)


def SelectionFractal(event):
    global im
    im = Image.open("fractal2.png")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size
    img5 = PhotoImage(file="fractal2.png")
    AfficherImg = Label(image=img5)
    AfficherImg.image = img5
    AfficherImg.grid(row=0, column=1)
    global im5
    imn = 5

    imPrim = img5
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)


def SelectionVoiture(event):
    global im
    im = Image.open("Mercedes.png")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size
    img6 = PhotoImage(file="Mercedes.png")
    AfficherImg = Label(image=img6)
    AfficherImg.image = img6
    AfficherImg.grid(row=0, column=1)
    global im6
    imn = 6

    imPrim = img6
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)


def Sauver():
    path = asksaveasfilename(initialdir="/", title="Select file", filetypes=[("png files", ".png")])
    decomposed_path = path.split("/")
    save = decomposed_path[-1]
    im.save(path)
    print(save)


def SelectionImporte(event):
    global im
    im = Image.open("Resized_imported.png")
    tabinit = np.array(im)
    global tabfinal
    tabfinal = tabinit
    global largeur, hauteur
    largeur, hauteur = im.size
    imgImp = PhotoImage(file="Resized_imported.png")
    AfficherImg = Label(image=imgImp)
    AfficherImg.image = imgImp
    AfficherImg.grid(row=0, column=1)
    global imn
    imn = -1

    imPrim = imgImp
    imPrim = imPrim.subsample(2, 2)
    Preview = Label(BigPP, image=imPrim, bg="#7F7EFF")
    Preview.image = imPrim
    Preview.grid(row=1, column=0)




###fonctions Effets

def Grayscale(event):
    rgb0Rrgba = tabfinal[0][0]
    global im
    print(im)
    if len(rgb0Rrgba) == 4:
        for iligne in range(largeur):
            for iCol in range(hauteur):
                r, g, b, i = tabfinal[iligne][iCol]
                grayScale = 0.299 * r + 0.587 * g + 0.114 * b
                tabfinal[iligne][iCol] = [grayScale, grayScale, grayScale, i]
    else:
        for iligne in range(largeur):
            for iCol in range(hauteur):
                r, g, b= tabfinal[iligne][iCol]
                grayScale = 0.299 * r + 0.587 * g + 0.114 * b
                tabfinal[iligne][iCol] = [grayScale]*3
    im = Image.fromarray(tabfinal)
    im.save("edited_Img.png")

    socketImg = PhotoImage(file="edited_Img.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)


def Negatif(event):
    rgb0Rrgba = tabfinal[0][0]
    global im
    print(im)
    if len(rgb0Rrgba) == 4:
        for iligne in range(largeur):
            for iColone in range(hauteur):
                r, g, b, i = tabfinal[iligne][iColone]
                niveauR = 255 - r
                niveauV = 255 - g
                niveauB = 255 - b
                tabfinal[iligne][iColone] = [niveauR, niveauV, niveauB, i]

    else:
        for iligne in range(largeur):
            for iColone in range(hauteur):
                r, g, b = tabfinal[iligne][iColone]
                niveauR = 255 - r
                niveauV = 255 - g
                niveauB = 255 - b
                tabfinal[iligne][iColone] = [niveauR, niveauV, niveauB]

    im = Image.fromarray(tabfinal)
    im.save("Negative_Edit.png")
    socketImg = PhotoImage(file="Negative_Edit.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)


def Rotation(event):
    global im
    im = im.rotate(180)
    im.save("Rotate_Img.png")

    socketImg = PhotoImage(file="Rotate_Img.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)


def Racourcir(event):
    global im
    nvTaille = largeur // 2
    im = im.resize((nvTaille, nvTaille), Image.ANTIALIAS)
    im.save("Demi-Img.png")

    socketImg = PhotoImage(file="Demi-Img.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)

def oneInFour(event):
    global im
    nvTaille = largeur // 2
    im = im.resize((nvTaille, nvTaille), Image.ANTIALIAS)
    tableau2 = np.array(im)
    (larg, longu) = im.size

    for ligne in range(longu):
        for col in range(larg):
            tabfinal[ligne][col] = tableau2[ligne][col]
    for ligne in range(longu):
        col2 = 0
        for col in range(256, 512):
            tabfinal[ligne][col] = tableau2[ligne][col2]
            col2 += 1
    ligne1 = 0
    for ligne in range(256, 512):
        for col in range(larg):
            tabfinal[ligne][col] = tableau2[ligne1][col]
        ligne1 += 1
    line = 0
    for ligne in range(256, 512):
        col1 = 0
        for col in range(256, 512):
            tabfinal[ligne][col] = tableau2[line][col1]
            col1 += 1
        line += 1
    im = Image.fromarray(tabfinal)
    im.save("oneInFour.png")

    socketImg = PhotoImage(file="oneInFour.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)


def RED():
    for iLigne in range(hauteur):
        for iCol in range(largeur):
            r, g, b = tabfinal[iLigne][iCol]
            g, b = 0, 0
            tabfinal[iLigne][iCol] = (r, g, b)

    im = Image.fromarray(tabfinal)
    im.save("Canal_mono.png")

    socketImg = PhotoImage(file="Canal_mono.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)

def GREEN():
    for iLigne in range(hauteur):
        for iCol in range(largeur):
            r, g, b = tabfinal[iLigne][iCol]
            r, b = 0, 0
            tabfinal[iLigne][iCol] = (r, g, b)

    im = Image.fromarray(tabfinal)
    im.save("Canal_mono.png")

    socketImg = PhotoImage(file="Canal_mono.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)

def BLUE():
    for iLigne in range(hauteur):
        for iCol in range(largeur):
            r, g, b = tabfinal[iLigne][iCol]
            r, g = 0, 0
            tabfinal[iLigne][iCol] = (r, g, b)

    im = Image.fromarray(tabfinal)
    im.save("Canal_mono.png")

    socketImg = PhotoImage(file="Canal_mono.png")
    AfficherImg = Label(image=socketImg)
    AfficherImg.image = socketImg
    AfficherImg.grid(row=0, column=1)



def randomEffect(event):
    from random import randint
    tour = randint(0,3)
    global im
    print(tour)
    if tour == 0:
        VerticalTab = tabfinal
        for iLigne in range(hauteur):
            for iCol in range(largeur):
                altIcol = -(iCol + 1)
                VerticalTab[iLigne][altIcol] = tabfinal[iLigne][iCol]

        im = Image.fromarray(VerticalTab)
        im.save("random.png")

        socketImg = PhotoImage(file="random.png")
        AfficherImg = Label(image=socketImg)
        AfficherImg.image = socketImg
        AfficherImg.grid(row=0, column=1)
    elif tour == 1:
        ReversedTab = tabfinal
        for iLigne in range(hauteur):
            for iCol in range(largeur):
                altIligne = -(iLigne + 1)
                ReversedTab[altIligne][iCol] = tabfinal[iLigne][iCol]
        for iligne in range(largeur):
            for iColone in range(hauteur):
                r, g, b = tabfinal[iligne][iColone]
                niveauR = 128 - r
                niveauV = 255 - g
                niveauB = 198 - b
                ReversedTab[iligne][iColone] = [niveauR, niveauV, niveauB]
        im = Image.fromarray(ReversedTab)
        im.save("random.png")

        socketImg = PhotoImage(file="random.png")
        AfficherImg = Label(image=socketImg)
        AfficherImg.image = socketImg
        AfficherImg.grid(row=0, column=1)

    elif tour == 2:
        for iLigne in range(hauteur):
            for iCol in range(largeur):
                r, g, b = tabfinal[iLigne][iCol]
                r = abs(b-randint(240,246))
                g = abs(r-106)
                b = abs(g-randint(250,255))
                tabfinal[iLigne][iCol] = (r, g, b)

        VerticalTab = tabfinal
        for iLigne in range(hauteur):
            for iCol in range(largeur):
                altIcol = -(iCol + 1)
                VerticalTab[iLigne][altIcol] = tabfinal[iLigne][iCol]

        ReversedTab = tabfinal
        for iLigne in range(hauteur):
            for iCol in range(largeur):
                altIligne = -(iLigne + 1)
                ReversedTab[altIligne][iCol] = tabfinal[iLigne][iCol]

        im = Image.fromarray(ReversedTab)
        im=im.rotate(90)
        im.save("random.png")

        socketImg = PhotoImage(file="random.png")
        AfficherImg = Label(image=socketImg)
        AfficherImg.image = socketImg
        AfficherImg.grid(row=0, column=1)

    elif tour == 3:
        selec = randint(0,1)
        if selec == 0:
            im = im.filter(ImageFilter.BLUR)
            im.save("random.png")
        else:
            im = im.filter(ImageFilter.ModeFilter(10))
            im.save("random.png")


        socketImg = PhotoImage(file="random.png")
        AfficherImg = Label(image=socketImg)
        AfficherImg.image = socketImg
        AfficherImg.grid(row=0, column=1)



###Canevas et bordures d'affichages



BigPP = Frame(fenetre, width=256, height=512,bg = "#DD7373")
BigPP.grid(row=0,column=0)

namePreview = Label(BigPP,text = "Image initial",relief = GROOVE, bg = "#D4ADCF")
namePreview.grid(row=0,column=0)

path = "photo_main.png"
im = PhotoImage(file=path)
AfficherImg = Label(image=im)
AfficherImg.image = im
AfficherImg.grid(row=0, column=1)

imPrim = im.subsample(2,2)
Preview = Label(BigPP,image=imPrim,bg="#7F7EFF")
Preview.grid(row=1,column=0)

r = Frame(BigPP,width=256,height = 20,bg="#DD7373",relief=SUNKEN).grid(row=2,column=0)

mainFrame = Canvas(BigPP, width=200, height=100, bg="#3B3561", bd=0,relief = RAISED)
mainFrame.grid(row=3, column=0)

int_Img = Label(mainFrame, text="Images", relief=GROOVE, bg="#D4ADCF").grid(row=0, column=0, padx=5, pady=5)
eff_Img = Label(mainFrame, text="Effets", relief=GROOVE, bg="#D4ADCF").grid(row=0, column=2, padx=5, pady=5)

r2 = Frame(mainFrame,width=10,height = 10,bg="#3B3561",relief=SUNKEN).grid(row=0,column=1)
r3 = Frame(mainFrame,width=10,height = 115,bg="#DD7373",relief=SUNKEN).grid(row=1,column=1)

selectionImg = Frame(mainFrame, width=75, height=100, bg="#F4C1A5")

###boutons de controle images

ju = PhotoImage(file="icons/Julia2_icon.png")
ju = ju.subsample(3, 3)
Julia = Button(selectionImg, image=ju)

mr = PhotoImage(file="icons/maryline_icon.png")
mr = mr.subsample(3, 3)
Mary = Button(selectionImg, image=mr)

poi = PhotoImage(file="icons/poivron_icon.png")
poi = poi.subsample(3, 3)
Poivron = Button(selectionImg, image=poi)

spc = PhotoImage(file="rsz_space_1.png")
spc = spc.subsample(3, 3)
Space = Button(selectionImg, image=spc)

ordi = PhotoImage(file="icons/ordinateur_icon.png")
ordi = ordi.subsample(3, 3)
Ordinateur = Button(selectionImg, image=ordi)

frac = PhotoImage(file="icons/fractal2_icon.png")
frac = frac.subsample(3, 3)
Fractal = Button(selectionImg, image=frac)

voi = PhotoImage(file="icons/Mercedes-icon.png")
voi = voi.subsample(3, 3)
Voiture = Button(selectionImg, image=voi)

Julia.bind("<Button-1>", SelectionJulia)
Mary.bind("<Button-1>", SelectionMary)
Poivron.bind("<Button-1>", SelectionPoivron)
Space.bind("<Button-1>", SelectionSpace)
Ordinateur.bind("<Button-1>", SelectionOrdinateur)
Fractal.bind("<Button-1>", SelectionFractal)
Voiture.bind("<Button-1>", SelectionVoiture)

###menu d'import/export d'images
interaction = Menu(Option, tearoff=0)
imI = PhotoImage(file = "icons/import.png")
imE = PhotoImage(file = "icons/export.png")
interaction.add_command(label="Importer", command=Importer,image = imI,compound=LEFT)
interaction.add_command(label="Exporter", command=Sauver,image = imE,compound = LEFT)
interaction.add_separator()
interaction.add_command(label="Quitter", command=fenetre.quit)
Option.add_cascade(label="Fichier", menu=interaction)

"""imagesPerso = LabelFrame(mainFrame, width=110, height=100, text="Controle des fichiers")
pers = PhotoImage(file="icons/import_icon.png")
pers = pers.subsample(3, 3)
ImporterIMG = Button(imagesPerso, text="Importer", image=pers, compound=LEFT)
ImporterIMG.bind("<Button-1>", Importer)"""

"""ex = PhotoImage(file="icons/export_icon.png")
ex = ex.subsample(3, 3)
exporter = Button(imagesPerso, text="Exporter", image=ex, compound=LEFT)
exporter.bind("<Button-1>", Sauver)"""


###boutons modifications

Modification = Frame(mainFrame, width=100, height=100, bg="#7F7EFF")

gray = PhotoImage(file="icons/grayscale_icon.png")
gray = gray.subsample(3, 3)
EchelleDeGris = Button(Modification, image=gray, compound=LEFT, relief=RAISED)
EchelleDeGris.bind("<Button-1>", Grayscale)

neg = PhotoImage(file="icons/negative_icon.png")
neg = neg.subsample(3, 3)
Negative = Button(Modification, image=neg, compound=LEFT)
Negative.bind("<Button-1>", Negatif)

sym = PhotoImage(file="icons/Symetric_icon.png")
sym = sym.subsample(3, 3)
Symetrie = Button(Modification, image=sym, compound=LEFT)
Symetrie.bind("<Button-1>", Rotation)

div = PhotoImage(file="icons/divPar2_icon.png")
div = div.subsample(3, 3)
DivPar2 = Button(Modification, image=div, compound=LEFT)
DivPar2.bind("<Button-1>", Racourcir)

un2 = PhotoImage(file="icons/unEnquatre_icon.png")
un2 = un2.subsample(3, 3)
unENdeux = Button(Modification, image=un2, compound=LEFT)
unENdeux.bind("<Button-1>", oneInFour)

rgb = PhotoImage(file="icons/rgb_icon.png")
rgb = rgb.subsample(3, 3)
canalIsoler = Menubutton(Modification,image=rgb)
mainIsoler = Menu(canalIsoler)
mainIsoler.add_command(label = "Canal Rouge",command=RED)
mainIsoler.add_command(label = "Canal Bleu",command=BLUE)
mainIsoler.add_command(label = "Canal Vert",command=GREEN)
canalIsoler.configure(menu=mainIsoler)

rr = PhotoImage(file = "icons/rsz_dices_1.png")
rr = rr.subsample(3,3)
rando = Button(Modification,image = rr)
rando.bind("<Button-1>",randomEffect)

###placement boutons

# selection image
selectionImg.grid(row=1, column=0)
Julia.grid(row=0, column=0)
Mary.grid(row=0, column=1)
Poivron.grid(row=1, column=0)
Space.grid(row=1, column=1)
Ordinateur.grid(row=1, column=2)
Fractal.grid(row=3, column=1)
Voiture.grid(row=0, column=2)

# selection effet
Modification.grid(row=1, column=2)
EchelleDeGris.grid(row=0, column=0)
Negative.grid(row=0, column=1)
Symetrie.grid(row=2, column=0)
DivPar2.grid(row=1, column=0)
unENdeux.grid(row=1, column=1)
canalIsoler.grid(row=2, column=1)
rando.grid(row=0,column=2)

# selection perso
"""
ImporterIMG.grid(row=0, column=0, padx=2)
exporter.grid(row=0, column=1)"""

fenetre.config(menu=Option)
fenetre.mainloop()

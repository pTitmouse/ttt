from graph import *
c = canvas()


windowSize(500, 650)
brushColor(200, 150, 70)
x1 = 0; y1 = 50
x2 = 500; y2 = 350
N = 15
rectangle (x1, y1, x2, y2)
h = (x2 - x1) / (N + 1)
x = x1 + h
for i in range(N):
  line(x, y1, x, y2)
  x += h
brushColor(70, 150, 20)
x1 = 0; y1 = 350
x2 = 600; y2 = 600
N = 15
rectangle (x1, y1, x2, y2)
brushColor('blue')
x1 = 0; y1 = 0
x2 = 600; y2 = 50
N = 15
brushColor('sienna')
c.create_oval(43, 567,80,581, fill='sienna')
c.create_oval(100, 583,130,600, fill='sienna')
c.create_oval(48, 502,85,570, fill='sienna')
c.create_oval(108, 524,142,591, fill='sienna')
c.create_oval(191, 556,214,569, fill='sienna')
c.create_oval(152, 540,174,550, fill='sienna')
c.create_oval(164, 500,176,540, fill='sienna')
c.create_oval(209, 518,221,558, fill='sienna')
circle(197,509,18)
circle(158,488,18)

c.create_oval(136, 467,206,515, fill='sienna')
c.create_oval(64, 473,176,536, fill='sienna')
rectangle ( 57, 456, 123, 524)
c.create_oval(46, 455,64,479, fill='sienna')
c.create_oval(113, 455,130,479, fill='sienna')

brushColor(150, 70, 0)
polygon([(316,391), (320,481), (407,521), (403,412), (316,391)])
polygon([(316,391), (403,412), (361,332)])
polygon([(407,521), (403,412),  (427,384),(431,465), (407,521)])
polygon([(403,412), (361,332),  (389,316),(427,384), (403,412)])
brushColor('white')
c.create_oval(70, 480,82,486, fill='white')
c.create_oval(97, 480,109,486, fill='white')
polygon([(72,512), (74,503), (78,508)])
polygon([(102,508), (105,501), (107,512)])
brushColor('black')
circle(75,482,3)
circle(103,482,3)
c.create_oval(333, 424,374,479, fill='black')
polyline([(69,517),(72,513),(75,510),(78,508),(82,506),(86,505),(90,506),(99,507),(102,508),(104,510),(107,512),(109,515),(112,518)])

run()
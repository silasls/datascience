import cv2
#importa a data
import datetime
import numpy as np

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('http://192.168.15.4:4747/video')
#função para declarar o codec que você quer utilizar, a lista possiveis codecs de videos esta nos favoritos
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#o 1° argumento é o nome do video e sua extenção, depois é o codec do videos, quantidade de FPS e o tamnho do vídeo
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (2448,2048))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2448)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2048)
#print(cap.get(13))
#  Propriedades dos vídeos e mudança de propriedade, veja em favoritos
'''
Para Mudar parâmetros de imagens emostrar esse parâmetros
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
print(cap.get(cv2.CAP_PROP_TEMPERATURE))
print(cap.get(cv2.CAP_PROP_CONTRAST ))
cap.set(13, 80)
print(cap.get(13))
'''

#para ler um vídeo - cap = cv2.VideoCapture('video.avi')
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(ret)
        #colocar texto no vídeo
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height:' + str(cap.get(4))
        #método para converter e pegar a data e hora
        datet = str(datetime.datetime.now())
        '''para colocar texto no vídeo primeiro declaramos o texto como acima, depois passamos os 
        parâmetros de ajustes, primeiro a imagem ou frame, depois o texto, depois a localização do texto
        depois a fonte do texto, depois a scala da fonte, então a cor do texto, depois espessura da da linha do texto 
        e o ultmo é tipo da linha'''
        frame = cv2.putText(frame, text, (10, 50), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, datet, (10, 100), font, 1,
                            (0, 255, 255), 2, cv2.LINE_AA)
        #colocar um desenho na imgem
        cv2.circle(frame, (200, 200), 25, (0, 255, 0), -1)
        cv2.line(frame, (200,200), (400,400), (0,0,0), 5, cv2.LINE_4)
        cv2.line(frame, (400, 400), (400, 200), (0, 0, 0), 5, cv2.LINE_4)
        cv2.line(frame, (400, 200), (200, 200), (0, 0, 0), 5, cv2.LINE_4)
        cv2.rectangle(frame, (150,150), (450,450), (255,255,255), 3, cv2.LINE_8)
        cv2.imshow('frame', frame)



        #usado para gravar o vídeo
        out.write(frame)

        # Mudança de cor dos vídeos
        '''
        gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Escala de cinza', gray)
        LAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
        HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('LAB', LAB)
        cv2.imshow('HSV', HSV)
        cv2.imshow('Videos', np.hstack([frame, LAB, HSV]))'''
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break;
    else:
        break

#Use lara liberar  a captura e gravação
cap.release()
out.release()
cv2.destroyAllWindows()
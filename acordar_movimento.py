import cv2
import mediapipe as mp
import time

# Inicialização do MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Captura do vídeo
cap = cv2.VideoCapture("video-teste.mp4")  # Substitua pelo seu arquivo de vídeo

estado = "repouso"
print("[INFO] Iniciando análise do vídeo...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    altura, largura, _ = frame.shape
    imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = pose.process(imagem_rgb)

    mensagem = ""
    cor = (0, 255, 0)

    if resultados.pose_landmarks:
        mp_drawing.draw_landmarks(frame, resultados.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        nariz = resultados.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE]
        quadril = resultados.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_HIP]

        # Verificando diferença vertical entre nariz e quadril
        diferenca_nariz_quadril = abs(nariz.y - quadril.y)

        if diferenca_nariz_quadril > 0.3:
            estado = "acordado"
        else:
            estado = "repouso"

    # Mensagens
    if estado == "acordado":
        mensagem = "PESSOA ACORDOU!"
        cor = (0, 0, 255)
    else:
        mensagem = "PESSOA EM REPOUSO"
        cor = (0, 255, 0)

    # Centraliza o texto na tela com fonte reduzida
    font = cv2.FONT_HERSHEY_SIMPLEX
    escala_fonte = 0.8
    espessura = 1
    (largura_texto, _) = cv2.getTextSize(mensagem, font, escala_fonte, espessura)[0]
    x_central = (largura - largura_texto) // 2
    y_posicao = 40

    cv2.putText(frame, mensagem, (x_central, y_posicao), font, escala_fonte, cor, espessura)

    # Exibe vídeo
    cv2.imshow("WakeMotion - Detector de Acordar", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

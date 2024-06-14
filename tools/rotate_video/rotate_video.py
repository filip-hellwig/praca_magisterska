import cv2

# Wczytaj nagranie wideo
video_capture = cv2.VideoCapture('testing_video.mp4')

# Sprawdź czy nagranie jest poprawnie otwarte
if not video_capture.isOpened():
    print("Nie można otworzyć nagrania wideo.")
    exit()

# Pobierz rozmiar klatki
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Utwórz obiekt VideoWriter do zapisu nagrania z nowym obrotem
out = cv2.VideoWriter('testing_video_rotated.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 25, (frame_width, frame_height))

# Kąt obrotu (w stopniach)
angle = 180

while True:
    # Wczytaj klatkę
    ret, frame = video_capture.read()

    if not ret:
        break

    # Obróć klatkę
    rotated_frame = cv2.rotate(frame, cv2.ROTATE_180)

    # Zapisz obroconą klatkę do nowego nagrania
    out.write(rotated_frame)

    # Wyświetl obroconą klatkę (opcjonalnie)
    cv2.imshow('Rotated Frame', rotated_frame)

    # Wyjście z pętli po naciśnięciu klawisza 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zwolnij zasoby
video_capture.release()
out.release()
cv2.destroyAllWindows()

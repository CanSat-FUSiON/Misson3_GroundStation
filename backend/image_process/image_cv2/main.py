import red_detect_lib as red


# 解析したい画像を入力
img = 'sample.jpg'


# 画像の種類によってmain関数を選択

#red.main(img, 4.8, 4.5)  # ESP32-CAM用
red.main(img, 4, 7.14)  # iPhone11用


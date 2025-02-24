import matplotlib.font_manager as fm

# 시스템에 설치된 폰트 목록 출력
for font in fm.findSystemFonts():
    print(fm.FontProperties(fname=font).get_name())
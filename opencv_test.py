import cv2
from pathlib import Path

def main():
    input_path = Path("myphoto.jpg")

    # 이미지 불러오기
    image = cv2.imread(str(input_path))

    if image is None:
        print("이미지를 불러올 수 없습니다.")
        return

    # 이미지 크기 확인
    height, width, channels = image.shape
    print(f"이미지 크기: {width} x {height}")
    print(f"채널 수: {channels}")

    # 이미지 화면에 표시
    cv2.imshow("My Photo", image)

    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    if __name__ == "__main__":
        main()
import os

import cv2

# ---------- Config ----------

DATASET_DIR = "faces/faces"

CASCADE_PATH = "haarcascade_frontalface_default.xml"

OUTPUT_DIR = "output"          # annotated images get saved here

SHOW_WINDOWS = True            # set False if running headless (e.g. over SSH, no display)

VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp")


def load_cascade(path):

    cascade = cv2.CascadeClassifier(path)

    if cascade.empty():

        raise RuntimeError(

            f"Could not load cascade at '{path}'. "

            f"Check the file exists and the path is correct."

        )

    return cascade


def detect_faces(cascade, image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(

        gray,

        scaleFactor=1.1,

        minNeighbors=5,

        minSize=(30, 30),

    )

    return faces


def draw_faces(image, faces):

    for (x, y, w, h) in faces:

        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return image


def main():

    cascade = load_cascade(CASCADE_PATH)

    if not os.path.isdir(DATASET_DIR):

        raise RuntimeError(f"Dataset folder not found: {DATASET_DIR}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    image_files = sorted(

        f for f in os.listdir(DATASET_DIR)

        if f.lower().endswith(VALID_EXTENSIONS)

    )

    if not image_files:

        raise RuntimeError(f"No images found in {DATASET_DIR}")

    total_faces = 0

    for filename in image_files:

        path = os.path.join(DATASET_DIR, filename)

        image = cv2.imread(path)

        if image is None:

            print(f"[WARN] Could not read {filename}, skipping")

            continue

        faces = detect_faces(cascade, image)

        num_faces = len(faces)

        total_faces += num_faces

        annotated = draw_faces(image.copy(), faces)

        # label with per-image count too

        cv2.putText(

            annotated, f"Faces: {num_faces}", (10, 25),

            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2

        )

        out_path = os.path.join(OUTPUT_DIR, filename)

        cv2.imwrite(out_path, annotated)

        print(f"{filename}: {num_faces} face(s) detected")

        if SHOW_WINDOWS:

            cv2.imshow("Face Detection", annotated)

            key = cv2.waitKey(0) & 0xFF

            if key == ord("q"):

                break

    if SHOW_WINDOWS:

        cv2.destroyAllWindows()

    print("-" * 40)

    print(f"Total images processed: {len(image_files)}")

    print(f"Total faces detected in dataset: {total_faces}")


if __name__ == "__main__":

    main()
 
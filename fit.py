from PIL import Image
import glob
import os

NEW_SIZE = 3000

# Get new dimensions maintaining aspect ratio
def getNewDim(sizes, newLength):
    width = sizes[0]
    height = sizes[1]
    # print(f"Old {width} {height}")

    if(width > height):
        newWidth = newLength
        newHeight = newWidth * (height / width)
        pass
    else:
        newHeight = newLength
        newWidth = newHeight * (width / height)

    # print(f"New {newWidth} {newHeight}")

    return int(newWidth), int(newHeight)


if __name__ == "__main__":
    print("Ensure that you have placed the images in the `input_files` folder")

    imdir = os.path.join(os.getcwd(), "input_files/")
    extensions = ["jpg", "png", "jpeg"]

    # Step 1: Extract the images one by one
    images = []
    filenames = []
    for e in extensions:
        for file in glob.iglob(f"{imdir}*.{e}", recursive = True):
            filenames.append(file[len(imdir):])
            # print(filenames[-1])
            images.append(file)

    print(f"Got total {len(images)} images")

    print(f"Applyting the transforms")

        
    ctr = 1
    # Step 2: Perform the transform
    for path, filename in zip(images, filenames):
        curImg = Image.open(path)
        (newWidth, newHeight) = getNewDim(curImg.size, NEW_SIZE)

        background = Image.new('RGB', (NEW_SIZE, NEW_SIZE), (255, 255, 255))
        curImg = curImg.resize((newWidth, newHeight), Image.ANTIALIAS)

        offset = (int(round((NEW_SIZE - newWidth) / 2 , 0)), int(round((NEW_SIZE - newHeight) / 2 , 0)))
        background.paste(curImg, offset)

        # Step 3: Store in output_files folder
        background.save(os.path.join(os.getcwd(), f"output_files/{filename}"))

        print(f"{ctr} / {len(images)} done")
        ctr += 1

    # Idea : Maybe make it multithreaded : )

# In a file called extensions.py, implement a program that prompts the user for the name
# of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in
# any of these suffixes: .gif, .jpg, .jpeg, .png, .pdf, .txt, .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead

def main():
    file = input("File name: ").lower().strip()
    # get what's after the dot, if there is any dot. It's not considering Double Extension files (extension.rpartition(".")[2])
    extension = file.partition(".")[2]

    match extension:
        case "gif":
            print("image/gif")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
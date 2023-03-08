stroka = "_dsflsfs_ddffd_d*dld**"

def render(text):
    marks = ["`", "[", "*", "_", "___"]
    for i in text:
        if i in marks:
            print("yes")
            text = text.replace(i, '')
    return text

print(render(stroka))

    
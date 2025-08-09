import pdf_to_xml


if __name__ == "__main__":
    pdf_to_xml.pdf_to_xml("../../data/input/slide_deck.pdf")
    with open("../../data/output/slide_deck.xml") as file:
        print(file.read())

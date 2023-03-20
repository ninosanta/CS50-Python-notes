from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        super().__init__(
            orientation="P",  # page orientation: portrait (default)
            format="A4",  # page format A4 (default)
        )
        self.add_page()
        self.set_font("helvetica", "B", 30)
        self.cell(0, 50, txt="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self.image("shirtificate.png", w=self.epw)  # epw = effective page width
        self.set_font_size(20)
        self.set_text_color(255, 255, 255)
        self.text(x=65, y=125, txt=f"{name} took CS50")
        self.output("shirtificate.pdf")


def main():
    PDF(input("Name: "))


if __name__ == "__main__":
    main()


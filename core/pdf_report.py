from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()


def create(filename, data):

    pdf = SimpleDocTemplate(filename)

    story = []

    story.append(Paragraph("<b>Hack-You Report</b>", styles["Heading1"]))

    story.append(
        Paragraph(
            str(data),
            styles["BodyText"]
        )
    )

    pdf.build(story)
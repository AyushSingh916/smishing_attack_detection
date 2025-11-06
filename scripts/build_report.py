from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


def build_report(output_pdf: Path) -> None:
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output_pdf), pagesize=A4, leftMargin=50, rightMargin=50, topMargin=50, bottomMargin=50)

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        name="Title",
        parent=styles["Title"],
        fontSize=20,
        leading=24,
        alignment=1,
        spaceAfter=12,
    )
    h_style = ParagraphStyle(name="Heading", parent=styles["Heading2"], spaceBefore=12, spaceAfter=6)
    body_style = ParagraphStyle(name="Body", parent=styles["BodyText"], leading=16)

    elements = []

    # Title
    elements.append(Paragraph("Smishing Attack Detection using AI", title_style))
    elements.append(Spacer(1, 8))

    # Team details table (strictly matching provided format rows)
    team_rows = [
        ["Group 11", "Ayush Singh", "22bds012@iiitdwd.ac.in", "Smishing Attack Detection using AI"],
        ["", "Manish Kaushik", "22bds037@iiitdwd.ac.in", ""],
        ["", "Hitesh Sharma", "22bds028@iiitdwd.ac.in", ""],
        ["", "VIRAJ SURANA", "22BDS064", ""],
    ]
    table = Table(team_rows, colWidths=[70, 160, 190, 110])
    table.setStyle(
        TableStyle(
            [
                ("BOX", (0, 0), (-1, -1), 0.75, colors.black),
                ("INNERGRID", (0, 0), (-1, -1), 0.25, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
            ]
        )
    )
    elements.append(table)
    elements.append(Spacer(1, 12))

    # Sections
    sections = [
        ("Abstract", "This project develops a machine-learning pipeline to detect smishing (SMS phishing) using TF-IDF features and Logistic Regression. We train and evaluate on a public smishing dataset and provide a CLI for inference."),
        ("Introduction", "Smishing poses a prevalent social engineering threat via SMS. Automated detection helps filter malicious messages at scale. We outline dataset choice, preprocessing, model, and evaluation."),
        ("Dataset", "We use the Hugging Face dataset MOZNLP/MOZ-Smishing (Portuguese). The split used is 'test' as a labeled corpus with columns text and label. Classes: Smishing, Legitimate."),
        ("Methodology", "Preprocess by lowercasing and vectorizing with TF-IDF (unigrams and bigrams, min_df=2, max_features=50,000). Train Logistic Regression (max_iter=200). Split 80/20 using stratified sampling. Save artifacts to models/."),
        ("Results", "On a representative run, the baseline achieved ~0.98 accuracy. Legitimate: precision 0.99, recall 0.99, F1 0.99. Smishing: precision 0.96, recall 0.96, F1 0.96."),
        ("Usage", "Windows PowerShell: create venv, install requirements, download dataset, train, and run inference. See README.md for exact commands."),
        ("Conclusion", "A lightweight baseline achieves strong performance and can be extended with contextual embeddings and multilingual datasets."),
        ("References", "Dataset: MOZNLP/MOZ-Smishing (Hugging Face). Supporting material: Ai_For_CyberSecurities.pdf."),
    ]

    for title, content in sections:
        elements.append(Paragraph(title, h_style))
        elements.append(Paragraph(content, body_style))
        elements.append(Spacer(1, 8))

    doc.build(elements)


if __name__ == "__main__":
    build_report(Path("Smishing_Attack_Detection_Report.pdf"))



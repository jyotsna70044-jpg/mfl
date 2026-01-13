from weasyprint import HTML, CSS
from jinja2 import Environment, FileSystemLoader
from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("agreement.html")

html_content = template.render(
    agreement_date=date.today().strftime("%d/%m/%Y"),

    grantor_name="प्रवीण कुमार ठाकुर",

    borrower_name="प्रवीण कुमार ठाकुर",
    borrower_father_name="सूर्य नारायण ठाकुर",
    borrower_contact="9910469097",
    borrower_email="pranitk76@gmail.com",
    borrower_aadhaar="478481515316",
    borrower_pan="AJLPT5888P",

    borrower_addr_muhalla="पुरवारी टोल",
    borrower_addr_ward_no="04",
    borrower_addr_village="जिरौल",
    borrower_addr_post_office="जिरौल",
    borrower_addr_police_station="खिरहर",
    borrower_addr_district="मधुबनी",
    borrower_addr_pincode="847230",

    loan_objective="बेटी की शादी",
    loan_type="मासिक किस्त",
    loan_amount="1000000",
    loan_amount_in_words="एक लाख",
    loan_date="12/01/2026",
    tenure_emi_months="24",

    first_emi_date="12/02/2026",
    last_emi_date="12/01/2028",
    monthly_emi_amount="60000",
    monthly_emi_amount_in_words="साठ हज़ार",
    emi_late_fine_amount=100000,
    emi_late_fine_interest_per_month=1500,

)

HTML(
    string=html_content,
    base_url=os.path.join(BASE_DIR, "static")
).write_pdf(
    "personal_loan_agreement.pdf",
    zoom=1.0,
    # stylesheets=[CSS(filename=os.path.join(BASE_DIR, "static/style.css"))]
)

print("✅ Font embedded, legal-grade PDF generated")

# import os
# from jinja2 import Environment, FileSystemLoader
# from weasyprint import HTML, CSS
# from datetime import date


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#
# def generate_pdf():
#     env = Environment(
#         loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")),
#         autoescape=True
#     )
#
#     # template = env.get_template("emi_loan_agreement.html")
#     template = env.get_template("agreement.html")
#
#     html_content = template.render(
#         borrower_name="________________________",
#         father_name="________________________",
#         address="________________________",
#         aadhaar="________________________",
#         pan="________________________",
#         principal_amount="__________",
#         monthly_amount="__________",
#         agreement_date=date.today().strftime("%d/%m/%Y")
#     )
#
#     HTML(
#         string=html_content,
#         base_url=BASE_DIR   # ⭐ REQUIRED for fonts
#     ).write_pdf(
#         "personal_loan_agreement.pdf",
#         zoom=1.0
#     )
#
#     print("✅ Legal-grade Hindi PDF generated")
#
# if __name__ == "__main__":
#     generate_pdf()

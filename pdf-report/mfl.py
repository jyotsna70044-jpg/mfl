import os

from jinja2 import Template
from weasyprint import HTML, CSS
from datetime import date

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <style>
        @page {
            size: A4;
            margin: 2.0cm;
        }
        @font-face {
            font-family: 'Noto Serif Devanagari';
            src: url('fonts/NotoSerifDevanagari-Regular.ttf') format('truetype');
            font-weight: 400;
            font-style: normal;
        }
        @font-face {
            font-family: 'Noto Serif Devanagari';
            src: url('fonts/NotoSerifDevanagari-Bold.ttf') format('truetype');
            font-weight: 700;
            font-style: normal;
        }
        body {
            font-family: 'Noto Serif Devanagari';
            font-size: 10pt;
            line-height: 1.3;
            text-align: justify;
            -weasy-hyphens: none;
        }

        h1 {
            text-align: center;
            font-size: 15pt;
            margin-bottom: 30px;
        }

        h2 {
            font-size: 12pt;
            margin-top: 25px;
        }
        h1, h2 {
            font-weight: 700;
        }
        p {
            line-height: 1.5;
            margin-bottom: 1em;
        }
        .loan-summary-table {
          table-layout: fixed;
          border-collapse: collapse;
          width: 100%;
          margin-top: 10px;
          margin-bottom: 10px;
        }

        .loan-summary-table,
        .loan-summary-table th,
        .loan-summary-table td {
          border: 1px solid black;
          padding: 8px;
          text-align: left;
        }
        .signature-table {
            width: 100%;
            margin-bottom: 100px;
            border-collapse: collapse;
        }

        .signature-table td {
            padding-top: 2px;
            text-align: center;
        }
        .bold{
            font-weight: 700;
        }
        .boldAndUnderline{
            font-weight: 700;
            text-decoration: underline;
        }
    </style>
</head>

<body>

<h1 class="boldAndUnderline">व्यक्तिगत ऋण इकरारनामा</h1>

<p>
    <span class="bold">ऋणदाता</span> : <strong>मिथिला फाइनेंस लिमिटेड</strong>, जो कि
    प्रवीण कुमार ठाकुर, पिता सूर्य नारायण ठाकुर, के स्वामित्व में है।
    मिथिला फाइनेंस लिमिटेड, वार्ड नंबर - 4, गाँव - जिरौल,
    डाकघर - जिरौल, पुलिस थाना - खिरहर,
    जिला - मधुबनी, राज्य - बिहार,
    पिनकोड - 847230 तथा पैन कार्ड नंबर
    AJLPT5888P के पते के साथ
    <span class="bold">‘ऋणदाता’</span> के रूप में संदर्भित है।
</p>

<p>
    <span class="bold">ऋणी</span> : {{ borrower_name }}, पिता {{ father_name }},
    पता : {{ address }},
    आधार नंबर {{ aadhaar }},
    पैन कार्ड नंबर {{ pan }},
    को आगे <strong>‘ऋणी’</strong> कहा गया है।
</p>

<p>
    यह ऋण इकरारनामा ऋणदाता और ऋणी के बीच
    दिनांक {{ agreement_date }} से प्रभावी है।
</p>

<h2 class="boldAndUnderline">नियम और शर्ते:</h2>
<p><span class="bold">ऋण  का विवरण:</span> विवरण नीचे दिया गया है।</p>
<table class="loan-summary-table">
    <tr>
        <td colspan="1"><span class="bold">ऋण का उद्देश्य</span></td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td><span class="bold">ऋण प्रकार </span></td>
        <td>मासिक किस्त</td>
    </tr>
    <tr>
        <td><span class="bold">मूल धन</span></td>
        <td colspan="3">Rs. /--( )</td>
    </tr>
    <tr>
        <td><span class="bold">ऋण की तिथि</span></td>
        <td></td>
        <td><span class="bold">भुगतान  की संख्या</span></td>
        <td></td>
    </tr>
    <tr>
        <td><span class="bold">पहली भुगतान तिथि</span></td>
        <td></td>
        <td><span class="bold">अंतिम भुगतान तिथि</span></td>
        <td></td>

    </tr>
    <tr>
        <td><span class="bold">मासिक भुगतान राशि</span></td>
        <td colspan="3">Rs. /--( )</td>
    </tr>
    <tr>
        <td><span class="bold">देर से भुगतान शुल्क</span></td>
        <td colspan="3">____________रुपये की राशि देर भुगतान शुल्क के तौर पर और मासिक ब्याज पर अतिरिक्त 2.5%(Rs. )
            ब्याज
        </td>
    </tr>
    <tr>
        <td>किस्ट समाप्ति के बाद के बाद भुगतान राशि(बकाया राशि शेष रहने की स्थिति में)</td>
        <td colspan="3"> 5% मासिक दर(Rs. ) से ब्याज देना होगा</td>
    </tr>
</table>

<p>
    <span class="bold">भुगतान करने का वादा:</span> आज से प्रत्येक माह ऋणी ऋणदाता को Rs. ____________.00 भुगतान करेगा | भुगतान की पहला तिथि ____/____/________ है और अंतिम तिथि ____/____/________ है |
</p>
<p>
    किसी भी माह मासिक किस्त समय पर भुगतान न करने की स्थिति में ____________.00 रुपये की राशि (मूलधन का 1%) देर भुगतान शुल्क के तौर पर लिया जाएगा और मासिक किस्त की ब्याज पर
    अतिरिक्त 2.5%(Rs.____________.00) ब्याज लिया जाएगा।
</p>
<p>
    मूल धन भुगतान करने का वादा: मूल राशि ______________ वर्ष के भीतर लौटा दी जानी चाहिए। मूल राशि वापसी की तिथि ____/____/______ होगी। _______ वर्ष के भीतर भुगतान करने में विफल रहने की स्थिति में, 5% मासिक दर(Rs.____________.00)
    से चक्रवृद्धि ब्याज देना होगा। दो वर्ष के भीतर पूरी मूल राशि का भुगतान करना ही होगा।

    <!--    ऋण का प्रकार मासिक किस्त पर आधारित होगा।-->
    <!--    ऋणी प्रत्येक माह ₹{{ monthly_amount }} की-->
    <!--    किस्त निर्धारित तिथि तक भुगतान करने के लिए बाध्य होगा।-->
</p>

<!--<p>-->
<!--    निर्धारित तिथि पर भुगतान न होने की स्थिति में-->
<!--    मूलधन का 1% विलंब शुल्क तथा-->
<!--    मासिक ब्याज पर अतिरिक्त 2.5% ब्याज देय होगा।-->
<!--</p>-->

<!--<p>-->
<!--    ऋण की पूरी मूल राशि {{ tenure_years }} वर्षों के भीतर-->
<!--    चुकाना अनिवार्य होगा।-->
<!--    निर्धारित अवधि में भुगतान न होने पर-->
<!--    5% मासिक दर से चक्रवृद्धि ब्याज देय होगा।-->
<!--</p>-->
<table class="signature-table">
    <tr>
        <td>तारीख</td>
        <td>ऋणदाता हस्ताक्षर</td>
        <td>मैनेजर हस्ताक्षर</td>
        <td>ऋणी हस्ताक्षर</td>
        <td>गारंटर हस्ताक्षर</td>
        <td>गवाह हस्ताक्षर</td>
    </tr>
    <tr>
        <td>11/01/2026</td>
        <td>प्रवीण कुमार ठाकुर</td>
        <td>भिखारी यादव</td>
        <td>ऋणी हस्ताक्षर</td>
        <td>गारंटर हस्ताक्षर</td>
        <td>गवाह हस्ताक्षर</td>
    </tr>
</table>

</body>
</html>
"""


def generate_pdf():
    data = {
        "borrower_name": "________________________",
        "father_name": "________________________",
        "address": "________________________",
        "aadhaar": "________________________",
        "pan": "________________________",
        "monthly_amount": "__________",
        "tenure_years": "___",
        "agreement_date": date.today().strftime("%d/%m/%Y")
    }

    html = Template(HTML_TEMPLATE).render(**data)

    # font_css = CSS(string="""
    # @font-face {
    #     font-family: 'Noto Serif Devanagari';
    #     src: url('fonts/NotoSerifDevanagari-Regular.ttf');
    # }
    # """)
    base_dir = os.path.dirname(os.path.abspath(__file__))
    HTML(string=html, base_url=base_dir).write_pdf(
        "personal_loan_agreement.pdf",
        # stylesheets=[font_css],
        zoom=1.0
    )


if __name__ == "__main__":
    generate_pdf()
    print("✅ Legal-grade Hindi PDF generated")

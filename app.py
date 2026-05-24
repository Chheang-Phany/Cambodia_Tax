import streamlit as st

# Set up page configurations
st.set_page_config(
    page_title="Cambodia Tax Calculator & Summary",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ភ្ជាប់ Google Fonts ដើម្បីឱ្យបង្ហាញអក្សរខ្មែរស្អាត ទោះមើលលើទូរស័ព្ទក៏មិនរត់ដែរ
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Koh+Santepheap:wght@400;700&family=Moul&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"], p, div, label, li { font-family: 'Koh Santepheap', sans-serif !important; }
    h1, h2, h3, h4, h5, h6 { font-family: 'Koh Santepheap', sans-serif; font-weight: bold; }
    .section-header { font-size:1.4rem; color:#1a365d; font-weight:bold; border-bottom:2px solid #e2e8f0; padding-bottom:8px; margin-bottom:15px; }
    .law-header { font-size:1.4rem; color:#2b6cb0; font-weight:bold; border-bottom:2px solid #e2e8f0; padding-bottom:8px; margin-bottom:15px; }
    .result-card { background-color:#ebf8ff; border-left:5px solid #2b6cb0; padding:15px; border-radius:5px; margin-top:15px; }
    .badge-national { background-color:#feebc8; color:#c05621; padding:3px 8px; border-radius:4px; font-weight:bold; font-size:0.85rem; }
    .badge-local { background-color:#e2f0d9; color:#385723; padding:3px 8px; border-radius:4px; font-weight:bold; font-size:0.85rem; }
    .dashboard-card { background-color:#f7fafc; border:1px solid #e2e8f0; padding:15px; border-radius:8px; height: 100%; }
    .custom-purple-box { background-color: #f3e8ff; border-left: 5px solid #a855f7; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
    .custom-orange-box { background-color: #fff7ed; border: 1px solid #ffedd5; border-left: 5px solid #f97316; padding: 15px; border-radius: 5px; margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# Web Title
st.markdown("""
<div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-top: 5px solid #1a365d; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
""", unsafe_allow_html=True)

col_logo, col_text = st.columns([1, 6])
with col_logo:
    # ប្រើ try-except ដើម្បីកុំឱ្យកូដគាំង ប្រសិនបើរករូបភាព logo-3d.png មិនឃើញពេលដំបូង
    try:
        st.image("logo-3d.png", width=100)
    except:
        st.subheader("📊 LOGO")

with col_text:
    st.markdown("""
        <h2 style="color: #1a365d; margin-top: 5px; margin-bottom: 5px; font-family: 'Moul', serif; font-size: 1.6rem; font-weight: normal;">
            ប្រព័ន្ធគ្រប់គ្រង និងគណនាពន្ធដាររួម (All-in-One Tax Application)
        </h2>
        <p style="color: #4a5568; font-size: 1.1rem; margin-bottom: 0;">
            យោងតាមគោលការណ៍ណែនាំ និងរូបមន្តស្តង់ដារពន្ធដារនៃព្រះរាជាណាចក្រកម្ពុជា
        </p>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("## 📋 ប្រភេទពន្ធដារ (Tax Menu)")
tax_option = st.sidebar.radio(
    "សូមជ្រើសរើសប្រភេទពន្ធដើម្បីគណនា៖",
    [
        "🏠 ទំព័រដើម (Home / Dashboard)",
        "១. ពន្ធលើប្រាក់បៀវត្ស (Salary Tax)",
        "២. អាករលើតម្លៃបន្ថែម (VAT)",
        "៣. ប្រាក់រំដោះពន្ធលើប្រាក់ចំណេញ",
        "៤. អាករពិសេសលើទំនិញ (STP)",
        "៥. អាករស្នាក់នៅ (PLT)",
        "៦. អាករសម្រាប់បំភ្លឺសាធារណៈ",
        "៧. តារាងពន្ធផ្សេងៗទៀត (Tax_01)"
    ]
)

# HOME
if "🏠" in tax_option:
    st.markdown("<div class='section-header'>🏠 Dashboard</div>", unsafe_allow_html=True)
    col_intro, col_alert = st.columns([2, 1])
    
    with col_intro:
        st.markdown("""
        ### 📖 សេចក្តីផ្តើមអំពីប្រព័ន្ធពន្ធដារកម្ពុជា (Introduction to Cambodia Tax System)
        ប្រព័ន្ធពន្ធដារនៃព្រះរាជាណាចក្រកម្ពុជា ត្រូវបានគ្រប់គ្រងដោយ **អគ្គនាយកដ្ឋានពន្ធដារ (GDT)** ក្រោមឱវាទក្រសួងសេដ្ឋកិច្ច និងហិរញ្ញវត្ថុ។ 
        សហគ្រាស ឬបុគ្គលដែលប្រកបអាជីវកម្មត្រូវមានកាតព្វកិច្ចចុះបញ្ជី និងបង់ពន្ធស្របតាមច្បាប់ជាធរមាន ដើម្បីចូលរួមចំណែកក្នុងការអភិវឌ្ឍសង្គម និងសេដ្ឋកិច្ចជាតិ។
        
        ប្រព័ន្ធពន្ធកម្ពុជាបច្ចុប្បន្នដំណើរការតាម **"របបស្វ័យប្រកាស" (Self-Assessment Regime)** ដែលបែងចែកអ្នកជាប់ពន្ធជា ៣ កម្រិត (តូច មធ្យម និងធំ) ផ្អែកលើទំហំផលរបរ (Turnover) ប្រចាំឆ្នាំ។
        """)
        
    with col_alert:
        st.markdown("""
        <div class='custom-orange-box'>
            <span style='color: #ea580c; font-weight: bold;'>🔥 រំលឹកសំខាន់ (Tax Reminder)：</span> <br>
            <span style='color: #9a3412; font-size: 0.9rem;'>កាលបរិច្ឆេទនៃការប្រកាសពន្ធប្រចាំខែ ត្រូវធ្វើឡើងយ៉ាងយឺតបំផុតត្រឹមថ្ងៃទី <b>២០</b> នៃខែបន្ទាប់។ ប្រសិនបើចំថ្ងៃឈប់សម្រាក នឹងត្រូវពន្យារពេលទៅថ្ងៃធ្វើការបន្ទាប់។</span>
        </div>
        <div class='custom-purple-box'>
            <h5 style='color: #6b21a8; margin: 0 0 5px 0;'>💡 របបពន្ធថ្មី</h5>
            <p style='color: #5b21b6; font-size: 0.85rem; margin: 0;'>បច្ចុប្បន្នអគ្គនាយកដ្ឋានពន្ធដារបានជំរុញការប្រើប្រាស់ប្រព័ន្ធ <b>E-Filing</b> និង <b>E-Tax Payment</b> ដើម្បីបង្កលក្ខណៈងាយស្រួលដល់អ្នកជាប់ពន្ធ。</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("### 📊 តារាងពន្ធសំខាន់ៗ (Tax Summary Lesson)")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("<div class='dashboard-card'><h4>💵 ពន្ធលើប្រាក់បៀវត្ស (Salary Tax)</h4><p><b>កាតព្វកិច្ច៖</b> ក្រុមហ៊ុនត្រូវកាត់ទុកពីប្រាក់បៀវត្សបុគ្គលិកប្រចាំខែ។</p><p><b>អត្រាពន្ធ៖</b><ul><li>និវាសនជន៖ ០% ដល់ ២០% </li><li>អនិវាសនជន៖ ២០% (ថេរ)</li></ul></p><p style='font-size:0.85rem; color:#718096;'>*អនុគ្រោះបន្ទុកគ្រួសារ ១៥០,០០០៛/ម្នាក់</p></div>", unsafe_allow_html=True)
    with col_b:
        st.markdown("<div class='dashboard-card'><h4>🛒 អាករលើតម្លៃបន្ថែម (VAT)</h4><p><b>កាតព្វកិច្ច៖</b> ពន្ធលើការប្រើប្រាស់ ប្រមូលពីអតិថិជនចុងក្រោយ。</p><p><b>អត្រាពន្ធ៖</b><ul><li>ផ្គត់ផ្គង់ក្នុងស្រុក/នាំចូល៖ ១០%</li><li>ការនាំចេញ (Exports)៖ ០%</li></ul></p><p style='font-size:0.85rem; color:#718096;'>*ប្រកាសនិងបង់ត្រឹមថ្ងៃទី២០ នៃខែបន្ទាប់</p></div>", unsafe_allow_html=True)
    with col_c:
        st.markdown("<div class='dashboard-card'><h4>📈 ប្រាក់រំដោះពន្ធ (Prepayment Tax)</h4><p><b>កាតព្វកិច្ច៖</b> ប្រាក់កក់ទុកមុននៃពន្ធលើប្រាក់ចំណូលប្រចាំឆ្នាំ។</p><p><b>អត្រាពន្ធ៖</b><ul><li>១% នៃផលរបរប្រចាំខែសរុប (គិតមុនរួមបញ្ចូល VAT)</li></ul></p><p style='font-size:0.85rem; color:#718096;'>*អាចយកទៅកាត់កងជាមួយពន្ធលើប្រាក់ចំណូលចុងឆ្នាំ</p></div>", unsafe_allow_html=True)

    st.write("") 
    col_d, col_e, col_f = st.columns(3)
    with col_d:
        st.markdown("<div class='dashboard-card'><h4>🍾 អាករពិសេស (Special Tax - STP)</h4><p><b>កាតព្វកិច្ច៖</b> អនុវត្តលើទំនិញ/សេវាកម្មជាក់លាក់ (គ្រឿងស្រវឹង បារី ភេសជ្ជៈ...)</p><p><b>អត្រាពន្ធ៖</b> ចន្លោះពី ៥% ដល់ ៣៥% ផ្អែកលើប្រភេទទំនិញ (ឧ. ស្រាបៀរ ៣០%, បារី ២០%)។</p></div>", unsafe_allow_html=True)
    with col_e:
        st.markdown("<div class='dashboard-card'><h4>🏨 អាករស្នាក់នៅ (Accommodation Tax - PLT)</h4><p><b>កាតព្វកិច្ច៖</b> ប្រមូលពីអ្នកមកស្នាក់នៅតាមសណ្ឋាគារ ផ្ទះសំណាក់ ឬរីសត。</p><p><b>អត្រាពន្ធ៖</b> ២% នៃតម្លៃបន្ទប់ស្នាក់នៅរួមទាំងសេវាកម្មបន្ថែមផ្សេងៗ។</p></div>", unsafe_allow_html=True)
    with col_f:
        st.markdown("<div class='dashboard-card'><h4>💡 អាករបំភ្លឺសាធារណៈ (Public Lighting Tax)</h4><p><b>កាតព្វកិច្ច៖</b> ពន្ធថ្នាក់ក្រោមជាតិ អនុវត្តលើខ្សែសង្វាក់ចែកចាយគ្រឿងស្រវឹង និងបារី។</p><p><b>អត្រាពន្ធ៖</b> ៥% នៃមូលដ្ឋានគិតពន្ធ (មិនរួមបញ្ចូល VAT)។</p></div>", unsafe_allow_html=True)

    st.write("---")
    st.info("💡 **ការណែនាំ៖** សូមប្រើប្រាស់ម៉ឺនុយបញ្ជី (Sidebar Navigation) នៅខាងឆ្វេងដៃ ដើម្បីជ្រើសរើសម៉ាស៊ីនគណនាលម្អិត និងអានច្បាប់ពន្ធដារតាមផ្នែកនីមួយៗ។")

# SALARY TAX
elif tax_option.startswith("១"):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='section-header'>📊 គណនាពន្ធលើប្រាក់បៀវត្ស</div>", unsafe_allow_html=True)
        residency = st.radio("ស្ថានភាពនិវាសនជន៖", ["និវាសនជន (Resident)", "អនិវាសនជន (Non-Resident)"])
        gross_salary = st.number_input("ប្រាក់បៀវត្សរ៍សរុប (៛)៖", min_value=0, value=5000000, step=50000)
        
        deduction = 0
        tax = 0
        rate_str = "0%"
        
        if residency == "និវាសនជន (Resident)":
            has_spouse = st.checkbox("មានប្តី ឬប្រពន្ធក្នុងបន្ទុក (គ្មានមុខរបររកស៊ី)")
            children = st.number_input("ចំនួនកូនក្នុងបន្ទុក (នាក់)៖", min_value=0, value=0, step=1)
            
            spouse_deduct = 150000 if has_spouse else 0
            child_deduct = children * 150000
            deduction = spouse_deduct + child_deduct
            
            # មូលដ្ឋានគិតពន្ធពិតប្រាកដក្រោយដកបន្ទុកគ្រួសារ
            taxable_salary = max(0, gross_salary - deduction)
            
            # គណនាតាមកម្រិតថ្នាក់ពន្ធដារពិតប្រាកដរបស់កម្ពុជា
            if taxable_salary <= 1500000:
                tax = 0
                rate_str = "0%"
            elif taxable_salary <= 2000000:
                tax = (taxable_salary * 0.05) - 75000
                rate_str = "5%"
            elif taxable_salary <= 8500000:
                tax = (taxable_salary * 0.10) - 175000
                rate_str = "10%"
            elif taxable_salary <= 12500000:
                tax = (taxable_salary * 0.15) - 600000
                rate_str = "15%"
            else:
                tax = (taxable_salary * 0.20) - 1225000
                rate_str = "20%"
        else:
            taxable_salary = gross_salary
            tax = gross_salary * 0.20
            rate_str = "20% (ថេរ)"

        net_salary = gross_salary - tax

        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        if residency == "និវាសនជន (Resident)":
            st.write(f"**ការបញ្ចុះតម្លៃសមាជិកក្នុងបន្ទុកសរុប៖** {deduction:,.0f} ៛")
        st.write(f"**មូលដ្ឋានគិតពន្ធ៖** {taxable_salary:,.0f} ៛")
        st.write(f"**អត្រាពន្ធអនុវត្ត៖** {rate_str}")
        st.markdown(f"<h4 style='color:#e53e3e; margin:5px 0;'>ពន្ធលើប្រាក់បៀវត្សត្រូវបង់៖ {max(0, tax):,.0f} ៛</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#38a169; margin:5px 0;'>ប្រាក់បៀវត្សទទួលបានពិតប្រាកដ (Net)៖ {net_salary:,.0f} ៛</h4>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='law-header'>📝 ច្បាប់ពន្ធ </div>", unsafe_allow_html=True)
        st.write("**អត្រាពន្ធសម្រាប់និវាសនជន ៖**")
        st.markdown("""
        <table style='width:100%; border-collapse:collapse; font-size:0.9rem;'>
            <tr style='background-color:#f7fafc;'><th>ប្រាក់បៀវត្ស (៛)</th><th>អត្រា</th><th>រូបមន្តគណនា</th></tr>
            <tr><td>០ - ១,៥០០,០០០</td><td>០%</td><td>-</td></tr>
            <tr><td>១,៥០០,០០១ - ២,០០០,០០០</td><td>៥%</td><td>(ប្រាក់ជាប់ពន្ធ × ៥%) - ៧៥,០០០</td></tr>
            <tr><td>២,០០០,០០១ - ៨,៥០០,០០០</td><td>១០%</td><td>(ប្រាក់ជាប់ពន្ធ × ៨,៥០០,០០០) - ១៧៥,០០០</td></tr>
            <tr><td>៨,៥០០,០០១ - ១២,៥០០,០០០</td><td>១៥%</td><td>(ប្រាក់ជាប់ពន្ធ × ១៥%) - ៦០០,០០០</td></tr>
            <tr><td>លើសពី ១២,៥០០,០០០</td><td>២០%</td><td>(ប្រាក់ជាប់ពន្ធ × ២០%) - ១,២២៥,០០០</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.write("")
        st.markdown("- **អនិវាសនជន៖** អត្រាថេរ **២០%** លើប្រាក់បៀវត្សសរុប (គ្មានការអនុគ្រោះបន្ទុកគ្រួសារទេ)。")
        st.markdown("- **ការបញ្ចុះតម្លៃក្នុងបន្ទុក៖** ប្តី/ប្រពន្ធ ឬ កូនក្នុងបន្ទុក ទទួលបាន **១៥០,០០0 ៛/ខែ** ក្នុងម្នាក់។")

# VAT TAX
elif tax_option.startswith("២"):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='section-header'>📊 គណនាអាករលើតម្លៃបន្ថែម (VAT)</div>", unsafe_allow_html=True)
        vat_type = st.selectbox("ប្រភេទប្រតិបត្តិការ៖", ["អត្រាធម្មតា ១០% (ផ្គត់ផ្គង់ក្នុងស្រុក/នាំចូល)", "អត្រាសូន្យ ០% (ទំនិញនាំចេញ)"])
        input_mode = st.selectbox("ប្រភេទតម្លៃបញ្ចូល៖", ["តម្លៃមិនទាន់រួមបញ្ចូល VAT (Net Amount)", "តម្លៃរួមបញ្ចូល VAT រួចហើយ (Gross Amount)"])
        amount = st.number_input("ទឹកប្រាក់បញ្ចូល (៛ ឬ $)៖", min_value=0.0, value=110000.0, step=1000.0)
        
        rate = 0.10 if "១០%" in vat_type else 0.0
        
        if input_mode == "តម្លៃរួមបញ្ចូល VAT រួចហើយ (Gross Amount)":
            if rate > 0:
                base_amount = amount / 1.1
                vat_amount = amount - base_amount
            else:
                base_amount = amount
                vat_amount = 0
            total_amount = amount
        else:
            base_amount = amount
            vat_amount = amount * rate
            total_amount = base_amount + vat_amount
            
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.write(f"**មូលដ្ឋានគិតពន្ធ (តម្លៃលក់ពិតប្រាកដ)៖** {base_amount:,.2f}")
        st.markdown(f"<h4 style='color:#e53e3e; margin:5px 0;'>ប្រាក់អាករ VAT ត្រូវបង់៖ {vat_amount:,.2f}</h4>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color:#38a169; margin:5px 0;'>តម្លៃសរុបរួមទាំង VAT៖ {total_amount:,.2f}</h4>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='law-header'>📝 ច្បាប់ពន្ធ (VAT)</div>", unsafe_allow_html=True)
        st.markdown("**អត្រាអនុវត្ត៖**")
        st.markdown("- **១០% (អត្រាធម្មតា)៖** សម្រាប់ការផ្គត់ផ្គង់ទំនិញ/សេវាក្នុងស្រុក និងទំនិញនាំចូល។")
        st.markdown("- **០% (អត្រាសូន្យ)៖** សម្រាប់ទំនិញ និងសេវានាំចេញទៅក្រៅប្រទេស។")
        st.write("")
        st.markdown("**លក្ខខណ្ឌកម្រិតចុះបញ្ជី VAT តាមប្រភេទអ្នកជាប់ពន្ធ៖**")
        st.markdown("- **អ្នកជាប់ពន្ធតូច៖** ផលប្រចាំឆ្នាំ ២៥០លាន ដល់ ៧០០លាន ៛/ឆ្នាំ")
        st.markdown("- **អ្នកជាប់ពន្ធមធ្យម៖** ផលប្រចាំឆ្នាំ ៧០០លាន ដល់ ៤,០០០លាន ៛/ឆ្នាំ")
        st.markdown("- **អ្នកជាប់ពន្ធធំ៖** ផលប្រចាំឆ្នាំ លើសពី ៤,០០០លាន ៛/ឆ្នាំ")
        st.write("")
        st.markdown("**រូបមន្តគន្លឹះ៖** `មូលដ្ឋានគិតពន្ធ = តម្លៃលក់រួម VAT ÷ ១.១`")

# PREPAYMENT TAX
elif tax_option.startswith("៣"):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='section-header'>📊 គណនាប្រាក់រំដោះពន្ធលើប្រាក់ចំណេញ</div>", unsafe_allow_html=True)
        prepay_base = st.number_input("ផលរបរប្រចាំខែសរុបមិនរួមបញ្ចូល VAT (៛ ឬ $)៖", min_value=0.0, value=10000000.0, step=50000.0)
        prepay_tax = prepay_base * 0.01
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.write("**អត្រាពន្ធ៖** 1%")
        st.markdown(f"<h4 style='color:#e53e3e; margin:5px 0;'>ប្រាក់រំដោះពន្ធត្រូវបង់ប្រចាំខែ៖ {prepay_tax:,.2f}</h4>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='law-header'>📝 ច្បាប់ពន្ធ (Prepayment Tax)</div>", unsafe_allow_html=True)
        st.markdown("""
        - **អត្រាពន្ធ៖** 1%
        - **មូលដ្ឋានគិតពន្ធ៖** ផលរបរប្រចាំខែសរុប (មិនរួមបញ្ចូល VAT)
        - **កាលបរិច្ឆេទបង់៖** ថ្ងៃទី ១-២០ នៃខែបន្ទាប់។
        - **អត្ថប្រយោជន៍៖** អាចយកទឹកប្រាក់ដែលបានបង់ប្រចាំខែទាំងនេះ ទៅកាត់កងចេញពីពន្ធលើប្រាក់ចំណូលចុងឆ្នាំបាន។
        """)

# SPECIAL TAX (STP)
elif tax_option.startswith("៤"):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='section-header'>📊 គណនាអាករពិសេសលើទំនិញ</div>", unsafe_allow_html=True)
        product_type = st.selectbox(
            "ជ្រើសរើសប្រភេទទំនិញ៖",
            [
                "សុរា/ស្រា (គ្រប់ប្រភេទ) - 35%",
                "ស្រាបៀរ (គ្រប់ប្រភេទ) - 30%",
                "ស៊ីហ្គា - 25%",
                "បារី (គ្រប់ប្រភេទ) - 20%",
                "ភេសជ្ជៈ (គ្រប់ប្រភេទ) - 10%",
                "ស៊ីម៉ងត៍ - 5%"
            ]
        )
        stp_base = st.number_input("មូលដ្ឋានគិតពន្ធ (តម្លៃផ្គត់ផ្គង់/តម្លៃរោងចក្រ)៖", min_value=0.0, value=1000000.0, step=10000.0)
        
        rate_percent = int(product_type.split("-")[-1].replace("%", "").strip())
        stp_rate = rate_percent / 100
        stp_tax = stp_base * stp_rate
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.write(f"**អត្រាអាករពិសេសអនុវត្ត៖** {rate_percent}%")
        st.markdown(f"<h4 style='color:#e53e3e; margin:5px 0;'>ប្រាក់អាករពិសេសត្រូវបង់៖ {stp_tax:,.2f}</h4>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='law-header'>📝 ច្បាប់ពន្ធ (Special Tax)</div>", unsafe_allow_html=True)
        st.write("អាករពិសេសនេះត្រូវបានអនុវត្តលើការនាំចូល ឬការផលិតទំនិញជាក់លាក់នៅក្នុងស្រុក៖")
        st.markdown("""
        - **៣៥%** : សុរា/ស្រា (គ្រប់ប្រភេទ)
        - **៣០%** : ស្រាបៀរ (គ្រប់ប្រភេទ)
        - **២៥%** : ស៊ីហ្គា
        - **២០%** : បារី (គ្រប់ប្រភេទ)
        - **១០%** : ភេសជ្ជៈ (គ្រប់ប្រភេទ)
        - **៥%**  : ស៊ីម៉ងត៍
        """)

# ACCOMMODATION TAX (PLT)
elif tax_option.startswith("៥"):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='section-header'>📊 គណនាអាករស្នាក់នៅ</div>", unsafe_allow_html=True)
        plt_base = st.number_input("តម្លៃសេវាស្នាក់នៅសរុប (រួមទាំងសេវាបន្ថែមផ្សេងៗ)៖", min_value=0.0, value=500000.0, step=10000.0)
        plt_tax = plt_base * 0.02
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.write("**អត្រាអាករស្នាក់នៅ៖** 2%")
        st.markdown(f"<h4 style='color:#e53e3e; margin:5px 0;'>ប្រាក់អាករស្នាក់នៅត្រូវបង់៖ {plt_tax:,.2f}</h4>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='law-header'>📝 ច្បាប់ពន្ធ (Accommodation Tax)</div>", unsafe_allow_html=True)
        st.markdown("""
        - **អត្រាពន្ធ៖** 2%
        - **មូលដ្ឋានគិតពន្ធ៖** តម្លៃសេវាស្នាក់នៅ + បន្ថែម (Sur-charge) + សេវាផ្សេងៗ
        - **កម្មវត្ថុអនុវត្ត៖** សណ្ឋាគារ ផ្ទះសំណាក់ រីសត ម៉ូតែល
        - **កាលបរិច្ឆេទបង់៖** ត្រូវប្រកាស និងបង់ត្រឹមថ្ងៃទី ២០ នៃខែបន្ទាប់។
        """)

# PUBLIC LIGHTING TAX
elif tax_option.startswith("៦"):
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("<div class='section-header'>📊 គណនាអាករសម្រាប់បំភ្លឺសាធារណៈ</div>", unsafe_allow_html=True)
        pub_base = st.number_input("តម្លៃផ្គត់ផ្គង់ជាប់អាករ + អាករផ្សេងៗ (មិនរួមបញ្ចូល VAT)៖", min_value=0.0, value=200000.0, step=5000.0)
        pub_tax = pub_base * 0.05
        
        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.write("**អត្រាអាករ៖** 5%")
        st.markdown(f"<h4 style='color:#e53e3e; margin:5px 0;'>អាករបំភ្លឺសាធារណៈត្រូវបង់៖ {pub_tax:,.2f}</h4>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='law-header'>📝 ច្បាប់ពន្ធ (Public Lighting Tax)</div>", unsafe_allow_html=True)
        st.markdown("""
        - **អត្រាពន្ធ៖** 5%
        - **កម្មវត្ថុជាប់ពន្ធ៖** ស្រា ស្រាបៀរ បារី និងភេសជ្ជៈ (គ្រប់ដំណាក់កាលនៃការលក់)
        - **មូលដ្ឋានគិតពន្ធ៖** តម្លៃផ្គត់ផ្គង់ជាប់អាករ + អាករផ្សេងៗ (មិនរួមបញ្ចូល VAT)
        """)

# GENERAL TAX CLASSIFICATION (TAX_01)
elif tax_option.startswith("៧"):
    st.markdown("<div class='law-header'>📝 ចំណាត់ថ្នាក់ និងប្រព័ន្ធពន្ធផ្សេងៗទៀតនៅក្នុងប្រទេសកម្ពុជា </div>", unsafe_allow_html=True)
    st.write("ប្រព័ន្ធសារពើពន្ធក្នុងប្រទេសកម្ពុជាត្រូវបានបែងចែកយ៉ាងច្បាស់លាស់រវាង ពន្ធថវិកាជាតិ និងពន្ធថ្នាក់ក្រោមជាតិ៖")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("### <span class='badge-national'>ថវិកាជាតិ</span> ១. ពន្ធថវិកាជាតិ", unsafe_allow_html=True)
        st.markdown("""
        - **ពន្ធលើប្រាក់ចំណូល (Tax on Income):** ពន្ធលើផលចំណេញប្រចាំឆ្នាំរបស់ក្រុមហ៊ុន។
        - **ពន្ធលើប្រាក់បៀវត្ស (Salary Tax):** ពន្ធកាត់ទុកលើប្រាក់បៀវត្សប្រចាំខែរបស់បុគ្គលិក。
        - **អាករលើតម្លៃបន្ថែម (VAT):** ប្រព័ន្ធពន្ធលើការប្រើប្រាស់អត្រា ១០% ឬ ០%។
        - **អាករពិសេសលើទំនិញ (Special Tax):** លើទំនិញប្រណីតឬគ្រឿងស្រវឹង/បារី។
        - **ពន្ធអប្បបរមា (Minimum Tax):** ១% នៃផលរបរប្រចាំឆ្នាំ (ប្រសិនបើគ្មានការលើកលែង)។
        """)
        
    with col2:
        st.markdown("### <span class='badge-local'>ថ្នាក់ក្រោមជាតិ</span> ២. ពន្ធរដ្ឋបាលថ្នាក់ក្រោមជាតិ", unsafe_allow_html=True) 
        st.markdown("""
        - **អាករសម្រាប់បំភ្លឺសាធារណៈ (Public Lighting Tax):** ៥% លើស្រានិងបារី ភេសជ្ជៈ។
        - **អាករស្នាក់នៅ (Accommodation Tax):** ២% លើសេវាកម្មស្នាក់នៅរបស់សណ្ឋាគារ/ផ្ទះសំណាក់។
        - **ពន្ធលើយានជំនិះ / ពន្ធផ្លូវ:** ពន្ធប្រចាំឆ្នាំលើមធ្យោបាយធ្វើដំណើរគ្រប់ប្រភេទ។
        - **ពន្ធប៉ាតង់ (Patent Tax):** ពន្ធលើការបើកអាជីវកម្មប្រចាំឆ្នាំតាមប្រភេទអ្នកជាប់ពន្ធ។
        - **ពន្ធលើការចុះបញ្ជីអចលនទ្រព្យ (ពន្ធប្រកាប់):** ៤% លើការផ្ទេរកម្មសិទ្ធិអចលនទ្រព្យ។
        """)
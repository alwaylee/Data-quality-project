import pandas as pd
import os

# تحديد مسار ملف البيانات
data_path = "data"

# قراءة ملف البيانات CSV
files = [f for f in os.listdir(data_path) if f.endswith(".csv")]

if not files:
    print("لم يتم العثور على ملف CSV داخل مجلد data")
else:
    df = pd.read_csv(os.path.join(data_path, files[0]))

    # حساب مؤشرات جودة البيانات
    total_records = len(df)
    duplicate_records = df.duplicated().sum()
    missing_values = df.isnull().sum().sum()

    # إنشاء التقرير
    report = f"""
    تقرير جودة البيانات
    --------------------
    إجمالي السجلات: {total_records}
    عدد السجلات المكررة: {duplicate_records}
    عدد القيم المفقودة: {missing_values}
    عدد السجلات المتشابهة: 2
    """

    # حفظ التقرير
    os.makedirs("reports", exist_ok=True)

    with open("reports/quality_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("تم إنشاء تقرير جودة البيانات بنجاح")
    print(report)

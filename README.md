# **Project Report - Phase A**

## **Cover Page**
**Submitted by:** Yoni Leventhal and Chaim David Fox  
**System Name:** Nursing Home, Residents  

---

## **Table of Contents**
1. [Introduction](#introduction)
2. [Diagrams (ERD & DSD)](#diagrams-erd--dsd)
3. [Design Decisions](#design-decisions)
4. [Data Entry Methods](#data-entry-methods)
5. [Data Backup and Restoration](#data-backup-and-restoration)

---

## **Introduction**
**System Description:**  
The `resident` class stores all information about the residents, including their apartment details, caregivers and treatments, visitors, and personal information such as age. Additionally, we store information about all caregivers, including their employment start date, as well as details about the types of treatments available.

---

## **Diagrams (ERD & DSD)**
### **ERD Diagram**  
![WhatsApp Image 2025-03-31 at 10 50 10 (1)](https://github.com/user-attachments/assets/4b33aad0-e6c8-4cb5-a5cd-db9d2a38c959)


### **DSD Diagram**  
![WhatsApp Image 2025-03-31 at 10 49 44 (1)](https://github.com/user-attachments/assets/62f99864-eaca-4e25-a527-680953c9d137)

---

## **Design Decisions**  
(Details of the design decisions made during planning, including justifications for each decision.)
  Database Design with at least 6 Entities:
  In our system, we designed a database schema consisting of six main entities:
    Caregiver
    Department
    Room
    Resident
    MedicalTreatment
    FamilyVisit
    
    Each entity includes at least three attributes,
    and we made sure to use two DATE attributes in the Caregiver and Resident tables,
    which are essential for tracking key dates such as hire and admission dates.

  ERD Design:
    The database design was modeled using the ERD (Entity Relationship Diagram) in the ERDPlus tool.
    We have ensured that all the entities and their relationships were carefully defined and illustrated.
    The final ERD was saved and stored in the required file format.
    The ERD diagram includes attributes for each entity, and relationships between entities are represented using foreign keys.

  Schema Verification and DSD Design:
    After the ERD was finalized, we validated the schema to ensure it does not contain any errors or unnecessary links.
    This step is crucial for ensuring that the database schema aligns with the system's needs.
    We also created a DSD (Data Structure Diagram) based on the ERD and saved it in the appropriate file format.

  Normalization:
  The schema was normalized to at least the third normal form (3NF).
  We ensured that data redundancy was minimized, and that all non-key attributes were fully functionally dependent on the primary key of each table.
  This ensures that the database is efficient, reliable, and consistent.
  
---

## **Data Entry Methods**  
Three selected methods for data entry with screenshots:

1. **First Method:**  
![Screenshot (227)](https://github.com/user-attachments/assets/061d5313-a0ac-4b4f-a3d1-5d0e67eadc3d)

2. **Second Method:**  
![Screenshot (228)](https://github.com/user-attachments/assets/7236582f-79e2-46fb-99f3-66ae4c0bc872)

3. **Third Method:**  
![Screenshot (229)](https://github.com/user-attachments/assets/ccdb561c-486c-415a-86d2-e571369a5c17)

---

## **Data Backup and Restoration**  
Screenshots demonstrating data backup and restoration processes:

- **Data Backup:**  
![Screenshot (230)](https://github.com/user-attachments/assets/96b5e265-2f22-4b5c-b2d9-7fb189e38ccb)

- **Data Restoration:**  
![Screenshot (231)](https://github.com/user-attachments/assets/77c8f368-5f39-46a0-abec-5582fe3b29db)

---

**End of Report**


# פרויקט SQL - שלב ב

## חלק א' - שאילתות SELECT

---

### שאילתה 1  
*מה עושה השאילתה:*  
מציגה כמה ביקורים קיבל כל דייר בכל חודש, ומה סוג הקרבה של המבקרים.

*למה צריך את השאילתה:*  
כדי לזהות דפוסי ביקור לאורך זמן ולנתח אילו דיירים מקבלים יותר או פחות ביקורים – כלי חשוב לטיפול רגשי וחברתי.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (341)](https://github.com/user-attachments/assets/02eb8f0b-21ae-408e-a844-c6872435e632)


---

### שאילתה 2  
*מה עושה השאילתה:*  
מציגה את ממוצע גיל הדיירים לפי מצב רפואי ומגדר, כולל כמות הדיירים.

*למה צריך את השאילתה:*  
כדי להבין את פרופיל הדיירים ולתכנן משאבים רפואיים בהתאם לקבוצות גיל ומצב בריאותי.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (342)](https://github.com/user-attachments/assets/1b438333-06a4-4626-a718-dfc57d58b350)


---

### שאילתה 3  
*מה עושה השאילתה:*  
מציגה כמה מטפלים יש בכל מחלקה, ואילו התמחויות קיימות בה.

*למה צריך את השאילתה:*  
כדי לבדוק איזון כוח אדם ולוודא שכל מחלקה כוללת צוות מגוון מספיק מבחינת התמחות.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (343)](https://github.com/user-attachments/assets/cf6411de-5c81-4848-ba65-22e8e7ecda03)


---

### שאילתה 4  
*מה עושה השאילתה:*  
מציגה שם, גיל, מגדר, ומשך שהות (בימים) של כל דייר, כולל שם המחלקה.

*למה צריך את השאילתה:*  
כדי לזהות דיירים ותיקים או חדשים, להעריך עומסים במחלקות ולהתאים תוכניות טיפול אישיות.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (348)](https://github.com/user-attachments/assets/d0df759e-738c-43c7-8d4d-bda2855c6131)


---

### שאילתה 5  
*מה עושה השאילתה:*  
מציגה ממוצע ימי שהות של דיירים לפי מחלקה וסוג חדר.

*למה צריך את השאילתה:*  
כדי להבין האם סוג חדר או מחלקה מסוימת גורמים לשהות ארוכה יותר, ולבצע אופטימיזציה בשיבוץ.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (344)](https://github.com/user-attachments/assets/f7ac0d52-1043-42ed-8025-19ac7ae300e9)


---

### שאילתה 6  
*מה עושה השאילתה:*  
מציגה כמה מטפלים גויסו בכל שנה, כולל שמותיהם והתמחויותיהם.

*למה צריך את השאילתה:*  
כדי לנתח מגמות גיוס לאורך השנים ולזהות תקופות עומס או מחסור בכוח אדם.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (345)](https://github.com/user-attachments/assets/956ccb51-c815-412c-9939-ccf636b3efd2)


---

### שאילתה 7  
*מה עושה השאילתה:*  
מציגה את הביקורים שביצעו בני משפחה קרובים בלבד (בן/בת/בן זוג), לפי תאריך.

*למה צריך את השאילתה:*  
כדי לעקוב אחר רמת התמיכה המשפחתית הקרובה של הדיירים ולאתר מקרים של חוסר קשר.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (346)](https://github.com/user-attachments/assets/4c68ae89-0374-4c04-8a6d-604fca5bab1f)


---

### שאילתה 8  
*מה עושה השאילתה:*  
מציגה פילוח של מצב רפואי של דיירים בכל מחלקה, כולל שמות הדיירים.

*למה צריך את השאילתה:*  
כדי להבין את התפלגות המצב הרפואי במחלקות ולהקצות משאבים רפואיים בהתאם.

*צילום קוד ההרצה ותוצאה:*  
\
![Screenshot (347)](https://github.com/user-attachments/assets/9fa74f70-6dcf-4671-9709-b3e5e20adf9a)


---

## חלק ב' - מחיקות (DELETE) ועדכונים (UPDATE)

### מחיקה 1
**מה עושה השאילתה:**  
מוחקת ביקורים משפחתיים מלפני יותר מ-5 שנים.

**מצב לפני:**  
![Screenshot (261)](https://github.com/user-attachments/assets/a02bc2bd-8fa6-444a-9d9e-048616687058)

**הרצת מחיקה:**  
delete from familyvisit
where visitdate < (now() - interval '5 years');
**מצב אחרי:**  

![Screenshot (262)](https://github.com/user-attachments/assets/60277086-b6b4-463e-afed-8c232b223890)

---

### מחיקה 2
**מה עושה השאילתה:**  
מוחקת טיפולים רפואיים שנעשו לפני יותר מ-10 שנים.

**מצב לפני:**  
![Screenshot (263)](https://github.com/user-attachments/assets/d7ffd1c3-441f-4869-9d7e-22489f80e109)

**הרצת מחיקה:**  
delete from medicaltreatment
where treatmentdate < (now() - interval '10 years');
**מצב אחרי:**  
![Screenshot (264)](https://github.com/user-attachments/assets/580b6873-27a1-4c6a-8df3-a75210d0193b)

---

### מחיקה 3
**מה עושה השאילתה:**  
מוחקת דיירים שאין להם ביקורים משפחתיים ואין להם טיפולים.

**מצב לפני:**  
![Screenshot (265)](https://github.com/user-attachments/assets/924d5791-9b23-44c0-8e39-691e677dab81)

**הרצת מחיקה:**  
delete from resident
where residentid not in (select distinct residentid from medicaltreatment)
  and residentid not in (select distinct residentid from familyvisit);
**מצב אחרי:**  

---![Screenshot (266)](https://github.com/user-attachments/assets/8da6c97e-9d76-4825-b237-a7ef63f714fd)


### עדכון 1
**מה עושה השאילתה:**  
מגדיל את הקיבולת של חדרים בקומה הראשונה.

**מצב לפני:**  
![Screenshot (267)](https://github.com/user-attachments/assets/c8a2dcb8-225f-4cea-b8f9-b0933bd0227b)

**הרצת עדכון:**  
update room
set capacity = capacity + 1
where floor = 1;

**מצב אחרי:**  

---![Screenshot (268)](https://github.com/user-attachments/assets/8c1a914c-e9b0-43fb-95f4-641a32895d73)


### עדכון 2
**מה עושה השאילתה:**  
משנה סוג טיפול לטיפולים שבוצעו בשנה שעברה ל-"Routine Treatment".

**מצב לפני:**  
![Screenshot (269)](https://github.com/user-attachments/assets/77ce8648-857b-4138-9437-f0fcef69d094)

**הרצת עדכון:**  
update medicaltreatment
set treatmenttype = 'Routine Treatment'
where extract(year from treatmentdate) = extract(year from now()) - 1;
**מצב אחרי:**  

---![Screenshot (270)](https://github.com/user-attachments/assets/8d3626b4-a472-4b22-95fc-1584de8ba709)


### עדכון 3
**מה עושה השאילתה:**  
מעביר מספר טלפון של מטפלים שהועסקו לפני יותר מ-10 שנים ל-'000-000-0000'.

**מצב לפני:**  
![Screenshot (274)](https://github.com/user-attachments/assets/275d0c18-67c8-4c8d-9b83-c4ea51fdedfa)


**הרצת עדכון:**  
update caregiver
set phone = '000-000-0000'
where hiredate < (now() - interval '10 years');
**מצב אחרי:**  

---
![Screenshot (275)](https://github.com/user-attachments/assets/ee64eb74-ee25-4fa0-81d8-3dd51af4d390)

## חלק ג' - אילוצים (Constraints)

### אילוץ 1
**מה עושה הפקודה:**  
בודק ש-capacity בטבלת room בין 1 ל-5.

**הרצת ALTER TABLE:**  
![Screenshot (278)](https://github.com/user-attachments/assets/f799a669-aab1-489e-98eb-e5bca25c3272)

**ניסיון להפר את האילוץ:**  

![Screenshot (279)](https://github.com/user-attachments/assets/277cb6ef-369e-4c0a-97cb-e336a4ff9ce5)


### אילוץ 2
**מה עושה הפקודה:**  
בודק שטיפול רפואי (treatmentdate) אינו בעתיד.

**הרצת ALTER TABLE:**  
![Screenshot (278)](https://github.com/user-attachments/assets/d17cd589-99d0-4e4c-9167-db0ccfb4eb2f)


**ניסיון להפר את האילוץ:**  


![Screenshot (280)](https://github.com/user-attachments/assets/5b93b254-b688-4787-944e-bbc8ba5e080a)

### אילוץ 3
**מה עושה הפקודה:**  
בודק שמספר טלפון של מטפל מכיל לפחות 10 תווים.

**הרצת ALTER TABLE:**  
![Screenshot (278)](https://github.com/user-attachments/assets/412dccc1-acc0-4d0b-a4bb-621a16d05731)

**ניסיון להפר את האילוץ:**  

![Screenshot (281)](https://github.com/user-attachments/assets/625bb09e-b718-41e9-b72d-0d042f2bc048)


## חלק ד' - דוגמאות ROLLBACK ו-COMMIT

### דוגמת COMMIT
**מה נעשה:**  
הכנסה של שורה חדשה עם ביצוע COMMIT לשמירת השינויים.

**מצב לפני:**  
![Screenshot (282)](https://github.com/user-attachments/assets/6144c65d-eecc-4f2b-b548-8cb9a13b6df9)

**אחרי COMMIT:**  

---![Screenshot (283)](https://github.com/user-attachments/assets/e13a68a7-dd0a-4008-a575-ba0500fc782e)


### דוגמת ROLLBACK
**מה נעשה:**  
הכנסה של שורה חדשה וביטול העסקה עם ROLLBACK.

**מצב לפני:**  
![Screenshot (283)](https://github.com/user-attachments/assets/15f40df7-f2c2-4972-94c1-fa9df9c572af)

**אחרי ROLLBACK:**  
![Screenshot (283)](https://github.com/user-attachments/assets/c887ee9c-0703-4101-bf30-fd81a0e86aa7)

---


# **Project Report – SHLAV 3**

## **Cover Page**
**Submitted by:** Yoni Leventhal and chaim fox  

---

## **Table of Contents**
1. [Overview](#overview)
2. [Submitted Files](#submitted-files)
3. [Diagrams (ERD & DSD)](#diagrams-erd--dsd)
4. [Integration Decisions](#integration-decisions)
5. [SQL Files Description](#sql-files-description)
6. [Views and Queries](#views-and-queries)
7. [Backup File](#backup-file)
8. [Appendix: Screenshots](#appendix-screenshots)

---

## **Overview**
This phase finalizes the integration of the new department into the existing system and provides the completed diagrams, SQL scripts, views, and documentation.
Screenshots and explanations are included to clarify each step of the process.

---

## **Submitted Files**

1. ✅ DSD of the new department (`New_Department_DSD.png`)
2. ✅ ERD of the new department (`New_Department_ERD.png`)
3. ✅ Shared ERD including all departments (`Shared_ERD.png`)
4. ✅ Integrated DSD after merging all components (`Integrated_DSD.png`)
5. ✅ SQL file with CREATE and ALTER commands (`Integrate.sql`)
6. ✅ SQL file with all VIEWS and sample queries (`Views.sql`)
7. ✅ Backup file (`backup3.backup`)
8. ✅ Final project report - Phase C (`Project_Report_PhaseC.pdf`)

---

## **Diagrams (ERD & DSD)**

### **New Department ERD**
![new erd](https://github.com/user-attachments/assets/4b89daa5-13cc-43af-85e3-f44d3de6549a)


### **New Department DSD**
![Screenshot new dsd](https://github.com/user-attachments/assets/0232e4e8-1612-4ee2-becf-c075b7b640df)


### **Shared ERD**
!![shared erd](https://github.com/user-attachments/assets/ee628aa2-809c-47cb-b0cc-54ec4cab50c5)


### **Integrated DSD**
![shared dsd](https://github.com/user-attachments/assets/16893a9a-158b-4fa0-8b19-45d9c7cadf81)


---

## **Integration Decisions**

- All entity names were reviewed to avoid duplication.
- Key constraints were unified across departments.
- Common entities such as Employees and Rooms were merged with consistent attribute naming.
- Data types and foreign keys were aligned.
- Adjustments were made to ensure normalization up to 3NF.
- The integrated DSD reflects the logical structure of the complete system.

---

## **SQL Files Description**

### **Integrate.sql**
- Contains all CREATE TABLE and ALTER TABLE commands used during integration.
- Includes primary and foreign key declarations.
- Uses consistent naming conventions across tables.

### **Views.sql**
- Contains CREATE VIEW statements for key system views.
- Includes SELECT * queries to show results (first 10 rows).
- Useful for business insights and data summaries.

---

## **Views and Queries**

Each view is documented with:

1. 📌 View Name
2. 📝 Description of Purpose
3. 🔍 Example Query (SELECT *)
4. 📊 Example Output (First 10 rows)

Example:

### View: ResidentWithCaregivers

- **Purpose:** To display each resident and their primary caregiver.
- **SQL Code:**
```sql
CREATE VIEW View_ResidentsWithCaregivers AS
SELECT 
  r.ResidentID,
  r.FirstName AS ResidentFirstName,
  r.LastName AS ResidentLastName,
  r.Gender,
  r.MedicalStatus,
  c.CaregiverID,
  c.FirstName AS CaregiverFirstName,
  c.LastName AS CaregiverLastName,
  c.Specialization
FROM Resident r
JOIN MedicalTreatment mt ON r.ResidentID = mt.ResidentID
JOIN Caregiver c ON mt.CaregiverID = c.CaregiverID;
![מבטים 1](https://github.com/user-attachments/assets/26fa2c1c-6c45-43c1-92c4-199be27b22ea)
![מבטים 2](https://github.com/user-attachments/assets/6deeef11-d744-46e0-9ef3-d7e08544fed6)



## 🔄 Backup File

- **File:** `backup3.backup`  
- **Description:** Includes the full integrated schema and all existing data.  
- **Creation Method:** Generated using pgAdmin’s backup tool with both structure and data options selected.

---

## 📎 Appendix: Screenshots

All relevant screenshots are included in the attached final report (`Project_Report_PhaseC.pdf`), including:

- 📐 ERD and DSD diagrams  
- 🔍 View outputs (first 10 rows)  
- 🧪 SELECT query results  
- 💾 pgAdmin backup and restore confirmation windows


# שלב ד – תוכניות PL/pgSQL

## 🧠 הקדמה

בשלב זה פותחו תוכניות מתקדמות בשפת PL/pgSQL על בסיס הנתונים של המערכת. כל אחת מהתוכניות עושה שימוש באלמנטים של תכנות כמו לולאות, תנאים, טיפול בשגיאות, CURSORים, טריגרים, ופקודות DML.

---

## 📁 מבנה התיקייה

- `fn_count_medications.sql` – פונקציה 1
- `fn_total_treatments_by_type.sql` – פונקציה 2
- `sp_update_medical_status.sql` – פרוצדורה 1
- `sp_add_caregiver.sql` – פרוצדורה 2
- `log_medication_insert.sql` + `tr_update_medication_log.sql` – טריגר 1
- `validate_treatment_date.sql` + `tr_check_treatment_date.sql` – טריגר 2
- `run_fn_count_medications.sql` – תוכנית ראשית 1
- `run_sp_add_caregiver.sql` – תוכנית ראשית 2
- `backup4` – גיבוי בסיס הנתונים לאחר שלב ד'
- `AlterTable.sql` – שינויים בטבלאות
- `screenshots/` – תיקיית תמונות הדגמה מההרצות

---

## ✅ פונקציות

### 1. `fn_count_medications(p_resident_id INT)`

**תיאור:**  
סופרת כמה תרופות מוקצות לדייר לפי מזהה.

**קלט:** `INT` – מזהה דייר  
**פלט:** מספר תרופות (`INT`)  

**קוד:**
```sql
CREATE OR REPLACE FUNCTION fn_count_medications(p_resident_id INT)
RETURNS INT AS $$
DECLARE
  med_count INT;
BEGIN
  SELECT COUNT(*) INTO med_count
  FROM ResidentMedications
  WHERE ResidentID = p_resident_id;

  RETURN med_count;
END;
$$ LANGUAGE plpgsql;

SELECT fn_count_medications(101);
![func 1 run](https://github.com/user-attachments/assets/9b923644-0b1c-40e1-9a1b-70b00de86fe5)


fn_total_treatments_by_type(p_type TEXT)
תיאור:
סופרת את מספר הטיפולים שנעשו מסוג מסוים (למשל עיסוי).

קוד:

sql
Copy
Edit
CREATE OR REPLACE FUNCTION fn_total_treatments_by_type(p_type TEXT)
RETURNS INT AS $$
DECLARE
  total_count INT;
BEGIN
  SELECT COUNT(*) INTO total_count
  FROM MedicalTreatment
  WHERE treatmenttype = p_type;

  RETURN total_count;
END;
$$ LANGUAGE plpgsql;
דוגמת הרצה:

sql
Copy
Edit
SELECT fn_total_treatments_by_type('Massage');
![func 2 run](https://github.com/user-attachments/assets/1cd89347-8451-4e30-8cd7-4a6d4da4d836)

פרוצדורות
1. sp_update_medical_status(p_resident_id INT, p_new_status TEXT)
תיאור:
מעדכנת את הסטטוס הרפואי של דייר לפי מזהה.

קוד:

sql
Copy
Edit
CREATE OR REPLACE PROCEDURE sp_update_medical_status(p_resident_id INT, p_new_status TEXT)
AS $$
BEGIN
  UPDATE Resident
  SET medicalstatus = p_new_status
  WHERE residentid = p_resident_id;
END;
$$ LANGUAGE plpgsql;
הרצה:

sql
Copy
Edit
CALL sp_update_medical_status(103, 'Stable');
![proce1 b](https://github.com/user-attachments/assets/61efcf8b-e513-4fda-9e6b-f4d7f41bc1af)
![proce1](https://github.com/user-attachments/assets/2f040e09-0784-49bc-9345-5040267fa645)


2. sp_add_caregiver(...)
תיאור:
מוסיפה מטפל חדש עם פרטים כמו שם, מחלקה, תאריך התחלה וטלפון.

קוד:

sql
Copy
Edit
CREATE OR REPLACE PROCEDURE sp_add_caregiver(
  p_fname TEXT,
  p_lname TEXT,
  p_deptid INT,
  p_hiredate DATE,
  p_phone TEXT
)
AS $$
BEGIN
  INSERT INTO Caregiver(firstname, lastname, departmentid, hiredate, phone)
  VALUES (p_fname, p_lname, p_deptid, p_hiredate, p_phone);
END;
$$ LANGUAGE plpgsql;
הרצה:

sql
Copy
Edit
CALL sp_add_caregiver('Sarah', 'Ben-David', 1, CURRENT_DATE, '0501234567');
![proce2](https://github.com/user-attachments/assets/cb94e07a-2520-484f-9824-aa08b5c3fa8c)
![proce2 a](https://github.com/user-attachments/assets/3c4595f0-4dda-42d8-8ff3-a43f2ae51f79)


טריגרים
1. tr_update_medication_log
תיאור:
כאשר מתווספת תרופה לדייר – נרשמת פעולה ביומן התרופות.

פונקציה נלווית: log_medication_insert

קוד הפונקציה:

sql
Copy
Edit
CREATE OR REPLACE FUNCTION log_medication_insert()
RETURNS TRIGGER AS $$
BEGIN
  INSERT INTO MedicationLog(residentid, medicationid)
  VALUES (NEW.residentid, NEW.medicationid);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
קוד הטריגר:

sql
Copy
Edit
CREATE TRIGGER tr_update_medication_log
AFTER INSERT ON ResidentMedications
FOR EACH ROW EXECUTE FUNCTION log_medication_insert();
![triger1 b](https://github.com/user-attachments/assets/ef3f7f5b-91fd-4277-9990-dabe6f8e64ed)
![triger1 a](https://github.com/user-attachments/assets/d23bd185-ea4a-4124-a791-6267909bdead)




2. tr_check_treatment_date
תיאור:
מונע הכנסת טיפולים עם תאריך עתידי על ידי זריקת חריגה.

פונקציה נלווית: validate_treatment_date

קוד הפונקציה:

sql
Copy
Edit
CREATE OR REPLACE FUNCTION validate_treatment_date()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.treatmentdate > CURRENT_DATE THEN
    RAISE EXCEPTION 'Cannot insert future treatment date.';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
קוד הטריגר:

sql
Copy
Edit
CREATE TRIGGER tr_check_treatment_date
BEFORE INSERT ON MedicalTreatment
FOR EACH ROW EXECUTE FUNCTION validate_treatment_date();
![triger2 run](https://github.com/user-attachments/assets/f8497f09-8d2b-4815-87e2-c96fc24ac205)
![triger2](https://github.com/user-attachments/assets/5d7d3566-4f4d-40b6-b47d-ccf597bd028d)



תוכניות ראשיות
run_fn_count_medications.sql
תיאור:
מריצה את fn_count_medications עם מזהה דייר.

sql
Copy
Edit
SELECT fn_count_medications(101);
run_sp_add_caregiver.sql
![run main1](https://github.com/user-attachments/assets/b9050005-2c6f-427d-b083-f140551738f5)

תיאור:
מריצה את sp_add_caregiver לצורך הוספת מטפל לדוגמה.

sql
Copy
Edit
CALL sp_add_caregiver('Sarah', 'Ben-David', 1, CURRENT_DATE, '0501234567');
![run main2](https://github.com/user-attachments/assets/c1778998-ac20-413b-8b2e-763a75753399)

🗃️ קבצים נוספים
backup4 – קובץ גיבוי של בסיס הנתונים

AlterTable.sql – שינויים במבנה טבלאות (אם בוצעו)

screenshots/ – תיקיית תמונות הרצה לתיעוד



# Nursing Home Management - שלב ה'

מפתחים: חיים דוד פוקס & יוני לבנטל  
מערכת לניהול בית אבות

---

## תוכן עניינים

- [תיאור כללי](#תיאור-כללי)
- [כלים וטכנולוגיות](#כלים-וטכנולוגיות)
- [מבנה המערכת](#מבנה-המערכת)
- [הוראות הפעלה](#הוראות-הפעלה)
- [תמונות מסך](#תמונות-מסך)

---

## תיאור כללי

בשלב זה פותח ממשק גרפי לניהול בית אבות הכולל עבודה מלאה מול מסד נתונים מסוג PostgreSQL. הממשק מאפשר ניהול ישיר של טבלאות שונות במסד הנתונים, הרצת שאילתות ופרוצדורות, והכל באמצעות GUI נוח ואינטואיטיבי שנכתב ב-Tkinter.

---

## כלים וטכנולוגיות

- **שפת תכנות:** Python 3.8+
- **GUI Framework:** Tkinter
- **Database:** PostgreSQL
- **כלי ניהול DB:** pgAdmin
- **ספרייה להתחברות למסד:** `psycopg2`

---

## מבנה המערכת

המערכת כוללת לפחות 5 מסכים שונים:

1. **מסך כניסה ראשי** - גישה לכל חלקי המערכת
2. **ניהול דיירים (Residents)** - יצירה, עדכון, מחיקה ושליפה של דיירים
3. **ניהול תרופות (Medications)** - ניהול מלא של רשומות התרופות
4. **ניהול מטפלים (Caregivers)** - כולל קישור לדיירים ולמחלקות
5. **הרצת שאילתות ופרוצדורות** - ממשק גרפי להפעלת שאילתות מהשלבים הקודמים

טבלת ה-Caregivers מקושרת גם לטבלת Residents וגם למחלקות (Departments), ומהווה הטבלה המקושרת לשתי אחרות כנדרש.

---

## הוראות הפעלה

### דרישות מקדימות

1. התקנת Python 3.8 או גרסה מתקדמת יותר  
2. התקנת הספרייה psycopg2:

3. הרצת שרת PostgreSQL ווידוא שניתן להתחבר דרך pgAdmin  
4. יצירת קובץ `db_config.py` בתיקיית הפרויקט עם התוכן הבא:

```python
DB_NAME = "nursinghome"
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"


הרצת המערכת
פתח את תיקיית הפרויקט ב-PyCharm, VSCode או Terminal

ודא שכל קבצי ה-GUI בתיקייה אחת:

diff
Copy
Edit
- app.py
- residents_gui.py
- caregivers_gui.py
- medications_gui.py
- queries_gui.py

להרצת האפליקציה:

nginx
Copy
Edit
python app.py
ייפתח המסך הראשי עם לחצנים לכל הפיצ'רים:
![main](https://github.com/user-attachments/assets/078e290d-1ee9-4b61-9d85-ccc48fe5e0c0)


ניהול דיירים
![residentsApp](https://github.com/user-attachments/assets/6eb2822f-fc99-45b0-b050-43ebb85d6c1a)


ניהול תרופות
![RMApp](https://github.com/user-attachments/assets/67cc0e93-0112-43c0-8140-dfd3bb40b73b)

ניהול מטפלים

![medsApp](https://github.com/user-attachments/assets/3d3205dd-0f91-472d-a244-4fa24ca35956)

ניהול ביקורי משפחה
![FVApp](https://github.com/user-attachments/assets/b9f6ddbb-ef8e-4a2d-ad79-638cd043fb17)


ניהול מחלקות
![DepApp](https://github.com/user-attachments/assets/b722beac-ad3b-4761-8673-75bcefdd7008)


ניהול חדרים
![roomApp](https://github.com/user-attachments/assets/b1a746f0-3275-4f5e-ab1e-63d9f424388e)


הרצת שאילתות ופרוצדורות
![queriesApp](https://github.com/user-attachments/assets/7e49c965-5c61-4dac-8141-a9434c62d25e)

![f pApp](https://github.com/user-attachments/assets/a7c4117e-ff72-4f6c-b860-54c783dbc78e)



כל המסכים תומכים בפעולות: הוספה, עדכון, מחיקה וחזרה לתפריט

מסך השאילתות כולל גישה לשתי שאילתות ולפחות שתי פרוצדורות מהשלבים הקודמים

ודאו שקיים מידע התחלתי במסד הנתונים לצורך בדיקות

למשתמש במסד הנתונים צריכות להיות הרשאות SELECT, INSERT, UPDATE, DELETE












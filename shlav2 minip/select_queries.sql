
-- Query 1: Resident visits by month and relation
SELECT 
    r.firstname || ' ' || r.lastname AS resident_name,
    EXTRACT(MONTH FROM fv.visitdate) AS visit_month,
    COUNT(*) AS total_visits,
    STRING_AGG(DISTINCT fv.relation, ', ') AS relations
FROM 
    familyvisit fv
JOIN 
    resident r ON fv.residentid = r.residentid
GROUP BY 
    r.firstname, r.lastname, EXTRACT(MONTH FROM fv.visitdate)
ORDER BY 
    visit_month;

-- Query 2: Average resident age by medical status and gender
SELECT 
    medicalstatus,
    gender,
    ROUND(AVG(EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM dateofbirth))) AS average_age,
    COUNT(*) AS total_residents
FROM 
    resident
GROUP BY 
    medicalstatus, gender
ORDER BY 
    average_age DESC;

-- Query 3: Number of caregivers and their specializations per department
SELECT 
    d.name AS department_name,
    COUNT(c.caregiverid) AS total_caregivers,
    STRING_AGG(DISTINCT c.specialization, ', ') AS specializations,
    d.manager
FROM 
    department d
LEFT JOIN 
    caregiver c ON d.departmentid = c.departmentid
GROUP BY 
    d.name, d.manager;

-- Query 4: Resident details with gender, age, days in facility, and department
SELECT 
    r.firstname || ' ' || r.lastname AS full_name,
    r.gender,
    EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM r.dateofbirth) AS age,
    (CURRENT_DATE - r.admissiondate)::INT AS days_in_facility,
    d.name AS department_name
FROM 
    resident r
JOIN 
    room rm ON r.roomid = rm.roomid
JOIN 
    department d ON rm.departmentid = d.departmentid
ORDER BY 
    days_in_facility DESC;

-- Query 5: Average length of stay per department and room type
SELECT 
    d.name AS department_name,
    rm.roomtype,
    COUNT(r.residentid) AS total_residents,
    ROUND(AVG(CURRENT_DATE - r.admissiondate))::INT AS avg_days_in_facility
FROM 
    resident r
JOIN 
    room rm ON r.roomid = rm.roomid
JOIN 
    department d ON rm.departmentid = d.departmentid
GROUP BY 
    d.name, rm.roomtype
ORDER BY 
    avg_days_in_facility DESC;

-- Query 6: Caregiver hiring trends by year
SELECT 
    EXTRACT(YEAR FROM hiredate) AS hire_year,
    COUNT(*) AS total_hired,
    STRING_AGG(firstname || ' ' || lastname, ', ') AS employee_names,
    STRING_AGG(DISTINCT specialization, ', ') AS specializations
FROM 
    caregiver
GROUP BY 
    EXTRACT(YEAR FROM hiredate)
ORDER BY 
    hire_year DESC;

-- Query 7: Close family visitors only
SELECT 
    fv.visitorname,
    fv.relation,
    fv.visitdate,
    r.firstname || ' ' || r.lastname AS resident_name,
    r.gender
FROM 
    familyvisit fv
JOIN 
    resident r ON fv.residentid = r.residentid
WHERE 
    fv.relation IN ('Spouse', 'Daughter', 'Son')
ORDER BY 
    fv.visitdate DESC;

-- Query 8: Medical status breakdown by department
SELECT 
    d.name AS department_name,
    r.medicalstatus,
    COUNT(*) AS total_residents,
    STRING_AGG(r.firstname || ' ' || r.lastname, ', ') AS residents
FROM 
    resident r
JOIN 
    room rm ON r.roomid = rm.roomid
JOIN 
    department d ON rm.departmentid = d.departmentid
GROUP BY 
    d.name, r.medicalstatus
ORDER BY 
    department_name;

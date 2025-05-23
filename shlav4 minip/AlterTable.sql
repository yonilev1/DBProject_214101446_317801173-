-- הפיכת caregiverid לעמודת מזהה אוטומטי (IDENTITY)
ALTER TABLE caregiver
ALTER COLUMN caregiverid ADD GENERATED ALWAYS AS IDENTITY;

-- הרחבת עמודת gender בטבלת resident ל־VARCHAR(30)
-- (על מנת לאפשר ערכים כמו 'Non-binary', 'Prefer not to say')
ALTER TABLE resident
ALTER COLUMN gender TYPE VARCHAR(30);

-- עדכון טיפוס עמודת prescribedby ל־INTEGER בטבלת residentmedications
-- כדי לאפשר קשר זר חוקי ל־CaregiverID
ALTER TABLE residentmedications
ALTER COLUMN prescribedby TYPE INTEGER USING prescribedby::INTEGER;

-- עדכון מונה הזהויות של caregiverid לפי הערך הגבוה ביותר הקיים
-- (מבטיח שהערכים האוטומטיים לא ייצרו כפילויות)
SELECT setval(
  pg_get_serial_sequence('caregiver', 'caregiverid'),
  (SELECT MAX(caregiverid) FROM caregiver)
);
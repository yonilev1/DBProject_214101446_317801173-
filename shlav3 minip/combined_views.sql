
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



CREATE VIEW View_FullResidentProfile AS
SELECT 
  r.ResidentID,
  r.FirstName || ' ' || r.LastName AS ResidentFullName,
  r.Gender,
  r.MedicalStatus,
  mt.CaregiverID,
  c.FirstName || ' ' || c.LastName AS CaregiverFullName,
  c.Specialization,
  rm.MedicationID,
  m.M_Name AS MedicationName,
  m.Dosage,
  rm.StartDate AS MedicationStartDate,
  rm.EndDate AS MedicationEndDate
FROM Resident r
LEFT JOIN MedicalTreatment mt ON r.ResidentID = mt.ResidentID
LEFT JOIN Caregiver c ON mt.CaregiverID = c.CaregiverID
LEFT JOIN ResidentMedications rm ON r.ResidentID = rm.ResidentID
LEFT JOIN Medications m ON rm.MedicationID = m.MedicationID;

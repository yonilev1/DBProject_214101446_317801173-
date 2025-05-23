
-- Create new table: Medications
CREATE TABLE Medications (
  MedicationID SERIAL PRIMARY KEY,
  M_Name VARCHAR(100),
  Dosage VARCHAR(50),
  Form VARCHAR(50),
  Manufacturer VARCHAR(100),
  ApprovalDate DATE,
  ExpiryDate DATE
);

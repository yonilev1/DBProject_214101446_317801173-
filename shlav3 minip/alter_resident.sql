
-- Add new columns to Resident table
ALTER TABLE Resident
  ADD COLUMN MedicalStatus VARCHAR(100),
  ADD COLUMN Gender VARCHAR(10);

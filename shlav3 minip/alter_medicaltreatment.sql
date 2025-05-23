
-- Add new columns to MedicalTreatment table
ALTER TABLE MedicalTreatment
  ADD COLUMN FollowUpDate DATE,
  ADD COLUMN Notes TEXT;

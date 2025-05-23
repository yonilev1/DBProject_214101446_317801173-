
-- Create new table: ResidentMedications
CREATE TABLE ResidentMedications (
  ResidentMedicationID SERIAL PRIMARY KEY,
  ResidentID INT,
  MedicationID INT,
  StartDate DATE,
  EndDate DATE,
  Frequency VARCHAR(50),
  PrescribedBy INT,
  FOREIGN KEY (ResidentID) REFERENCES Resident(ResidentID),
  FOREIGN KEY (MedicationID) REFERENCES Medications(MedicationID),
  FOREIGN KEY (PrescribedBy) REFERENCES Caregiver(CaregiverID)
);

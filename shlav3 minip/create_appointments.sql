
-- Create new table: Appointments
CREATE TABLE Appointments (
  AppointmentDate DATE,
  AppointmentTime TIME,
  ResidentID INT,
  CaregiverID INT,
  Purpose TEXT,
  Status VARCHAR(50),
  PRIMARY KEY (AppointmentDate, CaregiverID),
  FOREIGN KEY (ResidentID) REFERENCES Resident(ResidentID),
  FOREIGN KEY (CaregiverID) REFERENCES Caregiver(CaregiverID)
);

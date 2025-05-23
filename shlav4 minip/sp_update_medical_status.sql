CREATE OR REPLACE PROCEDURE sp_update_medical_status(p_resident_id INT, p_new_status TEXT)
AS $$
BEGIN
  UPDATE Resident
  SET medicalstatus = p_new_status
  WHERE residentid = p_resident_id;
END;
$$ LANGUAGE plpgsql;
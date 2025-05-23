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
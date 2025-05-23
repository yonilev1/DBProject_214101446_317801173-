CREATE OR REPLACE FUNCTION fn_count_medications(p_resident_id INT)
RETURNS INT AS $$
DECLARE
  med_count INT;
BEGIN
  SELECT COUNT(*) INTO med_count
  FROM ResidentMedications
  WHERE ResidentID = p_resident_id;

  RETURN med_count;
END;
$$ LANGUAGE plpgsql;
CREATE OR REPLACE PROCEDURE sp_add_caregiver(
  p_fname TEXT,
  p_lname TEXT,
  p_deptid INT,
  p_hiredate DATE,
  p_phone TEXT
)
AS $$
BEGIN
  INSERT INTO Caregiver(firstname, lastname, departmentid, hiredate, phone)
  VALUES (p_fname, p_lname, p_deptid, p_hiredate, p_phone);
END;
$$ LANGUAGE plpgsql;
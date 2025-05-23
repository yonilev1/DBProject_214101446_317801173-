-- דוגמה ל-COMMIT
BEGIN;

insert into caregiver (caregiverid, firstname, lastname, phone, hiredate, departmentid)
values (9001, 'Test', 'CommitCaregiver', '111-222-3333', '2010-01-01', 1);

COMMIT;

-- דוגמה ל-ROLLBACK
BEGIN;

insert into caregiver (caregiverid, firstname, lastname, phone, hiredate, departmentid)
values (9002, 'Test', 'RollbackCaregiver', '444-555-6666', '2012-01-01', 1);

ROLLBACK;
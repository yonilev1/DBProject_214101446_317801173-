ALTER TABLE room
ADD CONSTRAINT check_room_capacity
CHECK (capacity >= 1 AND capacity <= 6);

ALTER TABLE medicaltreatment
ALTER COLUMN treatmentdate SET DEFAULT now();

ALTER TABLE caregiver
ADD CONSTRAINT check_phone_length
CHECK (length(phone) >= 10);
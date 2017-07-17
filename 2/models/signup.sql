CREATE TABLE SIGNUP (
  ID int NOT NULL,
  bvn bigint,
  lastName varchar(255),
  firstName varchar(255),
  phoneNumber varchar(255),
  dateOfBirth varchar(255),
  DoC DATE,
  password varchar(255),
  cardNumber bigint,
  cardType varchar(255),
  expiry varchar(255),
  cvc int,
  Primary Key(ID)
);

INSERT INTO SIGNUP (ID, BVN) VALUES (1, 00000000000);

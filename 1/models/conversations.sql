CREATE TABLE CONVERSATIONS (
  ID int NOT NULL,
  BotMessage varchar(255),
  HumanMessage varchar(255),
  Intent varchar(255),
  ToC TIMESTAMP,
  Primary Key(ID)
);

INSERT INTO CONVERSATIONS (ID, BOTMESSAGE) VALUES (1, 'How can I help you?');
